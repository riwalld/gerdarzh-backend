# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    author_birthdate = models.DateTimeField(blank=True, null=True)
    author_deathdate = models.DateTimeField(blank=True, null=True)
    author_id = models.BigAutoField(primary_key=True)
    author_name = models.CharField(max_length=255)
    author_nationality = models.CharField(max_length=255)
    biography = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author'


class LitTrans(models.Model):
    lit_trans_type = models.IntegerField()
    lit_trans_id = models.BigAutoField(primary_key=True)
    lit_trans_eng = models.CharField(max_length=255, blank=True, null=True)
    lit_trans_fr = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'lit_trans'
        
class SemanticField(models.Model):
    sem_field_id = models.BigAutoField(primary_key=True)
    sem_field_name_eng = models.CharField(max_length=255)
    sem_field_name_fr = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'semantic_field'      
        
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
        managed = False
        db_table = 'source'
          
class WordStem(models.Model):
    gender = models.IntegerField(blank=True, null=True)
    word_class = models.IntegerField(blank=True, null=True)
    word_stem_language = models.IntegerField()
    word_stem_name = models.CharField(max_length=255)
    first_occurence = models.IntegerField()
    sem_field = models.ForeignKey(SemanticField, models.DO_NOTHING, blank=True, null=True)
    word_stem_id = models.BigAutoField(primary_key=True)
    descr_eng = models.CharField(max_length=255, blank=True, null=True)
    descr_fr = models.CharField(max_length=255, blank=True, null=True)
    phonetic = models.CharField(max_length=255, blank=True, null=True)
    ref_words_eng = models.CharField(max_length=255, blank=True, null=True)
    ref_words_fr = models.CharField(max_length=255)
    source =models.ManyToManyField(Source,through='WordStemSource')
    class Meta:
        managed = False
        db_table = 'word_stem'

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
        managed = False
        db_table = 'propernoun'

class Quote(models.Model):
    quote_id = models.BigAutoField(primary_key=True)
    source = models.ForeignKey('Source', models.DO_NOTHING, blank=True, null=True)
    quote_text = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'quote'





class SourceAuthor(models.Model):
    author = models.OneToOneField(Author, models.DO_NOTHING, primary_key=True)  # The composite primary key (author_id, source_id) found, that is not supported. The first column is selected.
    source = models.ForeignKey(Source, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'source_author'
        unique_together = (('author', 'source'),)


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
        managed = False
        db_table = 'user'

class WordStemParent(models.Model):
    child = models.OneToOneField(WordStem, models.DO_NOTHING, primary_key=True)  # The composite primary key (child_id, parent_id) found, that is not supported. The first column is selected.
    parent = models.ForeignKey(WordStem, models.DO_NOTHING, related_name='wordstemparent_parent_set')

    class Meta:
        managed = False
        db_table = 'word_stem_parent'
        unique_together = (('child', 'parent'),)


class WordStemPropernoun(models.Model):
    word_stem_pc_key = models.IntegerField(primary_key=True)  # The composite primary key (word_stem_pc_key, propernoun_id) found, that is not supported. The first column is selected.
    propernoun = models.ForeignKey(Propernoun, on_delete=models.CASCADE)
    word_stem = models.ForeignKey(WordStem, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'word_stem_propernoun'
        unique_together = (('word_stem_pc_key', 'propernoun_id'),)


class WordStemQuote(models.Model):
    quote = models.OneToOneField(Quote, models.DO_NOTHING, primary_key=True)  # The composite primary key (quote_id, word_stem_id) found, that is not supported. The first column is selected.
    word_stem = models.ForeignKey(WordStem, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'word_stem_quote'
        unique_together = (('quote', 'word_stem'),)


class WordStemSource(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)  # The composite primary key (source_id, word_stem_id) found, that is not supported. The first column is selected.
    word_stem = models.ForeignKey(WordStem, on_delete=models.CASCADE, db_column="word_stem_id")

    class Meta:
        managed = False
        db_table = 'word_stem_source'
        unique_together = (('source', 'word_stem'),)
