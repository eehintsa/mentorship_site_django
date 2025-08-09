from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import Student

def home(request):
    students = Student.objects.all()[:8]
    return render(request, 'students/home.html', {"students": students})

def student_list(request):
    qs = Student.objects.all()
    paginator = Paginator(qs, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'students/student_list.html', {"page_obj": page_obj})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {"student": student})
