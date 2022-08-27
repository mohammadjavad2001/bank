from site1.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Customer',CustomerViewset)
router.register('Account',AccountViewset)

