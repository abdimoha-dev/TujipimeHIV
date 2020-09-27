from django import forms
GENDER_CHOICES = (('male', 'male'), ('female', 'female'), ('others', 'others'))
TEST_CHOICES = (('positive', 'positive'), ('Negative',
                                           'Negative'), ('Inconclusive', 'inconclusive'))
PICKED_RESULTS = (('Yes', 'Yes'), ('No', 'No'))


class NameForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    gender = forms.CharField(
        label="gender", widget=forms.RadioSelect(choices=GENDER_CHOICES))
    dob = forms.DateField(label="Date of birth")
    date_tested = forms.DateField(label="Date Tested")
    test_result = forms.CharField(
        label="Test Result", widget=forms.RadioSelect(choices=TEST_CHOICES))
    picked_test = forms.CharField(label=" Picked Test results?", widget=forms.RadioSelect(choices=PICKED_RESULTS))
