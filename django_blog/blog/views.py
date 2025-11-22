from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) #User submits the form so it can be validated
        
        if form.is_valid(): #if form is valid create the user
            user = form.save()
            login(request, user) #log the user in
            return redirect('blog:home') #redirect to the homepage
    else:
        form = UserCreationForm() #if a GET request create a blank form
    return render(request, 'blog/register.html', {'form': form}) #render template with form

def login(request):
    form = AuthenticationForm(request, data = request.POST) #user submits form which is stored in the data variable
    if form.is_valid:
        username = form.cleaned_data.get('username')   #after validation cleaned_data cleans the data since django never uses raw data from forms 
        password = form.cleaned_data.get('password')   #since django cleans it we are extracting the password it cleaned from the data 
        user = authenticate(username=username, password=password)  #looks at the database to compare the data the user entered
        if user is not None: #if the users data is in the database
            login(request, user) #log the user in and creates a session
            return redirect(home, 'blog:home') # after login redirect them home 
    else: 
        form = AuthenticationForm() #blank form 
        
    return render(request, 'blog/login.html', {'form': form}) #renders this if user isnt logged and has errors and
