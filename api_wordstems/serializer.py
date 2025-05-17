from geriadur_api_django.models import SemanticField, Source, WordStem

from rest_framework import serializers
from geriadur_api_django import constants


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ["source_id", "abbreviation", "source_name_original"]


class WordStemSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="word_stem_id", required=False)
    wordStemName = serializers.CharField(source="word_stem_name")
    wordStemLanguage = serializers.SerializerMethodField(source="word_stem_language")
    wordClass = serializers.SerializerMethodField(source="word_class")
    engTranslation = serializers.CharField(source="ref_words_eng")
    frTranslation = serializers.CharField(source="ref_words_fr")
    semanticField = serializers.PrimaryKeyRelatedField(
        source="sem_field", queryset=SemanticField.objects.all()
    )
    firstOccurrence = serializers.IntegerField(source="first_occurence")
    gender = serializers.SerializerMethodField()
    descrEng = serializers.CharField(
        source="descr_eng", allow_blank=True, required=False
    )
    descrFr = serializers.CharField(source="descr_fr", allow_blank=True, required=False)
    phonetic = serializers.CharField(allow_blank=True, required=False)
    sources = serializers.PrimaryKeyRelatedField(
        source="source", queryset=Source.objects.all(), many=True
    )
    parents = serializers.PrimaryKeyRelatedField(
        source="parent_stems", queryset=WordStem.objects.all(), many=True
    )
    children = serializers.PrimaryKeyRelatedField(
        source="child_stems", queryset=WordStem.objects.all(), many=True
    )

    def create(self, validated_data):
        print(validated_data)
        source_ids = validated_data.pop("source")
        word_stem = WordStem.objects.create(**validated_data)
        word_stem.source.set(source_ids)
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
