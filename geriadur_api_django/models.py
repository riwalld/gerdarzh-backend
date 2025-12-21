from django.db import models
from django.contrib.contenttypes.models import ContentType


class Language(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=15)

    def get_name(self, lang_code):
        content_type = ContentType.objects.get_for_model(self.__class__)
        try:
            return Translation.objects.get(
                entity_type=content_type,
                entity_id=self.pk,
                field="name",
                language=lang_code,
            ).value
        except Translation.DoesNotExist:
            return None

    class Meta:
        db_table = "language"

    def __str__(self):
        return self.name


class EntityField(models.Model):
    entity_type = models.ForeignKey(ContentType, models.DO_NOTHING)
    field_name = models.CharField(max_length=50)

    class Meta:
        unique_together = ("entity_type", "field_name")


class Translation(models.Model):
    entity_type = models.ForeignKey(ContentType, models.SET_NULL, null=True)
    entity_id = models.PositiveIntegerField()
    field = models.ForeignKey(EntityField, models.SET_NULL, null=True)
    language = models.ForeignKey(Language, models.PROTECT)
    value = models.TextField()

    class Meta:
        unique_together = ("entity_type", "entity_id", "field", "language")
        indexes = [
            models.Index(fields=["entity_type", "entity_id", "field", "language"]),
        ]

    def __str__(self):
        return f"field '{self.field.field_name}' from the table '{self.entity_type.model}' = {self.value}"


class Country(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    country = models.ForeignKey(Country, models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Period(models.Model):
    country = models.ForeignKey(Country, models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Wordclass(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=15)

    class Meta:
        db_table = "wordclass"

    def __str__(self):
        return self.name


class Gender(models.Model):
    gender = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=15)

    class Meta:
        db_table = "gender"

    def __str__(self):
        return self.gender


class Author(models.Model):
    birthdate = models.DateTimeField(blank=True, null=True)
    deathdate = models.DateTimeField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    biography = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "author"

    def __str__(self):
        return self.author_name


class LitTrans(models.Model):
    type = models.IntegerField()
    id = models.BigAutoField(primary_key=True)
    name_eng = models.CharField(max_length=255, blank=True, null=True)
    name_fr = models.CharField(max_length=255)

    class Meta:
        db_table = "lit_trans"

    def __str__(self):
        return self.name_eng


class SemanticField(models.Model):
    sem_field_id = models.BigAutoField(primary_key=True)
    name_eng = models.CharField(max_length=255)
    name_fr = models.CharField(max_length=255)

    class Meta:
        db_table = "semantic_field"

    def __str__(self):
        return self.name_eng


class Source(models.Model):
    edition_date = models.IntegerField()
    language = models.IntegerField()
    writing_language = models.ForeignKey(
        Language, models.PROTECT, related_name="sources_as_writing"
    )
    studied_language = models.ForeignKey(
        Language, models.PROTECT, related_name="sources_as_studied"
    )
    type = models.IntegerField()
    source_id = models.BigAutoField(primary_key=True)
    abbreviation = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    orig_title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "source"

    def __str__(self):
        return self.title


class WordStem(models.Model):
    word_stem_id = models.BigAutoField(primary_key=True)
    word_stem_name = models.CharField(max_length=255)
    fr_translations = models.ManyToManyField(Translation, related_name="fr_wordstems")
    eng_translations = models.ManyToManyField(Translation, related_name="eng_wordstems")
    gender = models.IntegerField(blank=True, null=True)
    word_class = models.IntegerField(blank=True, null=True)
    word_stem_language = models.IntegerField()
    language = models.ForeignKey(Language, models.PROTECT, blank=True, null=True)
    wordclass = models.ForeignKey(Wordclass, models.PROTECT, blank=True, null=True)
    w_gender = models.ForeignKey(Gender, models.PROTECT, blank=True, null=True)
    first_occurence = models.IntegerField()
    sem_field = models.ForeignKey(SemanticField, models.SET_NULL, blank=True, null=True)
    descr_eng = models.CharField(max_length=255, blank=True, null=True)
    descr_fr = models.CharField(max_length=255, blank=True, null=True)
    phonetic = models.CharField(max_length=255, blank=True, null=True)
    translation = models.CharField(max_length=255, blank=True, null=True)
    ref_words_fr = models.CharField(max_length=255)
    source = models.ManyToManyField(Source, through="WordStemSource")
    child_stems = models.ManyToManyField(
        "self", symmetrical=False, blank=True, related_name="parent_stems_reverse"
    )

    class Meta:
        db_table = "word_stem"

    def __str__(self):
        return self.word_stem_name


class Propernoun(models.Model):
    propernoun_id = models.BigAutoField(primary_key=True)
    lit_trans = models.OneToOneField(LitTrans, models.DO_NOTHING, blank=True, null=True)
    cultural_area = models.BigIntegerField(blank=True, null=True)
    word_theme = models.BigIntegerField(blank=True, null=True)
    current_name = models.CharField(max_length=255)
    etymo_name = models.CharField(max_length=255)
    year = models.IntegerField(blank=True, null=True)
    period = models.CharField(max_length=45, blank=True, null=True)
    place = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    short_descr = models.CharField(max_length=150, blank=True, null=True)
    short_descr_fr = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=3000, blank=True, null=True)
    descr_fr = models.CharField(max_length=3000, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    confirmed = models.IntegerField(blank=True, null=True)
    img_caption = models.CharField(max_length=255)

    class Meta:
        db_table = "propernoun"

    def __str__(self):
        return self.current_name


class Quote(models.Model):
    quote_id = models.BigAutoField(primary_key=True)
    source = models.ForeignKey("Source", models.SET_NULL, blank=True, null=True)
    quote_text = models.CharField(max_length=255)

    class Meta:
        db_table = "quote"


class SourceAuthor(models.Model):
    author = models.OneToOneField(
        Author, models.DO_NOTHING, primary_key=True
    )  # The composite primary key (author_id, source_id) found, that is not supported. The first column is selected.
    source = models.ForeignKey(Source, models.DO_NOTHING)

    class Meta:
        db_table = "source_author"
        unique_together = (("author", "source"),)


class User(models.Model):
    language = models.IntegerField()
    choosen_language = models.ForeignKey(
        Language, models.DO_NOTHING, blank=True, null=True
    )
    score_h_figures = models.IntegerField()
    score_m_figures = models.IntegerField()
    score_objects = models.IntegerField()
    score_places = models.IntegerField()
    score_tribes = models.IntegerField()
    id = models.BigAutoField(primary_key=True)
    registration_date = models.DateTimeField()
    email = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "user"


"""
class WordStemParent(models.Model):
    child = models.OneToOneField(
        WordStem, models.DO_NOTHING, primary_key=True
    )  # The composite primary key (child_id, parent_id) found, that is not supported. The first column is selected.
    parent = models.ForeignKey(
        WordStem, models.DO_NOTHING, related_name="wordstemparent_parent_set"
    )

    class Meta:
        managed = False
        db_table = "word_stem_parent"
        unique_together = (("child", "parent"),)"""


class WordStemPropernoun(models.Model):
    word_stem_pc_key = models.IntegerField(primary_key=True)
    propernoun = models.ForeignKey(Propernoun, on_delete=models.CASCADE)
    word_stem = models.ForeignKey(WordStem, on_delete=models.CASCADE)

    class Meta:
        db_table = "word_stem_propernoun"
        unique_together = (("word_stem_pc_key", "propernoun_id"),)

    def __str__(self):
        return self.word_stem.word_stem_name


class WordStemQuote(models.Model):
    quote = models.OneToOneField(Quote, models.DO_NOTHING, primary_key=True)
    word_stem = models.ForeignKey(WordStem, models.DO_NOTHING)

    class Meta:
        db_table = "word_stem_quote"
        unique_together = (("quote", "word_stem"),)


class WordStemSource(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    word_stem = models.ForeignKey(
        WordStem, on_delete=models.CASCADE, db_column="word_stem_id"
    )

    class Meta:
        db_table = "word_stem_source"
        unique_together = (("source", "word_stem"),)
