from django.urls import path, include
from .views import ClientViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', ClientViewSet)


urlpatterns = [
    path('', include(router.urls))
    # path('', ClientViewSet.as_view({'get': 'list'})),
    # path('<int:pk>/', ClientViewSet.as_view({'put': 'update'}))
]
