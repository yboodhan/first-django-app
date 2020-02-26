from django.db import models
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# Declaring classes automatically generates tables and fields
# Primary keys are added automatically

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# Run with:
# python manage.py makemigrations polls
# python manage.py migrate
# python manage.py shell

# Superuser: python manage.py createsuperuser, testuser, testuser@email.com