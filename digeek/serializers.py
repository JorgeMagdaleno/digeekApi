from rest_framework import serializers
from digeek.models import Imagenes,Eventos,Digeek,Expositor,RedesSociales,RegistroDigeek,Visitante, UserAdminApp

class UserAdminAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdminApp
        fields = '__all__'

class ImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = '__all__'

class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = '__all__'

class DigeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Digeek
        fields = '__all__'

class ExpositorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expositor
        fields = '__all__'

class RedesSocialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedesSociales
        fields = '__all__'

class RegistroDigeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroDigeek
        fields = '__all__'

class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = '__all__'