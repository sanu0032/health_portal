from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,BlogPostForm
from .models import Profile,BlogPost, Category
from django.contrib.auth import logout
from django.shortcuts import redirect

def home(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = Profile(
                user=user,
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                profile_picture=form.cleaned_data.get('profile_picture'),
                address_line1=form.cleaned_data.get('address_line1'),
                city=form.cleaned_data.get('city'),
                state=form.cleaned_data.get('state'),
                pincode=form.cleaned_data.get('pincode'),
                user_type=form.cleaned_data.get('user_type'),
            )
            profile.save()
            messages.success(request, f'Account created for {user.username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def dashboard(request):
    profile = request.user.profile
    context = {
        'profile': profile,
    }
    return render(request, 'users/dashboard.html', context)

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return self.request.GET.get('next', '/dashboard/')

@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # Handle this case in your template

    return render(request, 'users/profile.html', {'profile': profile})

def index(request):
    return render(request, 'users/index.html')



@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('doctor_blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'users/create_blog_post.html', {'form': form})

@login_required
def doctor_blog_list(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'users/doctor_blog_list.html', {'posts': posts})

def patient_blog_list(request, category_id=None):
    if category_id:
        posts = BlogPost.objects.filter(draft=False, category_id=category_id)
    else:
        posts = BlogPost.objects.filter(draft=False)
    
    for post in posts:
        words = post.summary.split()
        if len(words) > 15:
            post.summary = ' '.join(words[:15]) + '...'

    categories = Category.objects.all()
    return render(request, 'users/patient_blog_list.html', {'posts': posts, 'categories': categories})

# views.py


@login_required
def logout_view(request):
    logout(request)
    return redirect('home') 