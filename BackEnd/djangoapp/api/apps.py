from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ApiConfig(AppConfig):
    name = 'djangoapp.api'
    verbose_name = _('api')

    def ready(self):
       import djangoapp.api.signals
