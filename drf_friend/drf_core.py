from rest_framework.viewsets import ViewSet as View
from rest_framework.response import Response
from .status import Status as MyStatus

class ViewSet(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Response(Response):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class status(MyStatus):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)