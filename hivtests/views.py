from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tests
from .forms import NameForm
from datetime import datetime, date
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import json
import requests

import time


def update_dhis():
    total_number_tested = Tests.objects.filter(
        date_tested=datetime.now()).count()
    # positve  children
    tested_positive_male_child = Tests.objects.filter(
        test_result='Positive', gender='Male', age__lt=15, date_tested=date.today()).count()
    tested_positive_female_child = Tests.objects.filter(
        test_result='Positive', gender='Female', age__lt=15, date_tested=date.today()).count()
    # Negative children
    tested_negative_male_child = Tests.objects.filter(
        test_result='Negative', gender='Male', age__lt=15, date_tested=date.today()).count()
    tested_negative_female_child = Tests.objects.filter(
        test_result='Negative', gender='Female', age__lt=15, date_tested=date.today()).count()

    # positive adults
    tested_positive_male_adult = Tests.objects.filter(
        test_result='Positive', gender='Male', age__gte=15, date_tested=date.today()).count()
    tested_positive_female_adult = Tests.objects.filter(
        test_result='Positive', gender='Female', age__gte=15, date_tested=date.today()).count()
    # negative male adults
    tested_negative_male_adults = Tests.objects.filter(
        test_result='Negative', gender='Male', age__gte=15, date_tested=date.today()).count()
    tested_negative_female_adults = Tests.objects.filter(
        test_result='Negative', gender='Female', age__gte=15, date_tested=date.today()).count()

    ###########total number tested##############
    # children
    total_tested_male_child = Tests.objects.filter(
        gender='Male', age__lt=15, date_tested=date.today()).count()
    total_tested_female_child = Tests.objects.filter(
        gender='Female', age__lt=15, date_tested=date.today()).count()
    # adults
    total_tested_male_adult = Tests.objects.filter(
        gender='Male', age__gte=15, date_tested=date.today()).count()
    total_tested_female_adult = Tests.objects.filter(
        gender='Female', age__gte=15, date_tested=date.today()).count()

    ############# picked results ##################
    picked_results_male_child = Tests.objects.filter(
        picked_test='Yes', gender='Male', age__lt=15, date_tested=date.today()).count()
    picked_results_female_child = Tests.objects.filter(
        picked_test='Yes', gender='Female', age__lt=15, date_tested=date.today()).count()

    picked_results_female_adult = Tests.objects.filter(
        picked_test='Yes', gender='Female', age__gte=15, date_tested=date.today()).count()
    picked_results_male_adult = Tests.objects.filter(
        picked_test='Yes', gender='Male', age__gte=15, date_tested=date.today()).count()

    # print(tested_positive_male_child)
    completdat = date.today().strftime("%Y")+"-"+date.today().strftime("%m") + \
        "-"+date.today().strftime("%d")
    prd = date.today().strftime("%Y")+date.today().strftime("%m") + \
        date.today().strftime("%d")

    data = {}
    datasetID = "LGkEZSNXgPV"
    completeDate = completdat
    period = prd
    orgUnit = "bzOfj0iwfDH"
    attributeOptionCombo = "HllvX50cXC0"

    data["dataSet"] = datasetID
    data["completeDate"] = completeDate
    data["period"] = period
    data["orgUnit"] = orgUnit
    data["attributeOptionCombo"] = attributeOptionCombo
    data["dataValues"] = []

    # total tested
    data["dataValues"].append({
        "dataElement": "VG8mdCWgnW7",
        "categoryOptionCombo": "aC4po8Ig28f",  # female adult
        "value": total_tested_female_adult
    })

    data["dataValues"].append({
        "dataElement": "VG8mdCWgnW7",
        "categoryOptionCombo": "BxHou2UUdVp",  # female child
        "value": total_tested_female_child
    })

    data["dataValues"].append({
        "dataElement": "VG8mdCWgnW7",
        "categoryOptionCombo": "qNdJ7YZNEcL",  # male child
        "value": total_tested_male_child
    })
    data["dataValues"].append({
        "dataElement": "VG8mdCWgnW7",
        "categoryOptionCombo": "jFVb0VKnW2d",  # male adults
        "value": total_tested_male_adult
    })
    # tested positive
    data["dataValues"].append({
        "dataElement": "rMJ9vmLLLAW",
        "categoryOptionCombo": "aC4po8Ig28f",  # female adult
        "value": tested_positive_female_adult
    })

    data["dataValues"].append({
        "dataElement": "rMJ9vmLLLAW",
        "categoryOptionCombo": "BxHou2UUdVp",  # female child
        "value": tested_positive_female_adult
    })
    data["dataValues"].append({
        "dataElement": "rMJ9vmLLLAW",
        "categoryOptionCombo": "qNdJ7YZNEcL",  # male child
        "value": tested_positive_male_child
    })

    data["dataValues"].append({
        "dataElement": "rMJ9vmLLLAW",
        "categoryOptionCombo": "jFVb0VKnW2d",  # male adult
        "value": tested_positive_male_adult
    })
    # tested negative
    data["dataValues"].append({
        "dataElement": "Nqksl9Su4zp",
        "categoryOptionCombo": "aC4po8Ig28f",  # female adult
        "value": tested_negative_female_adults
    })
    data["dataValues"].append({
        "dataElement": "Nqksl9Su4zp",
        "categoryOptionCombo": "BxHou2UUdVp",  # female child
        "value": tested_negative_female_child
    })

    data["dataValues"].append({
        "dataElement": "Nqksl9Su4zp",
        "categoryOptionCombo": "qNdJ7YZNEcL",  # male child
        "value": tested_negative_male_child
    })
    data["dataValues"].append({
        "dataElement": "Nqksl9Su4zp",
        "categoryOptionCombo": "jFVb0VKnW2d",  # male adult
        "value": tested_negative_male_adults
    })
    # picked results
    data["dataValues"].append({
        "dataElement": "lZomvx4sJLP",
        "categoryOptionCombo": "aC4po8Ig28f",  # female adult
        "value": picked_results_female_adult
    })
    data["dataValues"].append({
        "dataElement": "lZomvx4sJLP",
        "categoryOptionCombo": "BxHou2UUdVp",  # female child
        "value": picked_results_female_child
    })
    data["dataValues"].append({
        "dataElement": "lZomvx4sJLP",
        "categoryOptionCombo": "qNdJ7YZNEcL",  # male child
        "value": picked_results_male_child
    })
    data["dataValues"].append({
        "dataElement": "lZomvx4sJLP",
        "categoryOptionCombo": "jFVb0VKnW2d",  # male adult
        "value": picked_results_male_adult
    })

    # json_data = json.dumps(data)
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

    headers = {
        'Content-Type': 'application/json',
    }

    data = open('data.json')
    response = requests.post('http://35.194.15.145:8080/api/dataValueSets',
                             headers=headers, data=data, auth=('Super', 'Abdymohammed@123'))

    print(response.content)


# while 0:
#     schedule.run_pending()
#     time.sleep(1)


def index(request):
    # all_tests = Tests.objects.order_by('date_tested')[:5]
    # context = {'all_tests': all_tests}
    return render(request, "base.html")


@login_required(login_url='/login/')
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
            # calculate age
            today = date.today()
            age = today.year - \
                int(dob[0:4]) - ((today.month, today.day)
                                 < (int(dob[5:7]), int(dob[8:10])))

            details = Tests(name=name, gender=gender, dob=dob, date_tested=date_tested,
                            test_result=test_result, picked_test=picked_test, age=age)
            details.save()
            return render(request, "add_user.html", {'form': form})

    else:
        form = NameForm()
    return render(request, "add_user.html", {'form': form})

@login_required(login_url='/login/')
def get_daily_results(request):
    if request.method == 'GET':
        # total_number_tested(age/male/female)
        # positive_tests
        # negative_tests
        # number_of_picked_results

        total_number_tested = Tests.objects.filter(
            date_tested=datetime.now()).count()
        # positve  children
        tested_positive_male_child = Tests.objects.filter(
            test_result='Positive', gender='Male', age__lt=15, date_tested=date.today()).count()
        tested_positive_female_child = Tests.objects.filter(
            test_result='Positive', gender='Female', age__lt=15, date_tested=date.today()).count()
        # Negative children
        tested_negative_male_child = Tests.objects.filter(
            test_result='Negative', gender='Male', age__lt=15, date_tested=date.today()).count()
        tested_negative_female_child = Tests.objects.filter(
            test_result='Negative', gender='Female', age__lt=15, date_tested=date.today()).count()

        # positive adults
        tested_positive_male_adult = Tests.objects.filter(
            test_result='Positive', gender='Male', age__gte=15, date_tested=date.today()).count()
        tested_positive_female_adult = Tests.objects.filter(
            test_result='Positive', gender='Female', age__gte=15, date_tested=date.today()).count()
        # negative male adults
        tested_negative_male_adults = Tests.objects.filter(
            test_result='Negative', gender='Male', age__gte=15, date_tested=date.today()).count()
        tested_negative_female_adults = Tests.objects.filter(
            test_result='Negative', gender='Female', age__gte=15, date_tested=date.today()).count()

        ###########total number tested##############
        # children
        total_tested_male_child = Tests.objects.filter(
            gender='Male', age__lt=15, date_tested=date.today()).count()
        total_tested_female_child = Tests.objects.filter(
            gender='Female', age__lt=15, date_tested=date.today()).count()
        # adults
        total_tested_male_adult = Tests.objects.filter(
            gender='Male', age__gte=15, date_tested=date.today()).count()
        total_tested_female_adult = Tests.objects.filter(
            gender='Female', age__gte=15, date_tested=date.today()).count()

        ############# picked results ##################
        picked_results_male_child = Tests.objects.filter(
            picked_test='Yes', gender='Male', age__lt=15, date_tested=date.today()).count()
        picked_results_female_child = Tests.objects.filter(
            picked_test='Yes', gender='Female', age__lt=15, date_tested=date.today()).count()

        picked_results_female_adult = Tests.objects.filter(
            picked_test='Yes', gender='Female', age__gte=15, date_tested=date.today()).count()
        picked_results_male_adult = Tests.objects.filter(
            picked_test='Yes', gender='Male', age__gte=15, date_tested=date.today()).count()

        context = {
            'picked_results_male_adult': picked_results_male_adult,
            'picked_results_female_adult': picked_results_female_adult,
            'picked_results_female_child': picked_results_female_child,
            'picked_results_male_child': picked_results_male_child,
            'total_tested_female_adult': total_tested_female_adult,
            'total_tested_male_adult': total_tested_male_adult,
            'total_tested_female_child': total_tested_female_child,
            'total_tested_male_child': total_tested_male_child,
            'tested_positive_male_child': tested_positive_male_child,
            'tested_positive_female_child': tested_positive_female_child,
            'tested_negative_male_child': tested_negative_male_child,
            'tested_negative_female_child': tested_negative_female_child,
            'tested_positive_male_adult': tested_positive_male_adult,
            'tested_positive_female_adult': tested_positive_female_adult,
            'tested_negative_male_adults': tested_negative_male_adults,
            'tested_negative_female_adults': tested_negative_female_adults

        }

    return render(request, 'raw_data.html', context)
