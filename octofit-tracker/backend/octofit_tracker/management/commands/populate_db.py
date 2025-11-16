from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman'])

        # Users
        iron_man = User.objects.create(username='ironman', email='ironman@marvel.com', team='Marvel')
        cap = User.objects.create(username='cap', email='cap@marvel.com', team='Marvel')
        thor = User.objects.create(username='thor', email='thor@marvel.com', team='Marvel')
        superman = User.objects.create(username='superman', email='superman@dc.com', team='DC')
        batman = User.objects.create(username='batman', email='batman@dc.com', team='DC')
        wonder_woman = User.objects.create(username='wonderwoman', email='wonderwoman@dc.com', team='DC')

        # Activities
        Activity.objects.create(user='ironman', type='run', duration=30, date='2025-11-16')
        Activity.objects.create(user='cap', type='cycle', duration=45, date='2025-11-15')
        Activity.objects.create(user='thor', type='swim', duration=60, date='2025-11-14')
        Activity.objects.create(user='superman', type='fly', duration=120, date='2025-11-13')
        Activity.objects.create(user='batman', type='train', duration=90, date='2025-11-12')
        Activity.objects.create(user='wonderwoman', type='run', duration=50, date='2025-11-11')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=135)
        Leaderboard.objects.create(team='DC', points=260)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy')
        Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='Medium')
        Workout.objects.create(name='Plank', description='Hold plank for 1 min', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
