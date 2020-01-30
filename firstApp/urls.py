from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from firstApp.views import AuthView,AuthUserView

urlpatterns = [
    path('', views.index, name='index'),
    path('login', AuthView.login, name='login'),
    path('register', AuthView.register, name='register'),
    path('userHome', AuthUserView.userHome, name='userHome'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)