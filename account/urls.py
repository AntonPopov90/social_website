from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, \
    PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('', views.home_page, name='dashboard'),
    path('all_users/', views.user_list, name='all_users'),
    path('users/<username>', views.user_detail, name='user_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>[-\w]+)/<token>[-\w]+)/$', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('news/', views.news, name='news'),
    path('add_trophy/', views.add_trophy, name='add_trophy'),
    path('statistic/', views.statistic, name='statistic'),
    path('add-statistic/', views.add_statistic, name='add-statistic'),
    path('show-statistic/', views.show_statistic, name='show-statistic'),
    path('trophy_gallery/', views.trophy_gallery, name='trophy_gallery'),
]
#(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)