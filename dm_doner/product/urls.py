from django.urls import path

from .views import ProductAPIListView, ProductAPIDeleteView, ProductAPIDetailView

urlpatterns = [
    path('', ProductAPIListView.as_view()),
    path('<int:pk>/', ProductAPIDetailView.as_view()),
    path('<int:pk>/delete/', ProductAPIDeleteView.as_view()),
]
