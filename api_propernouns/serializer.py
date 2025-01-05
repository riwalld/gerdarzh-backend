
from rest_framework import serializers
from geriadur_api_django.models import Propernoun, LitTrans, WordStem, WordStemPropernoun

class LitTransSerializer(serializers.Serializer):
    litTransFr = serializers.CharField(source="lit_trans_fr")
    litTransEng = serializers.CharField(source="lit_trans_eng",allow_blank=True, required=False)
    litTransType = serializers.IntegerField(source="lit_trans_type")

class PropernounSerializer(serializers.Serializer):
    litTrans = LitTransSerializer(source='lit_trans')  # Nested serializer for the related LitTrans model
    currentName = serializers.CharField(source="current_name")
    etymoName = serializers.CharField(source="etymo_name")
    wordStemsPC = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(queryset=WordStem.objects.all()), 
        write_only=True
    )
    descrFr= serializers.CharField(source="descr_fr", allow_blank=True,required=False)
    descrEng = serializers.CharField(source="descr_eng", allow_blank=True,required=False)
    wordTheme = serializers.IntegerField(source="word_theme")
    culturalArea = serializers.IntegerField(source="cultural_area")
    place = serializers.CharField(allow_blank=True,required=False)
    country = serializers.CharField(allow_blank=True,required=False)
    period = serializers.CharField(allow_blank=True,required=False)
    year = serializers.IntegerField(required=False)
    image = serializers.CharField(allow_blank=True,required=False)
    imgCaption= serializers.CharField(source="img_caption", allow_blank=True,required=False)

    def create(self, validated_data):
        lit_trans_data = validated_data.pop('lit_trans')
        wordstems_data = validated_data.pop('wordStemsPC')
        print(wordstems_data)

        # Create the LitTrans instance
        lit_trans_instance = LitTrans.objects.create(**lit_trans_data)

        # Create the Propernoun instance with the lit_trans instance
        pn = Propernoun.objects.create(lit_trans=lit_trans_instance, **validated_data)
        
        i=0
        for ws in wordstems_data:
            print("Creating WordStemPropernoun with word_stem_id:", ws.pk, "and propernoun_id:", pn.pk, "at the place ", i, "of the name")
            WordStemPropernoun.objects.create(propernoun=pn, word_stem=ws, word_stem_pc_key=i)
            i += 1
            
        return pn

    def update(self, instance, validated_data):
        lit_trans_data = validated_data.pop('lit_trans', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance