from drf_friend.drf_core import Response, ViewSet, status
from drf_friend.core import show_modules_url
from drf_friend.raw_query.helpers import (
  fetch_all_to_dictionary,
  raw_query_collection
)
from django.db import connection


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
  
  def get_api_logs(self, request):
      query = 'SELECT * FROM drf_friend_api_logs'
  
      with connection.cursor() as cursor:
          cursor.execute(query)
          results = fetch_all_to_dictionary(cursor)
          output = raw_query_collection(request, results, 'api_logs')
      return Response(output)