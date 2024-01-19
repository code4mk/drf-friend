from drf_friend.initialize.initialize import (
  init_cors_middleware,
  init_all_modules,
  init_module_urls,
)

def init_drf_friend():
  init_cors_middleware()
  init_all_modules()
  init_module_urls()