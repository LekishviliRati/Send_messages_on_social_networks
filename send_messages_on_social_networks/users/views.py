from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == "GET":
        form = UserRegisterForm()
        return render(request, 'users/register.html', locals())
    elif request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        return redirect("register")


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Compte créé pour {username}')
#             return redirect('home_page')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})
