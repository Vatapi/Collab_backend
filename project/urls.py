from django.urls import path, include
from .views import current_user, UserList ,ProjectViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('views' ,ProjectViewset)

urlpatterns = [
    path('current_user/' , current_user),
    path('users/' , UserList.as_view()),
]

urlpatterns += router.urls
