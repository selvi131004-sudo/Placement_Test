from django.shortcuts import render, redirect
from .models import Student, Question, Result


def home(request):

    return render(request, 'home.html')



def register(request):

    if request.method == 'POST':

        email = request.POST['email']

        if Student.objects.filter(email=email).exists():

            return render(request, 'register.html', {
                'error': 'Email already exists'
            })

        Student.objects.create(

            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            college=request.POST['college'],
            year=request.POST['year'],
            password=request.POST['password']

        )

        return redirect('/login/')

    return render(request, 'register.html')



def login(request):

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        try:

            student = Student.objects.get(
                email=email,
                password=password
            )

            request.session['student_id'] = student.id

            request.session['test_completed'] = False

            return redirect('/dashboard/')

        except:

            return render(request, 'login.html', {
                'error': 'Invalid Login'
            })

    return render(request, 'login.html')



def dashboard(request):

    return render(request, 'dashboard.html')



def test(request, section):

    if request.session.get('test_completed'):

        return redirect('/result/')

    questions = Question.objects.filter(
        section=section
    )

    if request.method == 'POST':

        score = 0

        for question in questions:

            selected = request.POST.get(
                str(question.id)
            )

            if selected == question.answer:

                score += 1

        student = Student.objects.get(
            id=request.session['student_id']
        )

        status = "PASS"

        if score < 85:

            status = "RETRY"

        Result.objects.create(

            student=student,
            section=section,
            score=score,
            status=status

        )

        request.session['score'] = score

        request.session['status'] = status

        request.session['section'] = section

        time_taken = request.POST.get(
            'time_taken'
        )

        request.session['time_taken'] = time_taken

        request.session['test_completed'] = True

        return redirect('/result/')

    return render(request, 'test.html', {

        'questions': questions,

        'section': section

    })



def result(request):

    student = Student.objects.get(
        id=request.session['student_id']
    )

    return render(request, 'result.html', {

        'student': student,

        'score': request.session['score'],

        'status': request.session['status'],

        'section': request.session['section'],

        'time_taken': request.session['time_taken']

    })



def retry_test(request, section):

    request.session['test_completed'] = False

    return redirect(f'/test/{section}/')