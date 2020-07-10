from restapi.views import ObjectViewSet
from rest_framework import routers


## Add New Router Here
router = routers.DefaultRouter()
router.register('object', ObjectViewSet)


# for url in router.urls:
#     print(url, ' \n')