from django.db import models


class Language(models.Model):
    language = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=15)

    class Meta:
        db_table = "language"

    def __str__(self):
        return self.language


class Wordclass(models.Model):
    wordclass = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=15)

    class Meta:
        db_table = "wordclass"

    def __str__(self):
        return self.wordclass


class Gender(models.Model):
    gender = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=15)

    class Meta:
        db_table = "gender"

    def __str__(self):
        return self.gender


class Author(models.Model):
    author_birthdate = models.DateTimeField(blank=True, null=True)
    author_deathdate = models.DateTimeField(blank=True, null=True)
    author_id = models.BigAutoField(primary_key=True)
    author_name = models.CharField(max_length=255)
    author_nationality = models.CharField(max_length=255)
    biography = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "author"

    def __str__(self):
        return self.author_name


class LitTrans(models.Model):
    lit_trans_type = models.IntegerField()
    lit_trans_id = models.BigAutoField(primary_key=True)
    lit_trans_eng = models.CharField(max_length=255, blank=True, null=True)
    lit_trans_fr = models.CharField(max_length=255)

    class Meta:
        db_table = "lit_trans"

    def __str__(self):
        return self.lit_trans_eng


class SemanticField(models.Model):
    sem_field_id = models.BigAutoField(primary_key=True)
    sem_field_name_eng = models.CharField(max_length=255)
    sem_field_name_fr = models.CharField(max_length=255)

    class Meta:
        db_table = "semantic_field"

    def __str__(self):
        return self.sem_field_name_eng


class Source(models.Model):
    date_publication = models.IntegerField()
    language = models.IntegerField()
    type_source = models.IntegerField()
    source_id = models.BigAutoField(primary_key=True)
    abbreviation = models.CharField(max_length=255)
    source_name_english = models.CharField(max_length=255)
    source_name_original = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "source"

    def __str__(self):
        return self.source_name_english


class WordStem(models.Model):
    gender = models.IntegerField(blank=True, null=True)
    word_class = models.IntegerField(blank=True, null=True)
    word_stem_language = models.IntegerField()
    language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True)
    wordclass = models.ForeignKey(Wordclass, models.DO_NOTHING, blank=True, null=True)
    w_gender = models.ForeignKey(Gender, models.DO_NOTHING, blank=True, null=True)
    word_stem_name = models.CharField(max_length=255)
    first_occurence = models.IntegerField()
    sem_field = models.ForeignKey(
        SemanticField, models.DO_NOTHING, blank=True, null=True
    )
    word_stem_id = models.BigAutoField(primary_key=True)
    descr_eng = models.CharField(max_length=255, blank=True, null=True)
    descr_fr = models.CharField(max_length=255, blank=True, null=True)
    phonetic = models.CharField(max_length=255, blank=True, null=True)
    ref_words_eng = models.CharField(max_length=255, blank=True, null=True)
    ref_words_fr = models.CharField(max_length=255)
    source = models.ManyToManyField(Source, through="WordStemSource")
    child_stems = models.ManyToManyField(
        "self", symmetrical=False, blank=True, related_name="parent_stems_reverse"
    )

    class Meta:
        db_table = "word_stem"

    def __str__(self):
        return f"{self.word_stem_name} ({self.word_stem_language})"


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
    short_descr_eng = models.CharField(max_length=150, blank=True, null=True)
    short_descr_fr = models.CharField(max_length=150, blank=True, null=True)
    descr_eng = models.CharField(max_length=3000, blank=True, null=True)
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
    source = models.ForeignKey("Source", models.DO_NOTHING, blank=True, null=True)
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
    word_stem_pc_key = models.IntegerField(
        primary_key=True
    )  # The composite primary key (word_stem_pc_key, propernoun_id) found, that is not supported. The first column is selected.
    propernoun = models.ForeignKey(Propernoun, on_delete=models.CASCADE)
    word_stem = models.ForeignKey(WordStem, on_delete=models.CASCADE)

    class Meta:
        db_table = "word_stem_propernoun"
        unique_together = (("word_stem_pc_key", "propernoun_id"),)

    def __str__(self):
        return f"{self.word_stem.word_stem_name} on place {self.word_stem_pc_key} for {self.propernoun.current_name}"


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
