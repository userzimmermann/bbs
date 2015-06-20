# -*- coding: utf-8 -*-
from django.db import models
from wbc.process.models import Participation


class BebauungsplanParticipation(Participation):
    statement = models.TextField(verbose_name="Stellungnahme", help_text="Meine Stellungnahme/Kommentare")
    name = models.CharField(max_length=256, verbose_name="Name", help_text="Mein Name")
    address = models.CharField(max_length=256, verbose_name="Adresse", help_text="Meine Adresse")
    areacode = models.CharField(max_length=256, verbose_name="PLZ", help_text="Postleitzahl")
    email = models.EmailField(max_length=70, blank=True, verbose_name="Email", help_text="Email-Adresse")

    def __unicode__(self):
        return self.__class__.__name__

    class Meta:
        verbose_name = "Einwendung Bebauungsplanverfahren"
        verbose_name_plural = "Einwendungen Bebauungsplanverfahren"

