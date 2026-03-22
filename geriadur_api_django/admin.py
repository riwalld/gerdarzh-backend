from django.contrib import admin
from .models import (
    Author,
    Gender,
    LitTrans,
    SemanticField,
    Source,
    WordStem,
    WordstemTranslation,
    Propernoun,
    Quote,
    SourceAuthor,
    WordStemPropernoun,
    WordStemQuote,
    WordStemSource,
    Language,
    Wordclass,
)

admin.site.register(Author)
admin.site.register(LitTrans)
admin.site.register(SemanticField)
admin.site.register(Quote)
admin.site.register(Language)
admin.site.register(Wordclass)
admin.site.register(Gender)
admin.site.register(SourceAuthor)
admin.site.register(WordStemQuote)
admin.site.register(WordStemSource)


class WordStemPropernounInline(admin.TabularInline):
    model = WordStemPropernoun
    extra = 1

class WordStemSourceInline(admin.TabularInline):
    model = WordStemSource
    extra = 1
    
@admin.register(WordStem)
class WordStemAdmin(admin.ModelAdmin):
    inlines = [WordStemSourceInline]
    fields = ('word_stem_name','translations','language','wordclass','w_gender','phonetic','descr_fr','descr_eng','sem_field','first_occurence','child_stems')
    list_display = ("word_stem_name", "translations_join","language","wordclass")
    search_fields = ("word_stem_name", "translations__value")
    inlines = [WordStemPropernounInline]
    filter_horizontal = ("child_stems",)
    def translations_join(self, obj):
        return ", ".join([translation.value for translation in obj.translations.all()])
    translations_join.short_description = "Translations"


@admin.register(WordstemTranslation)
class WordStemAdmin(admin.ModelAdmin):
    list_display = ("language", "value")
    search_fields = ("value",)
    
@admin.register(Propernoun)
class PropernounAdmin(admin.ModelAdmin):
    list_display = ("current_name", "lit_trans", "etymo_name", "country")
    search_fields = ("current_name", "lit_trans", "etymo_name", "country")


@admin.register(WordStemPropernoun)
class WordStemPropernounAdmin(admin.ModelAdmin):
    list_display = ("word_stem", "word_stem_pc_key", "propernoun")
    search_fields = ("word_stem", "word_stem_pc_key", "propernoun")


@admin.register(Source)
class Source(admin.ModelAdmin):
    list_display = ("title", "orig_title")
    search_fields = ("title", "orig_title")
