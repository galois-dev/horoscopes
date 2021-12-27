from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.

# Horoscopes

class Horoscope(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_horoscopes')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_horoscopes')
    summary = models.TextField(default="")
    tags = models.ManyToManyField('Tag', related_name='horoscopes')

    def __str__(self):
        return self.name

    def __init__(self, **kwargs):
        if "request" in kwargs:
            request = kwargs.pop("request")
            self.created_by = request.user
            self.updated_by = request.user
        super(Horoscope, self).__init__(**kwargs)
            
    def save(self, **kwargs):
        if "request" in kwargs:
            request = kwargs.pop("request")
            self.created_by = request.user
            self.updated_by = request.user
        super(Horoscope, self).save(**kwargs)

    class Meta:
        ordering = ['-created_at']


class Tag(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __init__(self, **kwargs):
        if "request" in kwargs:
            request = kwargs.pop("request")
            self.updated_by = request.user
        super(Tag, self).__init__(**kwargs)
            
    def save(self, **kwargs):
        if "request" in kwargs:
            request = kwargs.pop("request")
            self.updated_by = request.user
        super(Tag, self).save(**kwargs)

    class Meta:
        ordering = ['-created_at']

class Horoscope_Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    sent_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_horoscopes')
    horoscope = models.ForeignKey('Horoscope', on_delete=models.CASCADE, related_name='messages')
    status = CharField(
        max_length=1,
        choices=[
            ('S', 'Sent'),
            ('R', 'Received'),
            ('D', 'Deleted'),
        ],
        default='S',
    )

    class Meta:
        ordering = ['-created_at']


class Horoscope_Push_Notification(models.Model):
    horoscope = models.ForeignKey(Horoscope, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    scheduled_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-created_at']


class Astrological_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    birth_time = models.TimeField()
    birth_place = models.CharField(max_length=50)
    residence = models.CharField(max_length=50)
    starsign = models.CharField(max_length=1, choices=[
        ('A', 'Aries'),
        ('T', 'Taurus'),
        ('G', 'Gemini'),
        ('C', 'Cancer'),
        ('L', 'Leo'),
        ('S', 'Sagittarius'),
        ('V', 'Virgo'),
        ('P', 'Pisces'),
        ('E', 'Aquarius'),
        ('S', 'Scorpio'),
        ('N', 'Capricorn'),
        ('U', 'Unspecified'),
    ])
    planetary_affinity = models.CharField(max_length=1, choices=[
        ('E', 'Earth'),
        ('M', 'Mars'),
        ('J', 'Jupiter'),
        ('S', 'Saturn'),
        ('U', 'Uranus'),
        ('N', 'Neptune'),
        ('P', 'Pluto'),
        ('V', 'Venus'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

        
class User_Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.CharField(max_length=1, choices=[
        ('T', 'Trial'),
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stripe_subscription_id = models.CharField(max_length=50)
    stripe_subscription_blob = models.JSONField()

    class Meta:
        ordering = ['-created_at']
