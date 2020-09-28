from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tests
from .forms import NameForm
from datetime import datetime
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as django_logout


def login(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    user =authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('add')
        
    else:
        return HttpResponse('/you are not logged in/')
            



def logout(request):
    django_logout(request)
    return HttpResponse('/you have logged out')
def index(request):
    # all_tests = Tests.objects.order_by('date_tested')[:5]
    # context = {'all_tests': all_tests}
    return render(request, "base.html")

@login_required
def add_test(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            gender = request.POST.get('gender')
            dob = request.POST.get('dob')
            date_tested = request.POST.get('date_tested')
            test_result = request.POST.get('test_result')
            picked_test = request.POST.get('picked_test')
            # age automatically complete

            details = Tests(name=name, gender=gender, dob=dob, date_tested=date_tested,
                            test_result=test_result, picked_test=picked_test)
            details.save()
            return HttpResponse('/thanks/')

    else:
        form = NameForm()
    return render(request, "add_user.html", {'form': form})


def get_daily_results(request):
    if request.method == 'GET':
        # total_number_tested(age/male/female)
        # positive_tests
        # negative_tests
        # number_of_picked_results

        total_number_tested = Tests.objects.filter(date_tested=datetime.now()).count()
        positive_tests = Tests.objects.filter(test_result='positive').count()
        negative_tests = Tests.objects.filter(test_result='Negative').count()
        number_of_picked_results = Tests.objects.filter(
            picked_test='Yes').count()

        print(number_of_picked_results)
    return HttpResponse('/thanks/')
