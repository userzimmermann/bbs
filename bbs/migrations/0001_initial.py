# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BplanEinwendung',
            fields=[
                ('participation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='participation.Participation')),
                ('statement', models.TextField(help_text=b'Meine Stellungnahme/Kommentare', verbose_name=b'Stellungnahme')),
                ('name', models.CharField(help_text=b'Mein Name', max_length=256, verbose_name=b'Name')),
                ('address', models.CharField(help_text=b'Meine Adresse', max_length=256, verbose_name=b'Stellungnahme')),
                ('areacode', models.CharField(help_text=b'Postleitzahl', max_length=256, verbose_name=b'PLZ')),
                ('email', models.EmailField(help_text=b'Email-Adresse', max_length=70, verbose_name=b'Email', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('participation.participation',),
        ),
    ]
