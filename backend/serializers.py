from rest_framework import serializers
from .models import Room, Equipment, Booking

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name']

class RoomSerializer(serializers.ModelSerializer):
    equipment = EquipmentSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['id', 'name', 'capacity', 'location', 'equipment']

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Booking
        fields = ['id', 'room', 'user', 'start_time', 'end_time', 'purpose']

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError('Время начала должно быть раньше времени окончания')
        
        room = data['room']
        start_time = data['start_time']
        end_time = data['end_time']

        overlapping_bookings = Booking.objects.filter(
            room = room,
            start_time__lt = end_time,
            end_time__gt = start_time
        )

        if self.isinstance:
            overlapping_bookings = overlapping_bookings.exclude(pk=self.instance.pk)

        if overlapping_bookings.exists():
            raise serializers.ValidationError('Эта комната уже забронирована на выбранный период')
        
        return data