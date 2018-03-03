from django.contrib import admin


# Register your models here.
from amara.models import Collection


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description', 'protocol', 'language', 'platform', 'keeper', 'created_at',)


admin.site.register(Collection, CollectionAdmin)
