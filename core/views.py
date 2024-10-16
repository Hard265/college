from django.shortcuts import render, redirect
from django.conf import settings
from .models import Result
import csv
import io

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    if request.user.is_superuser:
        return redirect('/admin')

    context = {"profile": request.user.student_profile}

    return render(request, 'index.html', context=context)


def examination_results(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    results = Result.objects.filter(student=request.user)
    return render(request, 'examination-results.html', {"results": results})


import io
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CSVUploadForm
from .models import Result, Student, Subject, Exam

@login_required
@permission_required('core.add_result', raise_exception=True)
def upload_results(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            reader = csv.DictReader(io_string)

            errors = []
            success_count = 0

            for idx, row in enumerate(reader, start=2):  # Start at 2 considering header
                try:
                    # Extract data from each row
                    student_reg = row['registration_number']
                    subject_code = row['subject_code']
                    exam_name = row['exam_name']
                    exam_year = int(row['exam_year'])
                    exam_semester = int(row['exam_semester'])
                    marks_obtained = float(row['marks_obtained'])
                    total_marks = float(row['total_marks'])

                    # Retrieve related objects
                    student = Student.objects.get(registration_number=student_reg)
                    subject = Subject.objects.get(code=subject_code)
                    exam, created = Exam.objects.get_or_create(
                        name=exam_name,
                        year=exam_year,
                        semester=exam_semester
                    )

                    # Create or update the Result
                    result, created = Result.objects.update_or_create(
                        student=student,
                        subject=subject,
                        exam=exam,
                        defaults={
                            'marks_obtained': marks_obtained,
                            'total_marks': total_marks
                        }
                    )
                    success_count += 1

                except Student.DoesNotExist:
                    errors.append(f"Row {idx}: Student with registration number '{student_reg}' does not exist.")
                except Subject.DoesNotExist:
                    errors.append(f"Row {idx}: Subject with code '{subject_code}' does not exist.")
                except ValueError as ve:
                    errors.append(f"Row {idx}: Invalid data type. {ve}")
                except Exception as e:
                    errors.append(f"Row {idx}: Unexpected error. {e}")

            if success_count:
                messages.success(request, f"Successfully uploaded {success_count} results.")
            if errors:
                for error in errors:
                    messages.error(request, error)

            return redirect('upload_results')
    else:
        form = CSVUploadForm()

    return render(request, 'core/upload_results.html', {'form': form})
