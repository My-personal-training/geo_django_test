from django.urls import path
from .views import CategoryList, CategoryDetail

urlpatterns = [
    path('categories/', CategoryList.as_view(), name=CategoryList.name),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name=CategoryDetail.name),
    # path('places/', all_places, name='all_places'),
    # path('places/<int:pk>', place_details, name='place_details'),
]

