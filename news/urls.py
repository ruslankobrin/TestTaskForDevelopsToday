from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

from . import views
# from .views import Like

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet, basename='profile')
router.register(r'comment', views.CommentViewSet, basename='comment')
router.register(r'like', views.LikeViewSet, basename='like')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]