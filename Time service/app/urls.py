from django.urls import path
from .views import AddTime, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('add-time/', AddTime.as_view(), name='add_time'),
]
