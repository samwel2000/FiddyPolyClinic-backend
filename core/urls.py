
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def Home(request):
    return redirect('admin/')
    
urlpatterns = [
    path('', Home),
    path('admin/', admin.site.urls),
    path('api/', include('fpc_api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
