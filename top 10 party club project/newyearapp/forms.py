from django import forms
from .models import LoginModel,RegisterModel,BookingModel


class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterModel
        fields = "__all__"

        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Enter Username'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter Email'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Enter Password'}) 
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = "__all__"

        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Enter Username'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Enter Password'}) 
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = "__all__"

        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Enter Username'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter Email'}),
            'phone':forms.NumberInput(attrs={'placeholder':'Enter Contact No.'}),
            'person':forms.NumberInput(attrs={'placeholder':'Enter no.of tickets'}),
            'msg':forms.TextInput(attrs={'placeholder':'Enter msg'}),
        }

        