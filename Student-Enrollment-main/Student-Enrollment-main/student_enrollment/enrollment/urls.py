from django.urls import path
from .views import student_list, add_student, export_students_csv, ExportStudentsPDF

urlpatterns = [
    path('', student_list, name='student_list'),
    path('add_student/', add_student, name='add_student'),
    path('export/csv/', export_students_csv, name='export_students_csv'),
    path('export/pdf/', ExportStudentsPDF.as_view(), name='export_students_pdf'),
]
