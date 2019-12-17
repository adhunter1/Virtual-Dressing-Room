from django.views.generic import TemplateView, View, ListView
from django.forms.models import model_to_dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

#from services import ServiceView
#from shop.models import Order
from .forms import UserSignupForm, InputBodyForm
from .models import Dresses
# Create your views here.
class HomePage(ListView):
    """Homepage template view."""
    model = Dresses
    template_name = "homepage/index.html"
    form= InputBodyForm
    #def get(self, request):
     #   """Serve the form page."""
    #    return render(request, self.template_name, {"form": self.form})

class ProfilePage(TemplateView):
    """Profile template view."""

    template_name = "registration/profile.html"
    
    def logout_request(request):
        logout(request)
        messages.info(request, "Logged out successfully!")
        return redirect("/")

class SignupPage(View):
    """Signup view."""

    template_name = "registration/signup.html"
    form = UserSignupForm

    def get(self, request):
        """Serve the form page."""
        return render(request, self.template_name, {"form": self.form})

    def post(self, request):
        """Handle submissions."""
        form = self.form(request.POST)
        if form.is_valid():
            user = form.signup_user()
            login(request, user)
            return redirect("/accounts/profile/")
        return render(request, self.template_name, {"form": form})  
