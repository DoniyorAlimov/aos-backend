from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('aggregations', views.AggregationViewSet)

urlpatterns = router.urls
