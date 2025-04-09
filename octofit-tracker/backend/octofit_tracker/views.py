from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout
from rest_framework_mongoengine.viewsets import ModelViewSet as DocumentViewSet

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': 'http://localhost:8000/api/users/',
        'teams': 'http://localhost:8000/api/teams/',
        'activities': 'http://localhost:8000/api/activities/',
        'leaderboard': 'http://localhost:8000/api/leaderboard/',
        'workouts': 'http://localhost:8000/api/workouts/',
    })

class UserViewSet(DocumentViewSet):
    queryset = User.objects
    serializer_class = UserSerializer

class TeamViewSet(DocumentViewSet):
    queryset = Team.objects
    serializer_class = TeamSerializer

class ActivityViewSet(DocumentViewSet):
    queryset = Activity.objects
    serializer_class = ActivitySerializer

class LeaderboardViewSet(DocumentViewSet):
    queryset = Leaderboard.objects
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(DocumentViewSet):
    queryset = Workout.objects
    serializer_class = WorkoutSerializer