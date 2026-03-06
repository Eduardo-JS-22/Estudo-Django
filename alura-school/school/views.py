from school.models import Course, Student, Registration
from school.serializers import CourseSerializer, StudentSerializer, RegistrationSerializer, ListRegistrationByStudentSerializer, ListRegistrationByCourseSerializer, StudentSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['code', 'description', 'level']
    ordering_fields = ['code', 'level']
    search_fields = ['code', 'level']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    #serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['name', 'email', 'cpf', 'birth_date']
    ordering_fields = ['name', 'cpf']
    search_fields = ['name', 'email', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class ListRegistrationByStudentViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['student_id'])
        return queryset
    serializer_class = ListRegistrationByStudentSerializer

class ListRegistrationByCourseViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['course_id'])
        return queryset
    serializer_class = ListRegistrationByCourseSerializer