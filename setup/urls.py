# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import include, path
# from rest_framework import routers

# from data.views import CodesViewSet

# router = routers.DefaultRouter()
# router.register('codes', CodesViewSet, basename='Codes')
  

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
# #     path('java_files/<str:filename>/', JavaFileViewSet.as_view(), name='java_files'),
# #     path('java_files/', JavaFileViewSet.as_view(), name='java_files_list'),
# #     path('<str:filename>/', JavaFileViewSet.as_view(), name='java_files'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from data.views import CodesAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CodesAPIView.as_view(), name='codes_api'),  # Adicionando a nova rota para a raiz
    # path('codes/', CodesAPIView.as_view(), name='codes_api'),
    # ... outras rotas se houver ...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
