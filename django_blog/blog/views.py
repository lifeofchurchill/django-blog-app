from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) #User submits the form so it can be validated
        
        if form.is_valid(): #if form is valid create the user
            user = form.save()
            login(request, user) #log the user in
            return redirect('blog:home') #redirect to the homepage
        else:
            form = UserCreationForm() #if a GET request create a blank form
        return render(request, 'blog/register.gtml' {'form': form}) #render template with form
