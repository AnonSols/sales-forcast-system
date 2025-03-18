from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SalesListView, export_sales_csv, import_sales_csv


urlpatterns = [
    path('', SalesListView.as_view(), name='import-sales'),  # Root URL
    path('export/', export_sales_csv, name='export-sales-csv'),
    path('sales/', SalesListView.as_view(), name='sales-list'),  # Sales page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path("import/", import_sales_csv, name="import-sales"),
]