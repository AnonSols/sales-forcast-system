from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SalesListView

urlpatterns = [
    path('', SalesListView.as_view(), name='sales-list'),  # Root URL
    path('sales/', SalesListView.as_view(), name='sales-list'),  # Sales page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]