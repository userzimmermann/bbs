# -*- coding: utf-8 -*-
from django.forms import ModelForm

from models import BebauungsplanParticipation


class BebauungsplanParticipationForm(ModelForm):
    class Meta:
        model = BplanEinwendung
        fields = '__all__'
