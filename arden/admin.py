from django.contrib import admin

from arden.models import Upo, Info


class UpoAdmin(admin.ModelAdmin):
    list_display = ('mid',
                    'info',
                    'condition',
                    'instruction',
                    'submitter',
                    'local_updated_at',
                    'local_created_at',)


class InfoAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'status',
                    'data',
                    'local_recorded_at',)


admin.site.register(Upo, UpoAdmin)
admin.site.register(Info, InfoAdmin)
