from django.urls import include, path

from rest_framework  import routers

from .views import *

router = routers.DefaultRouter()

router.register(r'student', studentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]