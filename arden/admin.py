from django.contrib import admin

from arden.models import Upo, Info


class UpoAdmin(admin.ModelAdmin):
    list_display = ('mid',
                    'info',
                    'condition',
                    'instruction',
                    'local_updated_at',
                    'local_created_at',)


class InfoAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'status',
                    'mid',
                    'name',
                    'sex',
                    'rank',
                    'face',
                    'regtime',
                    'spacesta',
                    'birthday',
                    'sign',
                    'toutu',
                    'toutuId',
                    'theme',
                    'theme_preview',
                    'coins',
                    'im9_sign',
                    'fans_badge',
                    'level_info_current_level',
                    'official_verify_type',
                    'official_verify_desc',
                    'official_verify_suffix',
                    'vip_vipType',
                    'vip_vipStatus',
                    'local_recorded_at',)


admin.site.register(Upo, UpoAdmin)
admin.site.register(Info, InfoAdmin)
