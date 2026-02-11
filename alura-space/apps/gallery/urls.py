from django.urls import path
from apps.gallery.views import index, image, search, new_image, edit_image, delete_image, filter

urlpatterns = [
    path('', index, name='index'),
    path('image/<int:image_id>/', image, name='image'),
    path('search/', search, name='search'),
    path('new-image/', new_image, name='new_image'),
    path('edit-image/<int:image_id>/', edit_image, name='edit_image'),
    path('delete-image/<int:image_id>/', delete_image, name='delete_image'),
    path('filter/<str:category>/', filter, name='filter'),
]