from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .serializers import BlogSerializer
from api.blogs.serializers import BlogSerializer  # Corrected import statement


@api_view(['GET', 'POST'])
def blogdeco(request):
    
    if request.method == 'GET':
        return Response( {
            "success": True,
            "message": "This is a GET request",
            "data": " "
        })
    if request.method == "POST":
        print("############", request.data)
        return Response( {
            "success": True,
            "message": "This is a POST request",
            "data": ""
        })
    return Response( { "success": True,
                        "message": "request is failed",
                       "data": ""
                       })

                        



