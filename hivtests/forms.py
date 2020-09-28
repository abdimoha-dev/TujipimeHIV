from django import forms
GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))
TEST_CHOICES = (('Positive', 'Positive'), ('Negative',
                                           'Negative'), ('Inconclusive', 'Inconclusive'))
PICKED_RESULTS = (('Yes', 'Yes'), ('No', 'No'))

class DateInput(forms.DateInput):
    input_type = 'date'
class NameForm(forms.Form):
    name = forms.CharField(label='name', max_length=100, widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder': 'Name'}
    ))
    gender = forms.CharField(
        label="gender", widget=forms.RadioSelect(choices=GENDER_CHOICES))
    dob = forms.DateField(label="Date of birth", widget=DateInput)
    date_tested = forms.DateField(label="Date Tested", widget=DateInput)
    test_result = forms.CharField(
        label="Test Result", widget=forms.RadioSelect(choices=TEST_CHOICES))
    picked_test = forms.CharField(label=" Picked Test results?", widget=forms.RadioSelect(choices=PICKED_RESULTS))
