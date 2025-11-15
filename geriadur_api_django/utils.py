from django.contrib.contenttypes.models import ContentType
from .models import Translation


class TranslationMixin:
    def get_translation(self, field_name, lang_code):
        content_type = ContentType.objects.get_for_model(self.__class__)
        try:
            return Translation.objects.get(
                entity_type=content_type,
                entity_id=self.pk,
                field=field_name,
                language=lang_code,
            ).value
        except Translation.DoesNotExist:
            return None
