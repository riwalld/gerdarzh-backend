from rest_framework.response import Response
from geriadur_api_django.models import Propernoun
from rest_framework import viewsets, status
from .serializer import PropernounSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView


class ProperNounsViewSet(viewsets.ModelViewSet):
    serializer_class = PropernounSerializer

    def get_queryset(self):
        propernouns = Propernoun.objects.all().order_by("current_name")
        return propernouns


class GetOneProperNounByNameView(APIView):
    def get(self, request, name):
        print("teststgeggoesgoien")
        propernoun = Propernoun.objects.filter(current_name=name).first()
        if not propernoun:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PropernounSerializer(propernoun)
        return Response(serializer.data)
