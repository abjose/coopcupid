import datetime

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    # Make primary key?
    user = models.OneToOneField(User, on_delete=models.CASCADE)#, primary_key=True)
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Community(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField('date created')
    bio = models.TextField()

    # Ideas for fields: https://www.ic.org/directory/search/
    size = models.IntegerField()
    cool = models.BooleanField(default=False)
    class SmellyLevel(models.TextChoices):
        SF = '1', 'Scent-Free'
        SS = '2', 'Slightly Smelly'
        QR = '3', 'Quite Rank'
    smelliness = models.CharField(blank=True, choices=SmellyLevel.choices, max_length=20)
    # This should be a Question, shouldn't it?

    class Meta:
        verbose_name_plural = "communities"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    creation_date = models.DateTimeField('date created')
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    content = models.TextField()

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField('date')
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    description = models.TextField()

    def __str__(self):
        return self.title


class Opening(models.Model):
    title = models.CharField(max_length=100)
    creation_date = models.DateTimeField('date created')
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=False)

    # need stuff like: associated questions
    # probably also need an Application model

    def __str__(self):
        return self.title


# Meant to allow multiple kinds of membership in a community.
# Should this be something else? maybe not the best way to limit access like to admin features
class Membership(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    class MemberType(models.IntegerChoices):
        FULL = 1, "Full"
        SOCIAL = 2, "Social"
        ALUM = 3, "Alum"
        FOLLOWER = 4, "Follower"
    member_type = models.IntegerField(choices=MemberType.choices)

    def __str__(self):
        return f"{self.profile} -> {self.community} ({self.get_member_type_display()})"


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    class QuestionType(models.IntegerChoices):
        CHOICE = 1
        TEXT = 2
    question_type = models.IntegerField(choices=QuestionType.choices)

    def __str__(self):
        return self.question_text


class ChoiceResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # Can be either from a User or Community.
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
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
