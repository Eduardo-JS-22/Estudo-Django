from django.http import JsonResponse

def students(request):
    if request.method == 'GET':
        students_data = [
            {'id': 1, 'name': 'Alice', 'age': 20},
            {'id': 2, 'name': 'Bob', 'age': 22},
            {'id': 3, 'name': 'Charlie', 'age': 21},
        ]
        return JsonResponse(students_data, safe=False)