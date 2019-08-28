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
    page = webdriver.Chrome('static/chromedriver')
    page.get(hotel)
    sleep(2)
    # Click in the List of all Language
    page.execute_script("document.querySelector('.hotels-review-list-parts-LanguageFilter__taLnk--3iBfk').click();")
    sleep(2)
    # Click in the Language selected
    page.execute_script(f"document.querySelector('input[value={language}]').click();")
    sleep(2)

    # Get data
    language_id = page.find_element_by_xpath(f'//input[@value="{language}"]').get_attribute('id')
    hotel_name = page.find_element_by_xpath('//h1[@id="HEADING"]').text
    total_reviews = page.find_element_by_xpath(f'//label[@for="{language_id}"]/span[@class="hotels-review-list-parts-LanguageFilter__paren_count--EHwQo"]').text
    hotel_rating = page.find_element_by_class_name('hotels-hotel-review-about-with-photos-Reviews__overallRating--vElGA').text
    stop_loop_for = calculate_stop_reviews(total_reviews)

    url_remove_http = hotel.replace('https://www.tripadvisor.co', '')
    url_split = url_remove_http.split('-Reviews-')
    print(stop_loop_for)
    # Extrac reviews for every Page
    for pagination in range(1, 4):
        try:
            print(f"Reviews Page: {pagination}")
            if pagination == 1:
                # Click in "Read More"
                page.execute_script("document.querySelector('.hotels-review-list-parts-ExpandableReview__cta--3U9OU').click();")
                sleep(2)
            else:
                sleep(2)
                click = (pagination - 1) * 5
                href = url_split[0] + '-Reviews-or' + str(click) + '-' + url_split[1]
                # Click in the next Page
                page.execute_script(f"""document.querySelector('a[href="{href}"]').click();""")
                sleep(4)
                # Click in "Read More"
                page.execute_script("document.querySelector('.hotels-review-list-parts-ExpandableReview__cta--3U9OU').click();")
                sleep(3)

            # Get all Reviews information
            reviews = page.find_elements_by_xpath('//div[@class=""]/div/div[@class="hotels-hotel-review-community-content-Card__ui_card--3kTH_ hotels-hotel-review-community-content-Card__card--1MJgB hotels-hotel-review-community-content-Card__section--28b0a"]')
            reviews_count = 0
            for review in reviews:
                review_dict = {
                    'review_text': review.find_elements_by_xpath('//q[@class="hotels-review-list-parts-ExpandableReview__reviewText--3oMkH"]')[reviews_count].text,
                    'review_date': replace_all_in_string(review.find_elements_by_xpath('//div[@class="hotels-review-list-parts-EventDate__event_date--CRXs4"]')[reviews_count].text, replace_in_reviews_date),
                    'review_header': review.find_elements_by_xpath('//div[@class="hotels-review-list-parts-ReviewTitle__reviewTitle--2Fauz"]')[reviews_count].text,
                    'review_rating': replace_all_in_string(review.find_elements_by_xpath('//div[@class="hotels-review-list-parts-RatingLine__bubbles--1oCI4"]/span')[reviews_count].get_attribute('class'), replace_in_reviews_rating),
                    'review_author': review.find_elements_by_xpath('//a[@class="ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC"]')[reviews_count].text
                }
                review_total_pages.append(review_dict)
                reviews_count += 1
        except Exception:
            print('No llego a la ultima página')

    page.quit()
    data = {
        'hotel_name': hotel_name,
        'total_reviews': total_reviews,
        'ratings': hotel_rating,
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