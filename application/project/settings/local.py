"""ローカル環境固有の設定"""

from logging.config import dictConfig

from common.conf import ConfFile
from project.settings.base import *

INSTALLED_APPS += [
    "drf_spectacular",
    "debug_toolbar",
    "django_extensions",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "project.urls.local"

REST_FRAMEWORK.update(
    {"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"}
)

SPECTACULAR_SETTINGS = {
    "TITLE": "プロジェクト名",
    "DESCRIPTION": "プロジェクトの詳細",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

# debug_toolbarが必要としている
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# クッキーとCSRFの設定
SESSION_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SECURE = False

# ログ設定
output_path = Path("output")
if not output_path.exists():
    output_path.mkdir()
dictConfig(ConfFile.get()["local"]["logging"])
