from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', include('books.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
)