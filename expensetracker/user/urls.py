from django.conf import settings
from .import views
from django.urls import path
from django.conf.urls.static import static



urlpatterns = [
   path('profile',views.profile,name='profile'),
   path('profile_edit',views.profile_edit,name='profile_edit')
]
