from django.db import transaction, DatabaseError
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from digeek.models import RegistroDigeek
from digeek.serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class RegistrarVisitanteBien(APIView):

    @transaction.atomic
    def post(self, request):
        my_data = JSONParser().parse(request)
        my_serializer1 = VisitanteSerializer(data=my_data["visitante"])

        try:
            if my_serializer1.is_valid():
                visitante = my_serializer1.save()
                digeekObj = Digeek(digeekid=my_data["registro"]["digeek"])
                eventosObj = Eventos(eventosid=my_data["registro"]["eventos"])
                registro = RegistroDigeek(
                    digeek=digeekObj,
                    visitante=visitante,
                    eventos=eventosObj,
                    last_update=my_data["registro"]["last_update"],
                    presencial=my_data["registro"]["presencial"]
                )
                registro.save()
                return JsonResponse("Se añadio correctamente", safe=False)
        except DatabaseError:
            return JsonResponse("No se pudo añadir", safe=False)


class ImagenApiGet(APIView):

    def get(self, request):
        imagenes = Imagenes.objects.all()
        my_serializer = ImagenesSerializer(imagenes, many=True)
        return JsonResponse(my_serializer.data, safe=False)


class ImagenApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        imagenes = Imagenes.objects.all()
        my_serializer = ImagenesSerializer(imagenes, many=True)
        return JsonResponse(my_serializer.data, safe=False)

    def post(self, request):
        my_data = JSONParser().parse(request)
        my_serializer = ImagenesSerializer(data=my_data)
        if my_serializer.is_valid():
            my_serializer.save()
            return JsonResponse("Se añadio correctamente", safe=False)
        return JsonResponse("No se pudo añadir", safe=False)

    def put(self, request):
        my_data = JSONParser().parse(request)
        imagen = Imagenes.objects.get(imagenesid=my_data['imagenesid'])
        my_serializer = ImagenesSerializer(imagen, data=my_data)
        if my_serializer.is_valid():
            my_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")


class ImagenAApiGet(APIView):

    def get(self, request, id=0):
        imagen = Imagenes.objects.get(imagenesid=id)
        my_serializer = ImagenesSerializer(imagen)
        return JsonResponse(my_serializer.data, safe=False)


class ImagenAApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=0):
        imagen = Imagenes.objects.get(imagenesid=id)
        my_serializer = ImagenesSerializer(imagen)
        return JsonResponse(my_serializer.data, safe=False)

    def delete(self, request, id=0):
        imagen = Imagenes.objects.get(imagenesid=id)
        imagen.delete()
        return JsonResponse("Deleted Successfully", safe=False)


class ImagenAApiByExpositorGet(APIView):

    def get(self, request, id=0):
        imagen = Imagenes.objects.select_related().filter(expositor=id)
        my_serializer = ImagenesSerializer(imagen, many=True)
        return JsonResponse(my_serializer.data, safe=False)


class ImagenAApiByExpositor(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=0):
        imagen = Imagenes.objects.select_related().filter(expositor=id)
        my_serializer = ImagenesSerializer(imagen, many=True)
        return JsonResponse(my_serializer.data, safe=False)


class DigeekApiGet(APIView):

    def get(self, request):
        digeek = Digeek.objects.all()
        my_serializer = DigeekSerializer(digeek, many=True)
        return JsonResponse(my_serializer.data, safe=False)


class DigeekApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        digeek = Digeek.objects.all()
        my_serializer = DigeekSerializer(digeek, many=True)
        return JsonResponse(my_serializer.data, safe=False)

    def post(self, request):
        my_data = JSONParser().parse(request)
        my_serializer = DigeekSerializer(data=my_data)
        if my_serializer.is_valid():
            my_serializer.save()
            return JsonResponse("Se añadio correctamente", safe=False)
        return JsonResponse("No se pudo añadir", safe=False)

    def put(self, request):
        my_data = JSONParser().parse(request)
        digeek = Digeek.objects.get(digeekid=my_data['digeekid'])
        my_serializer = DigeekSerializer(digeek, data=my_data)
        if my_serializer.is_valid():
            my_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")


class DigeekAApiGet(APIView):

    def get(self, request, id=0):
        digeek = Digeek.objects.get(digeekid=id)
        my_serializer = DigeekSerializer(digeek)
        return JsonResponse(my_serializer.data, safe=False)


class DigeekAApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=0):
        digeek = Digeek.objects.get(digeekid=id)
        my_serializer = DigeekSerializer(digeek)
        return JsonResponse(my_serializer.data, safe=False)

    def delete(self, request, id=0):
        digeek = Digeek.objects.get(digeekid=id)
        digeek.delete()
        return JsonResponse("Deleted Successfully", safe=False)


class EventosApiGet(APIView):

    def get(self, request):
        evento = Eventos.objects.all()
        my_serializer = EventosSerializer(evento, many=True)
        return JsonResponse(my_serializer.data, safe=False)


class EventosApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        evento = Eventos.objects.all()
        my_serializer = EventosSerializer(evento, many=True)
        return JsonResponse(my_serializer.data, safe=False)

    def post(self, request):
        my_data = JSONParser().parse(request)
        my_serializer = EventosSerializer(data=my_data)
        if my_serializer.is_valid():
            my_serializer.save()
            return JsonResponse("Se añadio correctamente", safe=False)
        return JsonResponse("No se pudo añadir", safe=False)

    def put(self, request):
        my_data = JSONParser().parse(request)
        evento = Eventos.objects.get(eventoid=my_data['eventoid'])
        my_serializer = EventosSerializer(evento, data=my_data)
        if my_serializer.is_valid():
            my_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")


class EventosAApiGet(APIView):

    def get(self, request, id=0):
        evento = Eventos.objects.get(eventoid=id)
        my_serializer = EventosSerializer(evento)
        return JsonResponse(my_serializer.data, safe=False)


class EventosAApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=0):
        evento = Eventos.objects.get(eventoid=id)
        my_serializer = EventosSerializer(evento)
        return JsonResponse(my_serializer.data, safe=False)

    def delete(self, request, id=0):
        evento = Eventos.objects.get(eventoid=id)
        evento.delete()
        return JsonResponse("Deleted Successfully", safe=False)


class EventosAApiMasterclassGet(APIView):

    def get(self, request):
        evento = Eventos.objects.filter(tipo="Masterclass")
        my_serializer = EventosSerializer(evento, many=True)
        return JsonResponse(my_serializer.data, safe=False)


class EventosAApiMasterclass(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        evento = Eventos.objects.filter(tipo="Masterclass")
        my_serializer = EventosSerializer(evento, many=True)
        return JsonResponse(my_serializer.data, safe=False)


class ExpositorApiGet(APIView):

    def get(self, request):
        expositor = Expositor.objects.all()
        my_serializer = ExpositorSerializer(expositor, many=True)
        return JsonResponse(my_serializer.data, safe=False)


class ExpositorApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        expositor = Expositor.objects.all()
        my_serializer = ExpositorSerializer(expositor, many=True)
        return JsonResponse(my_serializer.data, safe=False)

    def post(self, request):
        my_data = JSONParser().parse(request)
        my_serializer = ExpositorSerializer(data=my_data)
        if my_serializer.is_valid():
            my_serializer.save()
            return JsonResponse("Se añadio correctamente", safe=False)
        return JsonResponse("No se pudo añadir", safe=False)

    def put(self, request):
        my_data = JSONParser().parse(request)
        expositor = Expositor.objects.get(expositorid=my_data['expositorid'])
        my_serializer = ExpositorSerializer(expositor, data=my_data)
        if my_serializer.is_valid():
            my_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")


class ExpositorAApiGet(APIView):

    def get(self, request, id=0):
        expositor = Expositor.objects.get(expositorid=id)
        my_serializer = ExpositorSerializer(expositor)
        return JsonResponse(my_serializer.data, safe=False)


class ExpositorAApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=0):
        expositor = Expositor.objects.get(expositorid=id)
        my_serializer = ExpositorSerializer(expositor)
        return JsonResponse(my_serializer.data, safe=False)

    def delete(self, request, id=0):
        expositor = Expositor.objects.get(expositorid=id)
        expositor.delete()
        return JsonResponse("Deleted Successfully", safe=False)


class RedesSocialesApiGet(APIView):

    def get(self, request):
        redes_sociales = RedesSociales.objects.all()
        my_serializer = RedesSocialesSerializer(redes_sociales, many=True)
        return JsonResponse(my_serializer.data, safe=False)


class RedesSocialesApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        redes_sociales = RedesSociales.objects.all()
        my_serializer = RedesSocialesSerializer(redes_sociales, many=True)
        return JsonResponse(my_serializer.data, safe=False)

    def post(self, request):
        my_data = JSONParser().parse(request)
        my_serializer = RedesSocialesSerializer(data=my_data)
        if my_serializer.is_valid():
            my_serializer.save()
            return JsonResponse("Se añadio correctamente", safe=False)
        return JsonResponse("No se pudo añadir", safe=False)

    def put(self, request):
        my_data = JSONParser().parse(request)
        redes_sociales = RedesSociales.objects.get(redes_socialesid=my_data['redes_socialesid'])
        my_serializer = RedesSocialesSerializer(redes_sociales, data=my_data)
        if my_serializer.is_valid():
            my_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")


class RedesSocialesAApiGet(APIView):

    def get(self, request, id=0):
        redes_sociales = RedesSociales.objects.get(redes_socialesid=id)
        my_serializer = RedesSocialesSerializer(redes_sociales)
        return JsonResponse(my_serializer.data, safe=False)


class RedesSocialesAApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=0):
        redes_sociales = RedesSociales.objects.get(redes_socialesid=id)
        my_serializer = RedesSocialesSerializer(redes_sociales)
        return JsonResponse(my_serializer.data, safe=False)

    def delete(self, request, id=0):
        redes_sociales = RedesSociales.objects.get(redes_socialesid=id)
        redes_sociales.delete()
        return JsonResponse("Deleted Successfully", safe=False)


class VisitanteApiGet(APIView):

    def get(self, request):
        visitante = Visitante.objects.all()
        my_serializer = VisitanteSerializer(visitante, many=True)
        return JsonResponse(my_serializer.data, safe=False)


class VisitanteApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        visitante = Visitante.objects.all()
        my_serializer = VisitanteSerializer(visitante, many=True)
        return JsonResponse(my_serializer.data, safe=False)

    def post(self, request):
        my_data = JSONParser().parse(request)
        my_serializer = VisitanteSerializer(data=my_data)
        if my_serializer.is_valid():
            my_serializer.save()
            return JsonResponse("Se añadio correctamente", safe=False)
        return JsonResponse("No se pudo añadir", safe=False)

    def put(self, request):
        my_data = JSONParser().parse(request)
        visitante = Visitante.objects.get(visitanteid=my_data['visitanteid'])
        my_serializer = VisitanteSerializer(visitante, data=my_data)
        if my_serializer.is_valid():
            my_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")


class VisitanteAApiGet(APIView):

    def get(self, request, id=0):
        visitante = Visitante.objects.get(visitanteid=id)
        my_serializer = VisitanteSerializer(visitante)
        return JsonResponse(my_serializer.data, safe=False)


class VisitanteAApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=0):
        visitante = Visitante.objects.get(visitanteid=id)
        my_serializer = VisitanteSerializer(visitante)
        return JsonResponse(my_serializer.data, safe=False)

    def delete(self, request, id=0):
        visitante = Visitante.objects.get(visitanteid=id)
        visitante.delete()
        return JsonResponse("Deleted Successfully", safe=False)


class RegistroDigeekApiGet(APIView):

    def get(self, request):
        registro_digeek = RegistroDigeek.objects.all()
        my_serializer = RegistroDigeekSerializer(registro_digeek, many=True)
        return JsonResponse(my_serializer.data, safe=False)


class RegistroDigeekApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        registro_digeek = RegistroDigeek.objects.all()
        my_serializer = RegistroDigeekSerializer(registro_digeek, many=True)
        return JsonResponse(my_serializer.data, safe=False)

    def post(self, request):
        my_data = JSONParser().parse(request)
        my_serializer = RegistroDigeekSerializer(data=my_data)
        if my_serializer.is_valid():
            my_serializer.save()
            return JsonResponse("Se añadio correctamente", safe=False)
        return JsonResponse("No se pudo añadir", safe=False)

    def put(self, request):
        my_data = JSONParser().parse(request)
        registro_digeek = RegistroDigeek.objects.get(visitanteid=my_data['visitanteid'])
        my_serializer = RegistroDigeekSerializer(registro_digeek, data=my_data)
        if my_serializer.is_valid():
            my_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")


class RegistroDigeekAApiGet(APIView):

    def get(self, request, digeekid=0, visitanteid=0):
        registro_digeek = RegistroDigeek.objects.get(digeek=digeekid, visitante=visitanteid)
        my_serializer = RegistroDigeekSerializer(registro_digeek)
        return JsonResponse(my_serializer.data, safe=False)


class RegistroDigeekAApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, digeekid=0, visitanteid=0):
        registro_digeek = RegistroDigeek.objects.get(digeek=digeekid, visitante=visitanteid)
        my_serializer = RegistroDigeekSerializer(registro_digeek)
        return JsonResponse(my_serializer.data, safe=False)

    def delete(self, request, digeekid=0, visitanteid=0):
        registro_digeek = RegistroDigeek.objects.get(digeek=digeekid, visitante=visitanteid)
        registro_digeek.delete()
        return JsonResponse("Deleted Successfully", safe=False)
