from django import forms

from minuteman.models import Project

class ProjectForm(forms.Form):
    comments = forms.CharField(required=False)
    project = forms.ModelChoiceField(queryset=Project.objects.none())

    def __init__(self, contractor, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(contractors=contractor)
