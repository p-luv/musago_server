import random
import json
from rest_framework.decorators import api_view
from .models import Quiz
from . import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.
from .serializers import QuizSerializer


@api_view(['GET'])
def helloAPI(request):
    return Response("hello World!")

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs =  random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)


class SignupView(APIView):
    def post(self, request):

        if request.META['CONTENT_TYPE'] == "application/json":
            request = json.loads(request.body)
            user = User.objects.create_user(username=request['username'], password=request['password1'])
            profile = models.Profile(user=user, nickname=request['nickname'], carno=request['carno'], optype=request['optype'])

        else :
            user = User.objects.create_user(username=request.data['username'], password=request.data['password1'])
            profile = models.Profile(user=user, nickname=request.data['nickname'], carno=request.data['carno'], optype=request.data['optype'])

            user.save()
            profile.save()


        token = Token.objects.create(user=user)
        return Response({"Token": token.key})



class PointView(APIView):
    def get(self, request, format=None):

        results = models.Point.objects.filter(user=request.user)
        serializer = serializers.PointSerializer(results, many=True)
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):


        # if request.META['CONTENT_TYPE'] == "application/json":
        #     user = authenticate(username=request['username'], password=request['password'])
        # else :
        #     user = authenticate(username=request.data['username'], password=request.data['password'])

        print(request.data['username'])
        print(request.data['password'])
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({"Token": token.key})
        else:
            return Response(status=401)