import face_recognition
import numpy as np
import cv2

from rest_framework import serializers
from .models import StoreFace

class StorageFaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreFace
        fields = '__all__'

        
    def create(self, validated_data):

        image = validated_data.get('image')

        if image:
            image_array = np.asarray(bytearray(image.read()), dtype=np.uint8)

            img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_encoding = face_recognition.face_encodings(rgb_img)

            if img_encoding:
                validated_data['encoding'] = img_encoding[0].tolist()

        image.seek(0)

        return super().create(validated_data)
    
class CompareFaceSerializer(serializers.Serializer):
    image = serializers.ImageField()
    encoding = serializers.ListField(child=serializers.FloatField(), required=False)

    def validate_image(self, image):
        image_array = np.asarray(bytearray(image.read()), dtype=np.uint8)

        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img_encoding = face_recognition.face_encodings(rgb_img)

        if not img_encoding:
            raise serializers.ValidationError("No face detected in the image.")

        image.seek(0)
        self.context['encoding'] = img_encoding[0].tolist()

        return img_encoding[0] 