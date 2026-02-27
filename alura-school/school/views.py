from school.models import Course, Student, Registration
from school.serializers import CourseSerializer, StudentSerializer, RegistrationSerializer, ListRegistrationByStudentSerializer, ListRegistrationByCourseSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class CourseViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class ListRegistrationByStudentViewSet(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['student_id'])
        return queryset
    serializer_class = ListRegistrationByStudentSerializer

class ListRegistrationByCourseViewSet(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['course_id'])
        return queryset
    serializer_class = ListRegistrationByCourseSerializer