from django.contrib import admin
from django.urls import path
from chem_app import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Change 'view' to 'urls'
    path('', views.home, name='home'),
    path('chembl/', views.chembl, name='chembl'),
    path('povray/', views.povray, name='povray'),
]
