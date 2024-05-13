from django.urls import path
from .views import BlogPostListCreate, BlogChanging
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', BlogPostListCreate.as_view(), name='blogpost-view-create'),
    path('blogposts/<int:pk>/', BlogChanging.as_view(), name='update')
]


# router = DefaultRouter()
# router.register(r'blogpost', BlogPostViewSet)
# urlpatterns = router.urls   es roca titleit vakitxav, an modelidan sxva ramit tu momindeba 
