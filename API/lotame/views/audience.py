from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as requests_python
from rest_framework import status

@api_view(['POST'])
def get_audience(request):
    try:
        name = request.data.get('name')
        # key = request.data.get('key')
        url = f"https://api.lotame.com/2/audiences?only_profile=N&name={name}&client_name=AriadnaNetwork"
        response = requests_python.get(url)
        print(url)
        return Response(response.json(), status.HTTP_200_OK)
    except Exception:
        return Response({'Error':'URL incorrecto'}, status.HTTP_400_BAD_REQUEST)

