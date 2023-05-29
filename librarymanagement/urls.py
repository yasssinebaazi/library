
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls') ),
    path('', views.home_view),
    path('store', views.store),
    path('login', views.login),
    path('insign/', views.insign, name='insign'),
   


  
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


