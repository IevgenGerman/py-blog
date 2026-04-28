from django import forms
from .models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        labels = {
            "content": "",
        }
        widgets = {
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Write your comment here...",
                "rows": 3
            }),
        }
