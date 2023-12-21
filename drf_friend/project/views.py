from drf_friend.drf_core import Response, ViewSet, status
from drf_friend.core import show_modules_url

class ProjectViewset(ViewSet):
  
  def get_status(self, request):
    data = {
      'status': "drf-friend is working fine"
    }
    return Response(data, status=status.HTTP_200_OK)
  
  def get_routes(self, request):
    data = {
      'routes': show_modules_url()
    }
    
    return Response(data, status=status.HTTP_200_OK)