#loops through every requirement
from django import forms
from .models import Requirement

class AssessmentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for req in Requirement.objects.all():
            self.fields[f"req_{req.id}"] = forms.ChoiceField(
                label=req.title,
                choices=[('True', '✔️ Yes'), ('False', '❌ No')],
                widget=forms.RadioSelect
            )
