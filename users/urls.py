from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #path('password_reset/', views.password_reset, name='password_reset'),
    #path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    #path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
    path('profile/', views.profile, name='profile'),  # New profile URL pattern
    path('doctor/blog/create/', views.create_blog_post, name='create_blog_post'),
    path('doctor/blog/', views.doctor_blog_list, name='doctor_blog_list'),
    path('patient/blogs/', views.patient_blog_list, name='patient_blog_list'),
    path('patient/blogs/<int:category_id>/', views.patient_blog_list, name='patient_blog_list_by_category'),
    path('logout/', views.logout_view, name='logout'),  # URL for logout
]
