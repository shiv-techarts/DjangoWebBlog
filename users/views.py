from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            form.save()
            return redirect('blog-home')

    else:
        form = UserRegistrationForm()

    return render(request=request, template_name='users/register.html', context={'form': form})

@login_required
def profile(request):
    return render(request=request, template_name='users/profile.html', context={})
