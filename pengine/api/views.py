from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password

from api.models import User, Post
from .serializers import UserSerializer, PostSerializer

@api_view(['GET'])
def index(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid() == False: return Response(serializer.errors, status=400)
    hashed_pasword = make_password(request.data['password'])
    print(hashed_pasword)
    serializer.save(password=hashed_pasword)
    return Response(serializer.data, status=201)
    

@api_view(['GET'])
def posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createPost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid() == False: return Response(serializer.errors, status=400)
    serializer.save()
    return Response(serializer.data, status=201)