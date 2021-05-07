from django.db import models

# Create your models here.


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
    profession = models.CharField(
        max_length=200,
        null=True
    )

    date = models.DateTimeField(
        auto_now=True
    )
    

class Inquiries(models.Model):

    class Meta:
        pass

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

    date = models.DateTimeField(
        auto_now=True, 
       
    )


    '''def __str__(self):
        return self.names'''



class Contacts(models.Model):

    names = models.CharField(
        max_length=30,
        null=True,
    )

    contacts = models.IntegerField(
        null=True
    )

    profession = models.IntegerField(
        null=False
    )

    date = models.TimeField(
        null=True
    )

class Program(models.Model):
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


