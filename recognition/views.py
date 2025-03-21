import face_recognition
import numpy as np

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import StoreFace
from .serializers import StorageFaceSerializer, CompareFaceSerializer

@api_view(['POST'])
def upload_image(request):
    serializer = StorageFaceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'data': serializer.data, 'status': status.HTTP_201_CREATED, 'success': True}, status=status.HTTP_201_CREATED)
    return Response({'data': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST, 'success': False}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def compare_faces(request):
    serializer = CompareFaceSerializer(data=request.data)
    if serializer.is_valid():
        uploaded_encoding_img = serializer.context.get('encoding')

        stored_faces = StoreFace.objects.all()
        match = None

        for stored_face in stored_faces:
            stored_encoding = np.array(stored_face.encoding)

            match = face_recognition.compare_faces([np.array(stored_encoding)], np.array(uploaded_encoding_img))[0]

            if match == True:
                return Response({'data': {'name': stored_face.name, 'match': match}, 'status': status.HTTP_200_OK, 'success': True}, status=status.HTTP_200_OK)        
    return Response({'data': {'match': match}, 'status': status.HTTP_404_NOT_FOUND, 'success': False}, status=status.HTTP_404_NOT_FOUND)