from django.db import models

class TimeSlot(models.Model):
    # Start time of the time slot
    start = models.TimeField()

    # End time of the time slot
    stop = models.TimeField()

    # IDs of the users who have this time slot
    ids = models.JSONField()

class WeeklySchedule(models.Model):
    # Monday time slots
    monday = models.ManyToManyField(TimeSlot, related_name='monday_slots', blank=True)

    # Tuesday time slots
    tuesday = models.ManyToManyField(TimeSlot, related_name='tuesday_slots', blank=True)

    # Wednesday time slots
    wednesday = models.ManyToManyField(TimeSlot, related_name='wednesday_slots', blank=True)

    # Thursday time slots
    thursday = models.ManyToManyField(TimeSlot, related_name='thursday_slots', blank=True)

    # Friday time slots
    friday = models.ManyToManyField(TimeSlot, related_name='friday_slots', blank=True)

    # Saturday time slots
    saturday = models.ManyToManyField(TimeSlot, related_name='saturday_slots', blank=True)

    # Sunday time slots
    sunday = models.ManyToManyField(TimeSlot, related_name='sunday_slots', blank=True)
