from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from .models import Profile  # Add this import

# Your form classes
class BasicUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'date_of_birth', 'password1', 'password2')

class ProfileForm(forms.Form):
    college = forms.CharField(max_length=100)
    course = forms.CharField(max_length=50)
    department = forms.CharField(max_length=50)
    year_of_study = forms.ChoiceField(choices=[
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year'),
    ])
    academic_period = forms.CharField(max_length=9)
    profile_picture = forms.ImageField(help_text='Upload passport size photo (35mm x 45mm, max 2MB)')

# Your view functions
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = BasicUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['temp_user_id'] = user.id
            return redirect('profile_setup')
    else:
        form = BasicUserForm()
    return render(request, 'registration/signup.html', {'form': form})

def profile_setup(request):
    user_id = request.session.get('temp_user_id')
    if not user_id:
        return redirect('signup')
    
    user = User.objects.get(id=user_id)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            Profile.objects.create(
                user=user,
                college=form.cleaned_data['college'],
                course=form.cleaned_data['course'],
                department=form.cleaned_data['department'],
                year_of_study=form.cleaned_data['year_of_study'],
                academic_period=form.cleaned_data['academic_period'],
                profile_picture=form.cleaned_data['profile_picture'],
                cv=request.FILES.get('cv')  # Add this line
            )
            del request.session['temp_user_id']
            messages.success(request, 'Profile completed successfully! Please login.')
            return redirect('login')
    else:
        form = ProfileForm()
    
    return render(request, 'registration/profile_setup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def search(request):
    query = request.GET.get('q', '')
    return render(request, 'search_results.html', {'query': query})

@login_required
def available_jobs(request):
    return render(request, 'freelancers/available_jobs.html')

@login_required
def buy_products(request):
    return render(request, 'marketplace/buy_products.html')

@login_required
def sell_products(request):
    return render(request, 'marketplace/sell_products.html')

@login_required
def study_groups(request):
    return render(request, 'community/study_groups.html')

@login_required
def freelancer_profiles(request):
    return render(request, 'freelancers/freelancer_profiles.html')

@login_required
def discussion_forum(request):
    return render(request, 'community/discussion_forum.html')
