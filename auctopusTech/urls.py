from django.contrib import admin
from django.urls import include, path

from core.views import index, contact
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', index, name='index'),
    path('', include('core.urls')),

    # path('contact/', contact, name='contact'),
    path('books/', include('books.urls')),

    path('dashboard/', include('dashboard.urls')),

]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)