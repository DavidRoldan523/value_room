from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from json import dump
from time import sleep
from selenium import webdriver
from collections import OrderedDict


def replace_all_in_string(text, dic):
    OrderedDict(dic)
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


def calculate_stop_reviews(total_reviews):
    replace_in_total_reviews = {'.': '',
                                '(': '',
                                ')': '', }
    stop_loop_for = int(int(replace_all_in_string(total_reviews, replace_in_total_reviews)) / 5)
    if stop_loop_for % 2 == 0:
        stop_loop_for += 1
    else:
        stop_loop_for += 2
    return stop_loop_for


def get_all_reviews(hotel, language):
    review_total_pages = []
    replace_in_reviews_date = {"Fecha de la estadía:": "",
                               " de ": "-",
                               " ": "01-", }
    replace_in_reviews_rating = {"ui_bubble_rating bubble_": "",
                                 '0': '', }
    replace_in_number_reviews = {"(": "",
                                ")": "",
                                ".": ""}
    replace_in_review_text = {"\n": ". "}
    page = webdriver.Chrome('static/chromedriver.exe')
    page.get(hotel)
    sleep(2)
    # Click in the List of all Language
    #page.execute_script("document.querySelector('.hotels-review-list-parts-LanguageFilter__taLnk--3iBfk').click();")
    sleep(2)
    # Click in the Language selected
    #page.execute_script(f"document.querySelector('input[value={language}]').click();")
    sleep(2)

    # Get data
    language_id = page.find_element_by_xpath(f'//input[@value="{language}"]').get_attribute('id')
    destination_name = page.find_element_by_xpath('//h1[@id="HEADING"]').text
    #total_reviews = page.find_element_by_xpath(f'//label[@for="{language_id}"]/span[@class="hotels-review-list-parts-LanguageFilter__paren_count--EHwQo"]').text
    total_reviews = int(replace_all_in_string(page.find_element_by_css_selector('span.reviews_header_count').text, replace_in_number_reviews))
    destination_rating = replace_all_in_string(page.find_element_by_css_selector('span[class^="ui_bubble_rating bubble_"]').get_attribute('class'), replace_in_reviews_rating)
    stop_loop_for = int(page.find_element_by_css_selector('div.pageNumbers a.pageNum.last.taLnk').text)
    #print(language_id, destination_name, total_reviews, destination_rating, stop_loop_for)

    url_remove_http = hotel.replace('https://www.tripadvisor.co', '')
    url_split = url_remove_http.split('-Reviews-')
    # Extrac reviews for every Page
    for pagination in range(1, stop_loop_for):
        try:
            print(f"Reviews Page: {pagination}")
            if pagination == 1:
                # Click in "Read More"
                #page.execute_script('document.querySelector(\'.hotels-review-list-parts-ExpandableReview__cta--3U9OU\').click();')
                page.execute_script('document.querySelector("span.taLnk.ulBlueLinks").click();')
                sleep(2)
            else:
                sleep(2)
                # Click in the next Page
                page.execute_script("""
                    var element = document.querySelector("div.unified.ui_pagination a.nav.next.taLnk.ui_button.primary");
                    if(element){
                        element.click();
                    }
                """)
                sleep(4)
                # Click in "Read More"
                #page.execute_script("document.querySelector('.hotels-review-list-parts-ExpandableReview__cta--3U9OU').click();")
                page.execute_script("""
                    var element = document.querySelector("span.taLnk.ulBlueLinks");
                    if(element){
                        element.click();
                    }
                """)
                sleep(3)

            # Get all Reviews information
            #reviews = page.find_elements_by_xpath('//div[@class=""]/div/div[@class="hotels-hotel-review-community-content-Card__ui_card--3kTH_ hotels-hotel-review-community-content-Card__card--1MJgB hotels-hotel-review-community-content-Card__section--28b0a"]')
            #reviews = page.find_elements_by_xpath('//div[@data-test-target="reviews-tab"]')
            reviews = page.find_elements_by_css_selector('div#REVIEWS div.listContainer div.review-container')
            reviews_count = 0
            for review in reviews:
                try:
                    review_dict = {
                        'review_text': replace_all_in_string(review.find_element_by_css_selector('div.prw_rup.prw_reviews_text_summary_hsx div.entry p.partial_entry').text, replace_in_review_text),
                        'review_author': review.find_element_by_css_selector('div.prw_rup.prw_reviews_member_info_resp div.member_info div div.info_text div').text,
                        'review_date': review.find_element_by_css_selector('span.ratingDate').get_attribute('title'),
                        'review_header': review.find_element_by_css_selector('div.quote').text,
                        'review_rating': replace_all_in_string(review.find_element_by_css_selector('span[class^="ui_bubble_rating bubble_"]').get_attribute('class'), replace_in_reviews_rating),
                    }
                    #review_dict['review_date'] = review_dict['review_date'].replace(f'{review_dict["review_author"]} escribió una opinión el ', '')
                    #print(review_dict)
                    review_total_pages.append(review_dict)
                    reviews_count += 1
                except Exception as e:
                    print(e, 'Error en review')
                    print(pagination, review)
        except Exception as e:
            print(e, 'No llego a la ultima página')

    page.quit()
    data = {
        'destination_name': destination_name,
        'total_reviews': total_reviews,
        'ratings': destination_rating,
        'language': language,
        'reviews': review_total_pages,
    }
    return data


@api_view(['POST'])
def get_reviews(request):
    response_list = []
    hotels = request.data.get('hotels').split(',')
    language = request.data.get('language')
    for hotel in hotels:
        response = get_all_reviews(hotel, language)
        response_list.append(response)
    return Response(response_list, status.HTTP_200_OK)
