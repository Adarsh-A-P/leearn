from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.available_jobs, name='available_jobs'),
    path('buy/', views.buy_products, name='buy_products'),
    path('study-groups/', views.study_groups, name='study_groups'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('profile-setup/', views.profile_setup, name='profile_setup'),
    # Freelancer URLs
    path('freelancers/jobs/', views.available_jobs, name='available_jobs'),
    path('freelancers/profiles/', views.freelancer_profiles, name='freelancer_profiles'),
    
    # Marketplace URLs
    path('marketplace/buy/', views.buy_products, name='buy_products'),
    path('marketplace/sell/', views.sell_products, name='sell_products'),
    path('profile/', views.profile, name='profile'),
    
    # Community URLs
    path('community/groups/', views.study_groups, name='study_groups'),
    path('community/forum/', views.discussion_forum, name='discussion_forum'),
]