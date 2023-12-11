class Router:
    """A class for generating Django-style path definitions based on HTTP methods.

    Methods:
    - generate(http_method, path, controller):
        Generates a Django path definition string based on the provided HTTP method, path, and controller.

    - get(path, controller):
        Generates a path definition for the 'GET' method.

    - post(path, controller):
        Generates a path definition for the 'POST' method.

    - put(path, controller):
        Generates a path definition for the 'PUT' method.

    - delete(path, controller):
        Generates a path definition for the 'DELETE' method.

    - patch(path, controller):
        Generates a path definition for the 'PATCH' method.
    """

    @classmethod
    def generate(cls, http_method, path, controller):
        """Generate a Django path definition string.

        Args:
        - http_method (str): The HTTP method for the route ('get', 'post', 'put', 'delete', 'patch').
        - path (str): The URL path for the route.
        - controller (callable): The controller function or method.

        Returns:
        str: A Django path definition string.
        """
        class_name = ((controller.__qualname__).split('.'))[0]
        method_name = controller.__name__
        module_name = ((controller.__module__).split('.'))[1]
        path_split = path.split('/')
        path_name = '--'.join(path_split[:-1]) + path_split[-1].rstrip('/')

        data = f"path('{path}', {class_name}.as_view({{'{http_method}': '{method_name}'}}), name='{module_name}_{path_name}')"
        return data

    @classmethod
    def get(cls, path, controller):
        """Generate a path definition for the 'GET' method.

        Args:
        - path (str): The URL path for the route.
        - controller (callable): The controller function or method.

        Returns:
        str: A Django path definition string for the 'GET' method.
        """
        return cls.generate('get', path, controller)

    @classmethod
    def post(cls, path, controller):
        """Generate a path definition for the 'POST' method.

        Args:
        - path (str): The URL path for the route.
        - controller (callable): The controller function or method.

        Returns:
        str: A Django path definition string for the 'POST' method.
        """
        return cls.generate('post', path, controller)

    @classmethod
    def put(cls, path, controller):
        """Generate a path definition for the 'PUT' method.

        Args:
        - path (str): The URL path for the route.
        - controller (callable): The controller function or method.

        Returns:
        str: A Django path definition string for the 'PUT' method.
        """
        return cls.generate('put', path, controller)

    @classmethod
    def delete(cls, path, controller):
        """Generate a path definition for the 'DELETE' method.

        Args:
        - path (str): The URL path for the route.
        - controller (callable): The controller function or method.

        Returns:
        str: A Django path definition string for the 'DELETE' method.
        """
        return cls.generate('delete', path, controller)

    @classmethod
    def patch(cls, path, controller):
        """Generate a path definition for the 'PATCH' method.

        Args:
        - path (str): The URL path for the route.
        - controller (callable): The controller function or method.

        Returns:
        str: A Django path definition string for the 'PATCH' method.
        """
        return cls.generate('patch', path, controller)


class Route:
    """A class representing a collection of routes.

    Args:
    - routes (list): A list of routes.

    Methods:
    - get_all_routes():
        Retrieves all routes in the collection.

    Returns:
    list: A list of routes.
    """

    def __init__(self, routes):
        self.routes = routes

    def get_all_routes(self):
        """Retrieve all routes in the collection.

        Returns:
        list: A list of routes.
        """
        return [route for route in self.routes]
