from django.db import models

# Create your models here.
class contactUs(models.Model):

    class Meta:
        verbose_name = "names"

    names = models.CharField(
        max_length=30,
        null=True,
    )

    subject = models.CharField(
        max_length=30,
        null=True
    )

    message = models.TextField(
        max_length=200,
        null=True
    )

    date = models.TimeField(
        auto_now=False, 
        auto_now_add=False
    )


    def __str__(self):
        return self.names


class Participants(models.Model):

    names = models.CharField(
        max_length=30,
        null=True,
    )

    district = models.CharField(
        max_length=30,
        null=True
    )

    message = models.TextField(
        max_length=200,
        null=True
    )


class CommiteeMembers(models.Model):
    names = models.CharField(
        max_length=30,
        null=True,
    )

    district = models.CharField(
        max_length=30,
        null=True
    )
    message = models.TextField(
        max_length=200,
        null=True
    )
    
class Papers(models.Model):
    title = models.CharField(
        max_length=30,
        null=True
    )

    author = models.CharField(
        max_length=200,
        null=True
    )

    fieldofstudy = models.CharField(
        max_length=30,
        null=True
    )

    company = models.CharField(
        max_length=200,
        null=True
    )
    
    date = models.CharField(
        max_length=30,
        null=True
    )
    

class Contacts(models.Model):

    names = models.CharField(
        max_length=30,
        null=True,
    )

    contacts = models.IntegerField(
        max_length=30,
        null=True
    )

    profession = models.IntegerField(
        max_length=30,
        null=True
    )

    date = models.TimeField(
        max_length=200,
        null=True
    )

class program(models.Model):
    title = models.CharField(
        max_length=30,
        null=True,
    )

    agenda = models.CharField(
        max_length=30,
        null=True
    )

    message = models.TextField(
        max_length=200,
        null=True
    )


