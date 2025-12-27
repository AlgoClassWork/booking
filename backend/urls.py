from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, EquipmentViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls))
]