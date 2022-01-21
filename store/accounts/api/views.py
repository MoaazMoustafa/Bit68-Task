from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialilzers import UserSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def signup(request):
    response = {
        'data': '',
        'status': ''
    }

    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        response['data'] = {'user': user.data, 'token': Token.objects.get(
            user__username=user.data.get('username')).key,
            'message': 'user created successfully'
        }
        response['status'] = status.HTTP_201_CREATED
    else:
        response['data'] = {'user': user.errors,
                            'message': 'try another time 😊😃😃'}
        response['status'] = status.HTTP_400_BAD_REQUEST
    return Response(data=response['data'], status=response['status'])
