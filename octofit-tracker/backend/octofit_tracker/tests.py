from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create_user(username='ironman', email='ironman@marvel.com', team=team)
        self.assertEqual(user.email, 'ironman@marvel.com')
        self.assertEqual(user.team.name, 'Marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='DC')
        self.assertEqual(team.name, 'DC')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30)
        self.assertEqual(activity.type, 'run')
        self.assertEqual(activity.duration, 30)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes')
        self.assertEqual(workout.name, 'Morning Cardio')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
