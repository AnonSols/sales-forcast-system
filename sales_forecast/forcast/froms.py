from django import forms

class SalesDataUploadForm(forms.Form):
    file = forms.FileField(label="Upload CSV File")
