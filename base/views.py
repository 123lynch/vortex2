from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
# from .forms import RegistrationForm

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect('login')
#     else:
#         form = RegistrationForm()
#     return render(request, 'register.html', {'form': form})


class Loginpage(TemplateView):
    template_name = 'account/login.html'

class Registerpage(TemplateView):
    template_name = 'account/register.html'

class Contact(TemplateView):
    template_name = 'account/contact.html'

class About(TemplateView):
    template_name = 'blog/about.html'

