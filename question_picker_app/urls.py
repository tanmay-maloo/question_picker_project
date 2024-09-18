# urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('change-password/', views.change_password, name='change_password'),
    path('mark-done/<str:question_id>/', views.mark_done, name='mark_done'),
    path('mark-favorite/<str:question_id>/', views.mark_favorite, name='mark_favorite'),
    path('reset-sheet/', views.reset_sheet, name='reset_sheet'),
    path('restore-progress/', views.restore_progress, name='restore_progress'),  # New URL for restoring progress

]