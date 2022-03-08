import datetime

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300)


class Community(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField('date created')
    bio = models.CharField(max_length=300)

    # Ideas for fields: https://www.ic.org/directory/search/
    size = models.IntegerField()
    cool = models.BooleanField(default=False)
    class SmellyLevel(models.TextChoices):
        SF = '1', 'Scent-Free'
        SS = '2', 'Slightly Smelly'
        QR = '3', 'Quite Rank'
    smelliness = models.CharField(blank=True, choices=SmellyLevel.choices, max_length=20)

    class Meta:
        verbose_name_plural = "communities"
    
    def __str__(self):
        return self.name


# Meant to allow multiple kinds of membership in a community.
# Should this be something else? maybe not the best way to limit access like to admin features
class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    # Should this be an enum?
    membership_type = models.CharField(max_length=30)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class ChoiceResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # Can be either from a User or Community.
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, null=True, blank=True)

    # Stick with a single "spectrum" of possibilities so easier to compare answers.
    class ChoiceValue(models.IntegerChoices):
        STRONG_DISAGREE = 1
        DISAGREE = 2
        NEUTRAL = 3
        AGREE = 4
        STRONG_AGREE = 5
    choice = models.IntegerField(choices=ChoiceValue.choices)

    # def __str__(self):
    #     return self.choice_text

# So have question/answers, what about other information?
# like diet, astrological sign, religion, ...
# even better if can optionally choose multiple answers
# but also - those could be formulated as regular questions, better to leave them that way?
# but do need stuff like "house has 10 people out of 12 max"
# could have things other than Choice - like TextResponse and NumberResponse, that go with Questions
# for now just have them directly on the profile, I think...
