from django import forms
from .models import Resumemodel

GENDER_CHOICES =[
    ('Male','Male'),
    ('Female','Female')
]

CITY_JOB_CHOICES = [('Lahore','Lahore'),('Faisalabad','Faisalabad'),
('Karachi','Karachi'),('Multan','Multan'),('Islamabad','Islamabad')]

class Resumeform(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job City', choices=CITY_JOB_CHOICES , widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resumemodel
        fields = '__all__'
        labels = {'name':'Full Name','father_name':'Father Name','dob':'Date Of Birth','education':'Education','gender':'Gender','city':'Your City',
        'pin':'Postal Code','locality':'Locality','state':'State','mobile':'Mobile Number','email':'Email Address','job_city':'Prefer Job City'}
        error_messages = {'name':{'required':'please enter name'}, 'father name':{'required':'Please Enter Father Name'},'dob':{'required':'Enter Date of Birth'},'education':{'required':'Please Enter Education'},'mobile':{'required':'Please Enter Mobile Number'}}
        widgets = {'name':forms.TextInput(attrs={'class' : 'form-control','placeholder':'Your Name'}),
        'father_name':forms.TextInput(attrs={'class' : 'form-control','placeholder':'Your Father'}),
        'dob':forms.DateInput(attrs={'class' : 'form-control','id':'datepicker','placeholder':'Your Date Of Birth'}),
        'education':forms.TextInput(attrs={'class' : 'form-control','placeholder':'Your Education'}),
        'city':forms.TextInput(attrs={'class' : 'form-control','placeholder':'Current City'}),
        'pin':forms.NumberInput(attrs={'class' : 'form-control','placeholder':'Enter Postal Code Ex # 32500'}),
        'locality':forms.TextInput(attrs={'class' : 'form-control','placeholder':'Enter Distric'}),
        'state':forms.Select(attrs={'class' : 'form-select'}),
        'mobile':forms.NumberInput(attrs={'class' : 'form-control','placeholder':'Mobile Number With Country Code'}),
        'email':forms.EmailInput(attrs={'class' : 'form-control','placeholder':'For Example # example@gmail.com'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valfname = self.cleaned_data['father_name']
        if len(valname)<5:
            raise forms.ValidationError("Name should be minimum 5 character long")

        if len(valfname)<5:
            raise forms.ValidationError("Father Name should be minimum 5 character long")    