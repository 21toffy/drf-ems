from rest_framework import serializers
from django.contrib.auth.models import User


from poll.models import Question



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'title',
            'status',
            'created_by'
        ]
    pass
