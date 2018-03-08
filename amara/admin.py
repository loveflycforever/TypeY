from django.contrib import admin


# Register your models here.
from amara.models import Collection, Language, Fashion


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'title',
                    'description',
                    'protocol',
                    'language',
                    'extra',
                    'platform',
                    'keeper',
                    'website',
                    'created_at',)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'fashion',
                    'description',
                    'created_at',)
    search_fields = ('name', 'description')


class FashionAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'id',
                    'description',
                    'created_at',)
    search_fields = ('name', 'description')


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Fashion, FashionAdmin)
