from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ test api view"""

    def get(self , request , format=None):
        """return a list of APIView features"""
        an_apiview= [
            'Uses http method as function (get , post , put , patch , delete)',
            'Is similar tp a traditional Django view',
            'good controls',
            'is mapped manually to URLs',
        ]

        return Response({'message' : 'Hello' , 'an_apiview' : an_apiview} )
    
    

class HelloApiView2(APIView):
    """ test api view"""

    def get(self , request , format=None):
        """return a list of APIView features"""
        an_apiview= [            
            'good controls',
            'is mapped manually to URLs',
        ]

        return Response({'message' : 'Hello' , 'an_apiview' : an_apiview} )



