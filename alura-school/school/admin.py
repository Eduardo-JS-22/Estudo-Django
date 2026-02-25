from django.contrib import admin
from school.models import Student, Course

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'cpf', 'birth_date', 'phone_number')
    list_display_links = ('id', 'name')
    list_per_page = 20
    search_fields = ('name', 'email', 'cpf')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'level')
    list_display_links = ('id', 'code')
    list_per_page = 20
    search_fields = ('code', 'level')

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)