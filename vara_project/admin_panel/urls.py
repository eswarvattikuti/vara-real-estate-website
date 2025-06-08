from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # For default LogoutView

urlpatterns = [
    path('login/', views.AdminLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), # Redirect to login after logout
    path('', views.dashboard_overview_view, name='admin_dashboard_overview'),
    path('listings/', views.property_listings_view, name='admin_property_listings'),
    path('inquiries/', views.manage_inquiries_view, name='admin_manage_inquiries'),
    path('listings/add/', views.add_property_view, name='admin_add_property'),
    path('listings/edit/<int:property_id>/', views.edit_property_view, name='admin_edit_property'),
    path('listings/delete/<int:property_id>/', views.delete_property_view, name='admin_delete_property'),
]
