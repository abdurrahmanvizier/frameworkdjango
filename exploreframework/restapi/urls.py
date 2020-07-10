from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

from scripts.router import router

from rest_framework.authtoken import views as vw_rf

from . import views


urlpatterns = [
    path('api/test/', views.index, name='index'),
    path('api/objectall/', views.ObjectAll.as_view(), name='objectall'),
    path('api/', include(router.urls)),
    path('api-token-auth/', vw_rf.obtain_auth_token, name='api-token-auth')
]