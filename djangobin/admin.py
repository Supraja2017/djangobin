from django.contrib import admin
from . import models

# Register your models here.

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'lang_code', 'slug', 'mime', 'created_on')
    search_fields = ['name', 'mime']
    ordering = ['name']
    list_filter = ['created_on']
    date_hierarchy = 'created_on'

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('language', 'title', 'expiration', 'exposure', 'author')
    search_fields = ['title', 'author']
    ordering = ['-created_on']
    list_filter = ['created_on']
    date_hierarchy = 'created_on'
    #filter_horizontal = ('tags',)
    raw_id_fields = ('tags',)
    readonly_fields = ('highlighted_code', 'hits', 'slug', )
    fields = ('title', 'original_code', 'highlighted_code', 'expiration', 'exposure',
          'hits', 'slug', 'language', 'author', 'tags' )
 
 
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)
    #raw_id_fields = ('tags',)
    readonly_fields = ('slug',)

admin.site.register(models.Author)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.Snippet, SnippetAdmin)
admin.site.register(models.Tag, TagAdmin)
