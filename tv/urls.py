# from .views import TvViewSet#ListCreateView, DetailUpdateDeleteView
# from django.urls import path
#
# urlpatterns = [
#     path('list/', TvViewSet.as_view()),
#     # path('detail-update-delete/<int:pk>', DetailUpdateDeleteView.as_view()),
# ]


from rest_framework.routers import DefaultRouter
from .views import TvViewSet

router = DefaultRouter()
router.register(r'tv', TvViewSet, basename='tv')

urlpatterns = router.urls
