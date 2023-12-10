
from django.urls import path, include

urlpatterns = [
    path('', include('appSite.urls')),
    path('bg/', include('appBlog.urls')),
    path('con/', include('appContact.urls')),
]
