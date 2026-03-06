from rest_framework import serializers
from school.models import Student, Course, Registration
from school.validates import validate_student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'cpf', 'birth_date', 'phone_number']

    def validate(self, data):
        return validate_student(self, data)
    
class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'phone_number']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'code', 'description', 'level']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'student', 'course', 'period']

class ListRegistrationByStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()
    
class ListRegistrationByCourseSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ['student_name', 'period']

    def get_period(self, obj):
        return obj.get_period_display()