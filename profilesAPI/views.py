from rest_framework.views import APIView
from rest_framework.response import Response


class TestApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'similar to Django View',
            'mapped manually to URLs',
        ]

        return Response({'message': 'Hi!', 'an_apiview': an_apiview})
