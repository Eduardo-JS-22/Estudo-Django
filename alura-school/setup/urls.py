from django.contrib import admin
from django.urls import path, include
from school.views import CourseViewSet, StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
