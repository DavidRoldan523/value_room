import requests as requests_python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def remove_all_whitespaces(sentence):
    return ''.join(sentence.split())


@api_view(['POST'])
def get_url_keyword(request):
    try:
        # domain_adwords
        typedomain = remove_all_whitespaces(request.data.get('typedomain'))
        # b1915aca05c569c0d3c48205c7e673be
        key = remove_all_whitespaces(request.data.get('key'))
        # 10
        display_limit = remove_all_whitespaces(request.data.get('display_limit'))
        # Ph,Po,Pp,Pd,Nq,Cp,Vu,Tr,Tc,Co,Nr,Td
        export_columns = remove_all_whitespaces(request.data.get('export_columns'))
        # tigo.com.sv
        domain = remove_all_whitespaces(request.data.get('domain'))
        # po_asc
        display_sort = remove_all_whitespaces(request.data.get('display_sort'))
        # us
        database = remove_all_whitespaces(request.data.get('database'))
        url = f"https://api.semrush.com/" \
              f"?type={typedomain}" \
              f"&key={key}" \
              f"&display_limit={display_limit}" \
              f"&export_columns={export_columns}" \
              f"&domain={domain}" \
              f"&display_sort={display_sort}" \
              f"&database={database}"
        response = requests_python.get(url)
        print(response.text)
        return Response({'Response': response.text}, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': e}, status.HTTP_400_BAD_REQUEST)
