from django.urls import path
from . import views

urlpatterns=[
        
    path('',views.WomenHome.as_view(), name='home'),               # http://127.0.0.1:8000/
    path('about/',views.about, name='about'),         # http://127.0.0.1:8000/about/
    path('addpage/',views.AddPage.as_view(), name='add_page'),   # http://127.0.0.1:8000/addpage/
    path('contact/',views.contact, name='contact'),    # http://127.0.0.1:8000/contact/
    path('login/',views.LoginUser.as_view(), name='login'),           # http://127.0.0.1:8000/login/  
    path('logout/',views.logout_user, name='logout'),           # http://127.0.0.1:8000/logout/ 
    path('register/',views.RegisterUser.as_view(), name='register'),           # http://127.0.0.1:8000/register/  
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),           # http://127.0.0.1:8000/post/2/  
    path('category/<slug:cat_slug>/',views.WomenCategory.as_view(), name='category'),           # http://127.0.0.1:8000/category/2/


]

