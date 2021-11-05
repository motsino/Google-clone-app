from django.db import models
from django.contrib.auth.models import User
# Extending the user model
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Search(models.Model):
    link = models.URLField(max_length=300)
    title = models.CharField(max_length=500)
    item_url = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class Top_search_first(models.Model):
    link = models.URLField(max_length=300)
    item = models.CharField(max_length=500)

    def __str__(self):
        return self.item


class Top_search_second(models.Model):
    link = models.URLField(max_length=300)
    item = models.CharField(max_length=500)

    def __str__(self):
        return self.item


class Side_search(models.Model):
    link = models.URLField(max_length=300)
    item = models.CharField(max_length=500)

    def __str__(self):
        return self.item


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default='', null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    residential_address = models.CharField(max_length=500, blank=True)
    state_of_origin = models.CharField(max_length=100, blank=True)
    favorite_food = models.CharField(max_length=200, blank=True)
    about = models.TextField(blank=True, max_length=700)
    photo = models.FileField(
        upload_to='images/', null=True, verbose_name='', blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
