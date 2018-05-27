import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, TextInput
from django.utils.translation import gettext

from arden.models import Upo

PATTERN_OF_MID = re.compile(r'hello')


def isMatchedMid(mid):
    return re.match(PATTERN_OF_MID, mid)


class UpoForm(ModelForm):
    mid = CharField(label='阿婆主编号',
                    label_suffix='*',
                    max_length=20,
                    widget=TextInput)

    # def clean(self):
    #     mid = self.cleaned_data.get('mid')
    #     if isMatchedMid(mid):
    #         raise ValidationError(gettext("不合法的编号"))
    #     return self.cleaned_data

    class Meta:
        model = Upo
        fields = {'mid'}
