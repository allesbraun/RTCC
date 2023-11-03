
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from data.views import RunningTimeComplexityCalculatorAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RunningTimeComplexityCalculatorAPIView.as_view(), name='Running Time Complexity Calculator'),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
