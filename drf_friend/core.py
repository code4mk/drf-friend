from pathlib import Path
from django.urls import path, include
from .path import modules_path

def bind_modules_app():
    the_modules_path = Path(modules_path()).resolve()
    
    # Initialize an empty list to store installed apps
    INSTALLED_APPS = []

    # Loop through each module directory
    for module_dir in the_modules_path.iterdir():
        if module_dir.is_dir():
            # Construct the path to the urls.py file in the module directory
            module_urls_path = module_dir / 'urls.py'
            
            # Get the name of the module
            module_name = module_dir.name
            
            # Check if the urls.py file exists
            if module_urls_path.exists():
                # Append the module to INSTALLED_APPS
                INSTALLED_APPS.append(f'modules.{module_name}')

    # Return the INSTALLED_APPS list
    return INSTALLED_APPS

def bind_modules_urls():
    the_modules_path = Path(modules_path()).resolve()
    
    # Initialize an empty list to store urlpatterns
    urlpatterns = []

    # Loop through each module directory
    for module_dir in the_modules_path.iterdir():
        if module_dir.is_dir():
            # Get the name of the module
            module_name = module_dir.name
            
            # Construct the path to the urls.py file in the module directory
            module_urls_path = module_dir / 'urls.py'
            
            # Check if the urls.py file exists
            if module_urls_path.exists():
                # Construct the import path for the module's urls
                module_urls = f'modules.{module_name}.urls'
                
                # Append a path to urlpatterns, including the module's urls
                urlpatterns.append(path(f'api/v1/{module_name}/', include((module_urls, module_name))))

    # Return the urlpatterns list
    return urlpatterns
