from django.db import models

class TimeSlot(models.Model):
    """
    Model representing a time slot with start and stop times.
    
    Attributes:
        start (TimeField): The start time of the time slot.
        stop (TimeField): The stop time of the time slot.
        ids (JSONField): The IDs of the users who have this time slot.
    """
    start = models.TimeField()
    stop = models.TimeField()
    ids = models.JSONField()

class WeeklySchedule(models.Model):
    """
    Model representing the weekly schedule of a user.
    
    Attributes:
        monday (ManyToManyField): Monday time slots.
        tuesday (ManyToManyField): Tuesday time slots.
        wednesday (ManyToManyField): Wednesday time slots.
        thursday (ManyToManyField): Thursday time slots.
        friday (ManyToManyField): Friday time slots.
        saturday (ManyToManyField): Saturday time slots.
        sunday (ManyToManyField): Sunday time slots.
    """
    monday = models.ManyToManyField(TimeSlot, related_name='monday_slots', blank=True)
    tuesday = models.ManyToManyField(TimeSlot, related_name='tuesday_slots', blank=True)
    wednesday = models.ManyToManyField(TimeSlot, related_name='wednesday_slots', blank=True)
    thursday = models.ManyToManyField(TimeSlot, related_name='thursday_slots', blank=True)
    friday = models.ManyToManyField(TimeSlot, related_name='friday_slots', blank=True)
    saturday = models.ManyToManyField(TimeSlot, related_name='saturday_slots', blank=True)
    sunday = models.ManyToManyField(TimeSlot, related_name='sunday_slots', blank=True)
