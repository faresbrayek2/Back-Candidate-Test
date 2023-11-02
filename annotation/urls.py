from rest_framework.routers import DefaultRouter
from .views import LabelViewSet, DocumentViewSet, AnnotationViewSet

router = DefaultRouter()
router.register(r'labels', LabelViewSet, basename='label')
router.register(r'documents', DocumentViewSet, basename='document')
router.register(r'annotations', AnnotationViewSet, basename='annotation')

urlpatterns = router.urls
