import os
from django.conf import settings

def base_path(*args):
    """Return the absolute path to the Django project's base directory."""
    return os.path.join(settings.BASE_DIR, *args)
  
def modules_path(*args):
  return base_path('modules', *args)