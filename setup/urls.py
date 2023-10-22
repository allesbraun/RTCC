from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from data.views import CodesViewSet, HomeView, JavaFileViewSet

router = routers.DefaultRouter()
router.register('codes', CodesViewSet, basename='Codes')
router.register('home', HomeView, basename='Home')

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    # path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # path('general-control/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('java_files/<str:filename>/', JavaFileViewSet.as_view(), name='java_files'),
    path('java_files/', JavaFileViewSet.as_view(), name='java_files_list'),
    path('<str:filename>/', JavaFileViewSet.as_view(), name='java_files'),
]
