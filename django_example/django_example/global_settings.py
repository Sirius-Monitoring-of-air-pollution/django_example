from pathlib import Path

from .base_settings import BaseSettings


class GetSettingsMixin:
    def get_settings(self):
        return {k: getattr(self, k) for k in dir(self) if not str(k).startswith('_')}


class GlobalSettings(GetSettingsMixin, BaseSettings):
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

    @property
    def INSTALLED_APPS(self):
        installed_apps = super(GlobalSettings, self).INSTALLED_APPS
        installed_apps += [
            'django_flutter.apps.DjangoFlutterConfig',
            'frontend_example.apps.FrontendExampleConfig',
        ]
        return installed_apps

    FLUTTER_PROJECTS_PATH = Path(BaseSettings.BASE_DIR).parent.joinpath('flutter')
    USE_RELEASE_FLUTTER_APPS_LIST = True
    FLUTTER_APPS = ['frontend_example']
