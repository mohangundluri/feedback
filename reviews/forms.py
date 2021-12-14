from django import forms


class MyForm(forms.Form):
    user_name = forms.CharField(max_length=100, required=True, label="Your Name",error_messages={
        'required':'Your name is required',
        'max_length':"Your Name should be less than 100 alphabets"
    },)