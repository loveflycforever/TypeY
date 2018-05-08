from django.forms import ModelForm, CharField, TextInput

from arden.models import Upo


class UpoForm(ModelForm):
    mid = CharField(label='阿婆主编号',
                    label_suffix='*',
                    max_length=20,
                    widget=TextInput)

    class Meta:
        model = Upo
        fields = {'mid'}
