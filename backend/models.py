from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Room(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=200)
    room = models.ForeignKey(Room, related_name='equipment', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} в {self.room.name}'
    
class Booking(models.Model):
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    start_time = models.DateTimeField() # 21 декабря
    end_time = models.DateTimeField() # 18 декабря
    purpose = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.room.name} ({self.start_time} до {self.end_time})'
    
    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError('Время начала должно быть раньше времени окончания')
        
        overlapping_bookings = Booking.objects.filter(
            room=self.room,
            start_time__lt = self.end_time,
            end_time__gt = self.start_time
        )

        if self.pk:
            overlapping_bookings = overlapping_bookings.exclude(pk=self.pk)

        if overlapping_bookings.exists():
            raise ValidationError('Эта комната уже забронирована на выбранное время')
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    

