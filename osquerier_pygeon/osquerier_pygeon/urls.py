from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('query_hist_manager/', include('query_hist_manager.urls')),
    path('', RedirectView.as_view(url='query_hist_manager/', permanent=True)),
]
