from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Student
from .forms import StudentForm
import csv
from django.http import HttpResponse
from django.views.generic import View
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def student_list(request):
    students = Student.objects.all()
    form = StudentForm()
    return render(request, 'enrollment/student_list.html', {'students': students, 'form': form})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            # Provide error messages if the form is invalid
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def export_students_csv(request):
    students = Student.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Date of Birth'])

    for student in students:
        writer.writerow([student.first_name, student.last_name, student.email, student.date_of_birth])

    return response

class ExportStudentsPDF(View):
    def get(self, request):
        students = Student.objects.all()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="students.pdf"'

        p = canvas.Canvas(response, pagesize=letter)
        width, height = letter

        y = height - 40
        p.drawString(100, y, "First Name")
        p.drawString(200, y, "Last Name")
        p.drawString(300, y, "Email")
        p.drawString(400, y, "Date of Birth")

        y -= 20
        for student in students:
            p.drawString(100, y, student.first_name)
            p.drawString(200, y, student.last_name)
            p.drawString(300, y, student.email)
            p.drawString(400, y, str(student.date_of_birth))
            y -= 20

        p.showPage()
        p.save()

        return response
