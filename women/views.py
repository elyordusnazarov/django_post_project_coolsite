
from django.shortcuts import get_object_or_404, render,redirect
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from .models import Women, Category
from .forms import AddPostForm, LoginUserForm, RegisterUserForm
from django.views.generic import ListView, DetailView, CreateView

from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login





def PageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Page NOt Found</h1>')

class WomenHome(DataMixin, ListView):
    model=Women
    template_name='women/index.html'
    context_object_name='posts'
   
    
    def get_context_data(self, object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title="Главная страница")
       
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


def about(request):
    return render(request, 'women/about.html', {'menu':menu,'title':'about site'})

class AddPage(LoginRequiredMixin,DataMixin,CreateView):
    form_class=AddPostForm
    template_name='women/addpage.html'
    # login_url='/admin/'
    login_url =reverse_lazy('home')
    raise_exception =True

    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)              
        c_def=self.get_user_context(title="Добавление статъи")
        return dict(list(context.items()) + list(c_def.items()))


def contact(request):
     return HttpResponse("Back connection")

# def login(request):
#     return HttpResponse("Authentication")

class ShowPost(DataMixin, DetailView):
    model=Women
    template_name='women/post.html'
    slug_url_kwarg='post_slug'
    context_object_name='post'

    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)       
        c_def=self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))



class WomenCategory(DataMixin, ListView):   
    model=Women
    template_name='women/index.html'
    context_object_name='posts'
    allow_empty=False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self,*, object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        
        c_def=self.get_user_context(title='Категория -' + str(context['posts'][0].cat), cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))
    
class RegisterUser(DataMixin,CreateView):
    form_class= RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)       
        c_def=self.get_user_context(title='Register')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



class LoginUser(DataMixin, LoginView):
    form_class =LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)       
        c_def=self.get_user_context(title='Register')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
    









