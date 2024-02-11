from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from user import views as user_view
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', user_view.index , name = 'index'),
    path("admin/", admin.site.urls),
    path('login/', user_view.Login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'user/index.html'), name = 'logout'),
    path('register/', user_view.register, name = 'register'),
]
