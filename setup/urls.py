from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from data.views import CodesViewSet

# , JavaFileViewSet

router = routers.DefaultRouter()
router.register('codes', CodesViewSet, basename='Codes')
  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
#     path('java_files/<str:filename>/', JavaFileViewSet.as_view(), name='java_files'),
#     path('java_files/', JavaFileViewSet.as_view(), name='java_files_list'),
#     path('<str:filename>/', JavaFileViewSet.as_view(), name='java_files'),
]
