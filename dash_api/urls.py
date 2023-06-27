from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('aggregations', views.AggregationViewSet)
router.register('equipments', views.EquipmentViewSet, basename='equipments')

urlpatterns = router.urls
