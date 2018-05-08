from django.contrib import admin

from arden.models import Upo


class UpoAdmin(admin.ModelAdmin):
    list_display = ('mid',
                    'info',
                    'submitter',
                    'deleted',
                    'local_updated_at',
                    'local_created_at',)


admin.site.register(Upo, UpoAdmin)
