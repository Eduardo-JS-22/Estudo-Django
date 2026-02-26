from django.contrib import admin
from django.urls import path, include
from school.views import CourseViewSet, StudentViewSet, RegistrationViewSet, ListRegistrationByStudentViewSet, ListRegistrationByCourseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'registrations', RegistrationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:student_id>/registrations/', ListRegistrationByStudentViewSet.as_view(), name='registrations-by-student'),
    path('courses/<int:course_id>/registrations/', ListRegistrationByCourseViewSet.as_view(), name='registrations-by-course'),
]
