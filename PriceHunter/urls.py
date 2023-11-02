# urls.py
from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', RedirectView.as_view(url='/admin/', permanent=False)),  # Temporary redirect to the admin page
]
