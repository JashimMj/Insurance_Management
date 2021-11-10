from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name='index'),
    path('maindashboard/', views.maindashboardV,name='maindashboard'),
    path('admindashboard/', views.admindashboardV,name='admindashboard'),
    path('company/and/branch/', views.companyandbranchV,name='companyandbranch'),
    path('company/and/branch/save', views.CompanySaveV,name='companyandbranchsave'),








]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
