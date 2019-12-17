
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import (
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
    AuthenticationForm,
    UsernameField,
)
from django.contrib.auth.password_validation import validate_password
from django import forms
from django.core import validators
from .models import Profile
class InputBodyForm(forms.ModelForm):
    """Body measurements form."""
    shoulders = forms.IntegerField(
        label="Shoulders"
    )
    bust = forms.IntegerField(
        label="Bust"
    )
    waist = forms.IntegerField(
        label="Waist"
    )

    hips = forms.IntegerField(
        label="Hips"
    )
    height = forms.IntegerField(
        label="Height"
    )

    class Meta:
        model = Profile
        fields= ('shoulders','bust','waist','hips', 'height',)

    """validate the numbers"""
    """def clean_shoulders(self):
        data=self.cleaned_data['shoulders']
        if data<20:
            raise ValidationError('Too low')
        if data>60:
            raise ValidationError('Too high')
        return data
    def clean_bust(self):
        data=self.cleaned_data['bust']
        if data<20:
            raise ValidationError('Too low')
        if data>60:
            raise ValidationError('Too high')
        return data
    def clean_waist(self):
        data=self.cleaned_data['waist']
        if data<10:
            raise ValidationError('Too low')
        if data>50:
            raise ValidationError('Too high')
        return data
    def clean_hips(self):
        data=self.cleaned_data['hips']
        if data<20:
            raise ValidationError('Too low')
        if data>60:
            raise ValidationError('Too high')
        return data
"""
class UserSignupForm(forms.Form):
    """User signup form."""

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Your Email Address"})
    )
    password1 = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={"placeholder": "Make it a good one."}),
        label="Create A Password",
    )
    password2 = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={"placeholder": "Just double checking!"}),
        label="Confirm Your Password",
    )

    def clean(self):
        form_data = super().clean()
        user_model = get_user_model()
        qs = user_model.objects.filter(email=form_data.get("email"))
        if qs:
            raise forms.ValidationError("That email already has an account!")
        if not form_data["password1"] == form_data["password2"]:
            raise forms.ValidationError("Passwords do not match!")
        validate_password(form_data["password1"])
        return form_data

    def signup_user(self):
        """Create a user from the form data."""
        user_model = get_user_model()
        new_user = user_model.objects.create_user(
            username=self.cleaned_data["email"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password1"],
        )
        return new_user

class CustomLoginForm(AuthenticationForm):
    """Custom login form."""

    username = UsernameField(
        label="Email Address",
        widget=forms.TextInput(
            attrs={
                "autocomplete": "username",
                "autofocus": True,
                "placeholder": "Your email address.",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "placeholder": "Your password."}
        ),
    )


