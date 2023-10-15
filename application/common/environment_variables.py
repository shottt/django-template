from pydantic_settings import BaseSettings


class VariableSettings(BaseSettings):
    """環境変数を取得する設定クラス"""

    DEBUG_FLAG: bool = True
    """デバッグモードの切り替え"""
    DJANGO_SECRET_KEY: str = "secretkey"
    """Djangoのシークレットキー"""
    DJANGO_ALLOWED_HOSTS: str = "localhost 127.0.0.1 [::1] back web"
    """リクエストを許可するホスト名"""
    MYSQL_DATABASE: str = "django-db"
    """MYSQLのデータベース名"""
    MYSQL_USER: str = "django"
    """MYSQLのユーザ名"""
    MYSQL_PASSWORD: str = "django"
    """MYSQLのパスワード"""
    MYSQL_HOST: str = "db"
    """MYSQLのホスト名"""
    MYSQL_PORT: int = 3306
    """MYSQLのポート番号"""
    DJANGO_SETTINGS_MODULE: str = "project.settings.local"
    """Djangoアプリケーションの設定モジュールを指定"""
    TRUSTED_ORIGINS: str = "http://localhost"
    """CORSで許可するオリジン"""
    CSRF_COOKIE_DOMAIN: str = ""
    """CSRFCookieを設定するときに使用されるドメイン"""


settings = VariableSettings()
"""Django用の環境変数"""
