from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def generate_simple_response(request):
    name = request.GET.get('id')
    email = request.GET.get('email')
    message = request.GET.get('message')

    return Response({'name': name}, status=status.HTTP_200_OK)
