from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Tutorial
from .serializers import TutorialSerializer
# Create your views here.


@api_view(['GET'])
def get_tuturial(request):
    tutorial = Tutorial.objects.all()
    tutorial_serializers = TutorialSerializer(tutorial,many = True)
    content = {
        "code":"0",
        "tutorial_list":tutorial_serializers.data}
    return JsonResponse(content, safe=False)

@api_view(['POST'])
def add_tutorial(request):
    tutorial_data = JSONParser().parse(request)
    tutorial_serializer = TutorialSerializer(data=tutorial_data)
    if tutorial_serializer.is_valid():
        tutorial_serializer.save()
        response = {
            "code":"0",
            "message":"succes add tutorial",
            "data":tutorial_serializer.data
        }
        return JsonResponse(response, status=status.HTTP_201_CREATED)
    return JsonResponse(tutorial_serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','DELETE'])
def tutorials(request,id_tutorial):
    try:
        tutorial = Tutorial.objects.get(pk=id_tutorial)
    except Tutorial.DoesNotExist:
        return HttpResponse(status=404)


    tutorialSerializer = TutorialSerializer(tutorial)

    if request.method == 'GET':
        response = {
            "code":"1",
            "detail_tutorial":tutorialSerializer.data
        }
        return Response(response)
    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            response = {
                "code":"1",
                "message":"Updata Tutorail succes"
            }
            return Response(response)
        return JsonResponse(tutorial_serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tutorial.delete()
        response = {'code':'0', 'message':'Deleted Successfully'}
        return JsonResponse(response,status=status.HTTP_204_NO_CONTENT)
