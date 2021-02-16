from django import forms

class ParseForm(forms.Form):
    class Meta:
        fields = [
            'url',
        ]