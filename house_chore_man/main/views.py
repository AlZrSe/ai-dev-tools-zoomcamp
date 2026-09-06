from django.shortcuts import render
from django.views.generic import ListView
from .models import Chore, Room, HouseholdMember

class ChoreListView(ListView):
    model = Chore
    template_name = 'main/chore_list.html'
    context_object_name = 'chores'
    paginate_by = 25  # if we want pagination, but we can adjust later

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter by frequency
        frequency = self.request.GET.get('frequency')
        if frequency:
            queryset = queryset.filter(frequency=frequency)
        # Filter by assignee (HouseholdMember)
        assignee_id = self.request.GET.get('assignee')
        if assignee_id:
            queryset = queryset.filter(assigned_to_id=assignee_id)
        # Filter by room
        room_id = self.request.GET.get('room')
        if room_id:
            queryset = queryset.filter(room_id=room_id)
        # Filter by status (completed)
        status = self.request.GET.get('status')
        if status is not None:
            # status is string 'True' or 'False'
            if status.lower() == 'true':
                queryset = queryset.filter(completed=True)
            elif status.lower() == 'false':
                queryset = queryset.filter(completed=False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add filter choices to context
        context['frequencies'] = Chore.FREQUENCY_CHOICES
        context['assignees'] = HouseholdMember.objects.all()
        context['rooms'] = Room.objects.all()
        # We'll keep the current filter values in context to show in the form
        context['current_filters'] = {
            'frequency': self.request.GET.get('frequency', ''),
            'assignee': self.request.GET.get('assignee', ''),
            'room': self.request.GET.get('room', ''),
            'status': self.request.GET.get('status', ''),
        }
        return context