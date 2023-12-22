from django.urls import path 
from drf_friend.project.views import ProjectViewset
from drf_friend.router import Router, Route

routes = [
    Router.get('status/', ProjectViewset.get_status),
    Router.get('api/show-routes/', ProjectViewset.get_routes),
    Router.get('api/show-api-logs/', ProjectViewset.get_api_logs),
]

urlpatterns = [eval(route) for route in Route(routes).get_all_routes()]


