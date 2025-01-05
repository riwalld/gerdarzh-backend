
from rest_framework.response import Response
from geriadur_api_django.models import Propernoun
from rest_framework import viewsets,status
from .serializer import PropernounSerializer
from rest_framework.decorators import action

class ProperNounsViewSet(viewsets.ModelViewSet):
    serializer_class = PropernounSerializer
    
    def get_queryset(self):
        propernouns = Propernoun.objects.all()
        return propernouns
    
    @action(detail=False, methods=['get'], url_path='propernoun')
    def get_one(self, request):
        propernoun = Propernoun.objects.filter(current_name=request.query_params.get("current_name", None)).first()
        serializer = self.get_serializer(propernoun)
        return Response(serializer.data, status=status.HTTP_200_OK)