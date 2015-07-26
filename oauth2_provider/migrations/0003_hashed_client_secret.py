# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations
from django.db.migrations.operations.base import Operation

from oauth2_provider.models import Application


class HashAndSaltClientSecret(Operation):

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        pass

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        applications = Application.objects.all()
        for app in applications:
            app.save(force_hash_secret=True)

    def state_forwards(self, app_label, state):
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0002_08_updates'),
    ]

    operations = [
        HashAndSaltClientSecret()
    ]





