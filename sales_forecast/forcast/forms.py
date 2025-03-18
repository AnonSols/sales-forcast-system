from django import forms

class SalesDataImportForm(forms.Form):
    file = forms.FileField(label="Upload CSV File")
