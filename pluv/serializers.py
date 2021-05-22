from rest_framework import serializers
from .models import Quiz, Point


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer')

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ('user', 'score', 'speed', 'interventions', 'speeding')
