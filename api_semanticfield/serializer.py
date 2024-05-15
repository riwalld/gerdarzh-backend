
from rest_framework import serializers

    
class SemantiFieldSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="sem_field_id",required=False)
    engName = serializers.CharField(source="sem_field_name_eng")
    frName = serializers.CharField(source="sem_field_name_fr")