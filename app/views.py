from django.shortcuts import render

from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    #post, dont use serializers
    def post(self, request, *args, **kwargs):
        print(request.data['file'])
        #save the file on local
        file = request.data['file']
        with open(file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
    
        return Response(status=status.HTTP_201_CREATED)
