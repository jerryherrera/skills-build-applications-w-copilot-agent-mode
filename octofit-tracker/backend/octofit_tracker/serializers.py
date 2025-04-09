from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TeamSerializer(DocumentSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class ActivitySerializer(DocumentSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class LeaderboardSerializer(DocumentSerializer):
    class Meta:
        model = Leaderboard
        fields = '__all__'

class WorkoutSerializer(DocumentSerializer):
    class Meta:
        model = Workout
        fields = '__all__'