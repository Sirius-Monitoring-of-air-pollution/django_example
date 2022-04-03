import logging

logger = logging.getLogger(__name__)

try:
    from .local_setting import LocalSetting as Setting
except ImportError:
    from .global_settings import GlobalSettings as Setting

globals().update(Setting().get_settings())
