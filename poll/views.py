from django.shortcuts import render
from .models import Question
from .serializers import QuestionSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView



class PollAPIView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=200)
    def post(self, request):
        data = request.data
        serializer =  QuestionSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PollDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Question.objects.get(id=id)
        except Question.DoesNotExist as e:
            return Response({'error':'Given question object was not found.'}, status=404)
    def get(self,request, id=None):
        instance=self.get_object(id)
        serializer = QuestionSerializer(instance)
        return Response(serializer.data)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = QuestionSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return Response("data":"data deleted", status=201)



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

