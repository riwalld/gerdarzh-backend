from django.contrib import admin
from .models import (
    Author,
    Gender,
    LitTrans,
    SemanticField,
    Source,
    WordStem,
    Propernoun,
    Quote,
    SourceAuthor,
    WordStemPropernoun,
    WordStemQuote,
    WordStemSource,
    Language,
    Wordclass,
)


class WordStemPropernounInline(admin.TabularInline):
    model = WordStemPropernoun
    extra = 1


class WordStemAdmin(admin.ModelAdmin):
    list_display = ("word_stem_name", "word_stem_language")
    search_fields = ("word_stem_name",)
    inlines = [WordStemPropernounInline]
    filter_horizontal = ("child_stems",)


admin.site.register(Author)
admin.site.register(LitTrans)
admin.site.register(SemanticField)
admin.site.register(Source)
admin.site.register(WordStem, WordStemAdmin)
admin.site.register(Propernoun)
admin.site.register(Quote)
admin.site.register(Language)
admin.site.register(Wordclass)
admin.site.register(Gender)

admin.site.register(SourceAuthor)
admin.site.register(WordStemPropernoun)
admin.site.register(WordStemQuote)
admin.site.register(WordStemSource)
