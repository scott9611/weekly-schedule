from rest_framework import viewsets
from .database.models import WeeklySchedule
from .database.serializers import WeeklyScheduleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


class WeeklyScheduleViewSet(viewsets.ModelViewSet):
    queryset = WeeklySchedule.objects.all()
    serializer_class = WeeklyScheduleSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    """
    A protected endpoint that requires authentication.
    This view function is decorated with @api_view and @permission_classes
    to ensure that only authenticated users can access it.
    
    Returns:
    - 200 OK: A JSON response containing a message and the authenticated user's string representation.
    - 401 Unauthorized: If the request is not authenticated.
    """
    return Response(data={"message": "This is a protected endpoint.", "user": str(request.user)})
