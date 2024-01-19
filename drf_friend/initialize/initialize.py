from django.conf import settings
from drf_friend.core import bind_modules_app

def init_cors_middleware():
    cors_middleware_class = 'drf_friend.cors.middleware.CorsMiddleware'
    settings.MIDDLEWARE.insert(0, cors_middleware_class)
    
def init_all_modules():
  settings.INSTALLED_APPS.extend(bind_modules_app())