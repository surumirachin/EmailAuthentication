from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from myapp.forms import CustomUserCreationForm
from myapp.forms import PostForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from django.urls import reverse_lazy
from django.views.generic import  CreateView

# Create your views here.
def index(request):

    count = User.objects.count()

    return render(request, "myapp/home.html", {"count": count})

@login_required()
def home(request):
    return render(request,'registration/login.html')

def register_view(request):
    form = CustomUserCreationForm()  
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    # else:
    #     form = CustomUserCreationForm
    return render(request,'registration/register.html',{'form':form})

class RegisterView(CreateView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)

    template_name = "registration/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")

class Post_view(LoginRequiredMixin,View):

    def get(self,request):
        form= PostForm()
        return render(request,'myapp/post.html',{'form':form}) 
        
    def post(self,request):
        form =PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post')
        else:    
          return render(request,'myapp/post.html',{'form':form})


def view_list(request):

    list= Post.objects.all()

    print(list)

    return render(request, "myapp/view_list.html", {"list": list})

   

