from django.contrib import admin
from django.urls import path, include
from django.contrib.flatpages import views as flatpage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secret/', flatpage_views.flatpage, {'url': '/secret/'}, name='secret'),
    path('', include('my_app.urls')),
    path('<path:url>', flatpage_views.flatpage),
