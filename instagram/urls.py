from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet) # 2개 URL을 만들어 준다.
# router.urls # url pattern list

app_name = 'instagram'
urlpatterns = [
    path('public/', views.PublicPostListAPIView.as_view()),
    path('', include(router.urls)),
]