from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Quiz, Result
from .forms import SignupForm, LoginForm
import datetime as dt

question_list = []
score = 0
question_number = 1
start_time = 0
end_time = 0
username = 0
date = dt.datetime.today()
today = date.date()


def home(request):
    return render(request, 'home.html')


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully !')
            form.save()
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    global username
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                username = user
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def dashboard(request):
    return render(request, 'dashboard.html')


def get_question(request, sub):
    global question_list, start_time
    if request.method == 'POST':
        if start_time == 0:
            start_time = dt.datetime.now()
        questions = Quiz.objects.filter(subject=sub)
        question_list = list(questions)
    return render(request, 'questions.html', {'questions': question_list[0], 'qn': question_number})


def check_answer(request):
    global end_time, score, question_list
    finish = False
    if request.method == 'POST':
        q = question_list[0]
        selected = request.POST['option']
        if selected.lower() == q.answer.lower():
            answer = True
            score += 1
        else:
            answer = False
        if len(question_list) == 1:
            finish = True
            end_time = dt.datetime.now()
        return render(request, 'questions.html', {'answer': answer, 'questions': q, 'finish': finish,
                                                  'qn': question_number, 'correct_answer': q.answer})


def next_question(request):
    global question_number, question_list
    if request.method == 'GET':
        question_number += 1
        if len(question_list) > 1:
            question_list.pop(0)
    return render(request, 'questions.html', {'questions': question_list[0], 'qn': question_number})


def result(request):
    time = end_time - start_time
    total_time = str(time).split(':')
    minutes = int(total_time[1])
    seconds = format(float(total_time[2]), '.0f')
    stu_result = Result(student=username, subject=question_list[0].subject, marks=score, date=today,
                        time=end_time.time())
    stu_result.save()
    return render(request, 'result.html', {'total': score, 'minutes': minutes, 'seconds': seconds})


def user_logout(request):
    global question_list, score, question_number, start_time, end_time, date, today
    score = end_time = start_time = date = today = 0
    question_list = []
    question_number = 1
    logout(request)
    return redirect('home')
