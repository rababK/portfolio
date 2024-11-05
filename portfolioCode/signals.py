from django.core.management import call_command
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import AppConfig

class portfolioCodeConfig(AppConfig):
    name = 'portfolioCode'

    def ready(self):
        post_migrate.connect(load_initial_data, sender=self)

@receiver(post_migrate)
def load_initial_data(sender, **kwargs):
    if sender.name == 'portfolioCode':
        call_command('loaddata', 'initial_data.json')