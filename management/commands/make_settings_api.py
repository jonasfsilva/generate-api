import os
import json
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Command to get all apps, models and fields in project'

    def get_current_file_path(self):
        return os.path.dirname(os.path.realpath(__file__))

    def get_all_model_instances(self):
        from django.apps import apps
        all_models = apps.get_models()

        data = {}
        for model in all_models:
            data.update({
                model._meta.app_label:{
                    model._meta.object_name:[ field.name for field in model._meta.fields]
                    }
                })
        with open(self.get_current_file_path(), 'w') as outfile:
            json.dump(data, outfile)

    def handle(self, *args, **options):
        self.get_all_model_instances()
        