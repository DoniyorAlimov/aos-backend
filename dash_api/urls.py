from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('aggregations', views.AggregationViewSet)
router.register('aggregation-types', views.AggregationTypeViewSet)
router.register('equipments', views.EquipmentViewSet, basename='equipments')
router.register('tags', views.SimpleEquipmentViewSet, basename='tags')

urlpatterns = router.urls
