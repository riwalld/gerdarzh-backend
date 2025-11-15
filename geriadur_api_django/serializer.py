
from rest_framework import serializers
from geriadur_api_django.models import Propernoun, LitTrans, WordStem, WordStemPropernoun
from geriadur_api_django.models import SemanticField, Source, WordStem
from rest_framework import serializers
from geriadur_api_django import constants

class LitTransSerializer(serializers.Serializer):
    litTransFr = serializers.CharField(source="name_fr")
    litTransEng = serializers.CharField(source="name_eng",allow_blank=True, required=False)
    litTransType = serializers.IntegerField(source="type")

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

    
class SemanticFieldSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="sem_field_id",required=False)
    engName = serializers.CharField(source="name_eng")
    frName = serializers.CharField(source="name_fr")
    
    

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ["source_id", "abbreviation", "orig_title"]


class WordStemParentSerializer(serializers.ModelSerializer):
    parent_stems_reverse = serializers.SerializerMethodField()
    name = serializers.CharField(source="word_stem_name")
    word_stem_language = serializers.SerializerMethodField(source="word_stem_language")

    class Meta:
        model = WordStem
        fields = [
            "word_stem_id",
            "name",
            "word_stem_language",
            "ref_words_fr",
            "ref_words_fr",
            "first_occurence",
            "phonetic",
            "parent_stems_reverse",
        ]

    def get_word_stem_language(self, obj):
        return constants.LANGUAGE_CHOICES.get(obj.word_stem_language)

    def get_parent_stems_reverse(self, obj):
        return WordStemParentSerializer(obj.parent_stems_reverse.all(), many=True).data


class WordStemChildSerializer(serializers.ModelSerializer):
    child_stems = serializers.SerializerMethodField()
    name = serializers.CharField(source="word_stem_name")
    word_stem_language = serializers.SerializerMethodField(source="word_stem_language")

    class Meta:
        model = WordStem
        fields = [
            "word_stem_id",
            "name",
            "word_stem_language",
            "ref_words_fr",
            "ref_words_fr",
            "first_occurence",
            "phonetic",
            "child_stems",
        ]

    def get_word_stem_language(self, obj):
        return constants.LANGUAGE_CHOICES.get(obj.word_stem_language)

    def get_child_stems(self, obj):
        return WordStemChildSerializer(obj.child_stems.all(), many=True).data


class WordStemSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="word_stem_id", required=False)
    name = serializers.CharField(source="word_stem_name")
    wordStemLanguage = serializers.SerializerMethodField(source="word_stem_language")
    wordClass = serializers.SerializerMethodField(source="word_class")
    engTranslation = serializers.CharField(source="translation")
    frTranslation = serializers.CharField(source="ref_words_fr")
    semanticField = serializers.PrimaryKeyRelatedField(
        source="sem_field", queryset=SemanticField.objects.all()
    )
    firstOccurrence = serializers.IntegerField(source="first_occurence")
    gender = serializers.SerializerMethodField()
    engDescription = serializers.CharField(
        source="descr_eng", allow_blank=True, required=False
    )
    frDescription = serializers.CharField(
        source="descr_fr", allow_blank=True, required=False
    )
    phonetic = serializers.CharField(allow_blank=True, required=False)
    sources = serializers.PrimaryKeyRelatedField(
        source="source", queryset=Source.objects.all(), many=True
    )
    parents = WordStemParentSerializer(
        source="parent_stems_reverse", many=True, read_only=True
    )
    children = WordStemChildSerializer(source="child_stems", many=True, read_only=True)
    parents_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    )
    children_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    )

    def create(self, validated_data):
        source_ids = validated_data.pop("source", [])
        parent_dicts = validated_data.pop("parents_ids", [])
        children = validated_data.pop("children_ids", [])
        word_stem = WordStem.objects.create(**validated_data)
        word_stem.source.set(source_ids)
        word_stem.child_stems.set(children)
        for parent_id in parent_dicts:
            parent = WordStem.objects.filter(word_stem_id=parent_id).first()
            if parent:
                parent.child_stems.add(word_stem)
        return word_stem

    def get_wordStemLanguage(self, obj):
        return constants.LANGUAGE_CHOICES.get(obj.word_stem_language)

    def get_gender(self, obj):
        return constants.GENDER_CHOICES.get(obj.gender)

    def get_wordClass(self, obj):
        return constants.WORDCLASS_CHOICES.get(obj.word_class)

    def to_internal_value(self, data):
        language_name = data.get("wordStemLanguage")
        gender_name = data.get("gender")
        wordClass_name = data.get("wordClass")

        try:
            data = super().to_internal_value(data)
        except Exception as e:
            print(f"Error during desrialisation: {e}")
            raise

        data["word_stem_language"] = constants.get_keys_by_value(
            constants.LANGUAGE_CHOICES, language_name
        )

        data["gender"] = constants.get_keys_by_value(
            constants.GENDER_CHOICES, gender_name
        )

        data["word_class"] = constants.get_keys_by_value(
            constants.WORDCLASS_CHOICES, wordClass_name
        )
        return data
