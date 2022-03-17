
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


admin.site.site_header = 'My E-coms'
admin.site.index_title = 'dashboard'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('accounts/', include('accounts.urls')),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

