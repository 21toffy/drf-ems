from django.shortcuts import render
from .models import Question
from .serializers import QuestionSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser


# @api_view(['GET'])
@csrf_exempt
def poll(request):
    if request.method=='GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method=='POST':
        json_parser=JSONParser()
        data = json_parser.parse(request)
        serializer =  QuestionSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, statuss=400)

