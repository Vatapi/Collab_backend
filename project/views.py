from rest_framework.decorators import api_view
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken , ProjectSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets , filters
from .models import Project

@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    print(serializer.data)
    return Response(serializer.data)

class UserList(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user_posted__username' , 'title' , 'skills')
