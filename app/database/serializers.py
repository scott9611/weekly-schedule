from rest_framework import serializers
from .models import TimeSlot, WeeklySchedule

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'

class WeeklyScheduleSerializer(serializers.ModelSerializer):
    monday = TimeSlotSerializer(many=True)
    tuesday = TimeSlotSerializer(many=True)
    wednesday = TimeSlotSerializer(many=True)
    thursday = TimeSlotSerializer(many=True)
    friday = TimeSlotSerializer(many=True)
    saturday = TimeSlotSerializer(many=True)
    sunday = TimeSlotSerializer(many=True)

    class Meta:
        model = WeeklySchedule
        fields = '__all__'

    def create(self, validated_data):
        """
        Create a new WeeklySchedule instance with associated TimeSlots for each day.

        Args:
            validated_data (dict): The validated data containing TimeSlot information for each day.

        Returns:
            WeeklySchedule: The newly created WeeklySchedule instance with associated TimeSlots.
        """
        monday_data = validated_data.pop('monday')
        tuesday_data = validated_data.pop('tuesday')
        wednesday_data = validated_data.pop('wednesday')
        thursday_data = validated_data.pop('thursday')
        friday_data = validated_data.pop('friday')
        saturday_data = validated_data.pop('saturday')
        sunday_data = validated_data.pop('sunday')

        # Create the WeeklySchedule object
        weekly_schedule = WeeklySchedule.objects.create(**validated_data)

        # Create and add TimeSlots for each day
        for time_slot_data in monday_data:
            time_slot = TimeSlot.objects.create(**time_slot_data)
            weekly_schedule.monday.add(time_slot)

        for time_slot_data in tuesday_data:
            time_slot = TimeSlot.objects.create(**time_slot_data)
            weekly_schedule.tuesday.add(time_slot)

        for time_slot_data in wednesday_data:
            time_slot = TimeSlot.objects.create(**time_slot_data)
            weekly_schedule.wednesday.add(time_slot)

        for time_slot_data in thursday_data:
            time_slot = TimeSlot.objects.create(**time_slot_data)
            weekly_schedule.thursday.add(time_slot)

        for time_slot_data in friday_data:
            time_slot = TimeSlot.objects.create(**time_slot_data)
            weekly_schedule.friday.add(time_slot)

        for time_slot_data in saturday_data:
            time_slot = TimeSlot.objects.create(**time_slot_data)
            weekly_schedule.saturday.add(time_slot)

        for time_slot_data in sunday_data:
            time_slot = TimeSlot.objects.create(**time_slot_data)
            weekly_schedule.sunday.add(time_slot)

        return weekly_schedule

    def update(self, instance, validated_data):
        """
        Update an existing WeeklySchedule instance and its associated TimeSlots.

        Args:
            instance (WeeklySchedule): The existing WeeklySchedule instance to update.
            validated_data (dict): The validated data containing updated TimeSlot information for each day.

        Returns:
            WeeklySchedule: The updated WeeklySchedule instance with new associated TimeSlots.
        """
        # Extract nested data for each day
        monday_data = validated_data.pop('monday')
        tuesday_data = validated_data.pop('tuesday')
        wednesday_data = validated_data.pop('wednesday')
        thursday_data = validated_data.pop('thursday')
        friday_data = validated_data.pop('friday')
        saturday_data = validated_data.pop('saturday')
        sunday_data = validated_data.pop('sunday')

        # Update the WeeklySchedule object
        instance.save()

        # Clear existing TimeSlots for each day
        instance.monday.clear()
        instance.tuesday.clear()
        instance.wednesday.clear()
        instance.thursday.clear()
        instance.friday.clear()
        instance.saturday.clear()
        instance.sunday.clear()

        # Create and add new TimeSlots for each day
        for time_slot_data in monday_data:
            time_slot = TimeSlot.objects.create(**time_slot_data)
            instance.monday.add(time_slot)

        for time_slot_data in tuesday_data:
            time_slot = TimeSlot.objects.create(**time_slot_data)
            instance.tuesday.add(time_slot)

        for time_slot_data in wednesday_data:
            time_slot = TimeSlot.objects.create(**time_slot_data)
            instance.wednesday.add(time_slot)

        for time_slot_data in thursday_data:
            time_slot = TimeSlot.objects.create(**time_slot_data)
            instance.thursday.add(time_slot)

        for time_slot_data in friday_data:
            time_slot = TimeSlot.objects.create(**time_slot_data)
            instance.friday.add(time_slot)

        for time_slot_data in saturday_data:
            time_slot = TimeSlot.objects.create(**time_slot_data)
            instance.saturday.add(time_slot)

        for time_slot_data in sunday_data:
            time_slot = TimeSlot.objects.create(**time_slot_data)
            instance.sunday.add(time_slot)

        return instance
