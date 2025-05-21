from .base import *

DEBUG = False
ALLOWED_HOSTS = []


SESSION_COOKIE_SECURE = True          # requiere HTTPS
CSRF_COOKIE_SECURE    = True
SESSION_COOKIE_AGE    = 1800          # 30 min
