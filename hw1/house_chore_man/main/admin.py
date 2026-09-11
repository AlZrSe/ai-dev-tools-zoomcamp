from django.contrib import admin
from .models import HouseholdMember, Room, Chore, ChoreAssignment

@admin.register(HouseholdMember)
class HouseholdMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'created_at')
    list_filter = ('role', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('name',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Chore)
class ChoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'frequency', 'room', 'assigned_to', 'due_date', 'completed')
    list_filter = ('frequency', 'completed', 'due_date', 'room')
    search_fields = ('name', 'description')
    ordering = ('due_date', 'name')
    date_hierarchy = 'due_date'

@admin.register(ChoreAssignment)
class ChoreAssignmentAdmin(admin.ModelAdmin):
    list_display = ('chore', 'assigned_to', 'assigned_date', 'completed_date', 'status')
    list_filter = ('status', 'assigned_date', 'completed_date')
    search_fields = ('chore__name', 'assigned_to__name')
    ordering = ('-assigned_date',)

