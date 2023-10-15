"""開発環境固有の設定"""

from logging.config import dictConfig

from common.conf import ConfFile
from project.settings.base import *

# クッキーとCSRFの設定
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SECURE = True

# ログ設定
dictConfig(ConfFile.get()["dev"]["logging"])
