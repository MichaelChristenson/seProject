from django import forms

from .choices import MONTHS, YEARS
from .models import Awards, Education, Experience, Resume, Skills


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = '__all__'
        exclude = ('resume',)

    def clean(self):
        super().clean()
        school = self.cleaned_data['school']
        degree = self.cleaned_data['degree']
        if school == '' and degree != '':
            raise forms.ValidationError('Please fill out degree.')
        return self.cleaned_data


EducationFormset = forms.inlineformset_factory(
    Resume,
    Education,
    form=EducationForm,
    exclude=('resume',),
    extra=0,
    min_num=1,
    max_num=5,
    widgets={
        'school': forms.TextInput(attrs={'placeholder': 'School'}),
        'graduation_year': forms.Select(choices=YEARS),
        'degree': forms.TextInput(attrs={'placeholder': 'Degree Earned'})
    }
)

ExperienceFormset = forms.inlineformset_factory(
    Resume,
    Experience,
    exclude=('resume',),
    extra=0,
    min_num=1,
    max_num=10,
    widgets={
        'company': forms.TextInput(attrs={'placeholder': 'Company'}),
        'title': forms.TextInput(attrs={'placeholder': 'Job Title'}),
        'start_month': forms.Select(choices=MONTHS),
        'start_year': forms.Select(choices=YEARS),
        'end_month': forms.Select(choices=MONTHS),
        'end_year': forms.Select(choices=YEARS)
    }
)

SkillsFormset = forms.inlineformset_factory(
    Resume,
    Skills,
    exclude=('resume',),
    extra=0,
    min_num=1,
    max_num=20,
    widgets={
        'skill': forms.TextInput(attrs={'placeholder': 'Skill Name'})
    }
)

AwardsFormset = forms.inlineformset_factory(
    Resume,
    Awards,
    exclude=('resume',),
    extra=0,
    min_num=1,
    max_num=10,
    widgets={
        'award': forms.TextInput(attrs={'placeholder': 'Award'}),
        'year': forms.Select(choices=YEARS)
    }
)
