# Generated by Django 3.2.2 on 2021-05-07 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommiteeMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=30, null=True)),
                ('district', models.CharField(max_length=30, null=True)),
                ('message', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=30, null=True)),
                ('contacts', models.IntegerField(max_length=30, null=True)),
                ('profession', models.IntegerField(max_length=30, null=True)),
                ('date', models.TimeField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inquiries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=30, null=True)),
                ('subject', models.CharField(max_length=30, null=True)),
                ('message', models.TextField(max_length=200, null=True)),
                ('date', models.TimeField()),
            ],
            options={
                'verbose_name': 'names',
            },
        ),
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, null=True)),
                ('author', models.CharField(max_length=200, null=True)),
                ('fieldofstudy', models.CharField(max_length=30, null=True)),
                ('company', models.CharField(max_length=200, null=True)),
                ('date', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=30, null=True)),
                ('district', models.CharField(max_length=30, null=True)),
                ('message', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, null=True)),
                ('agenda', models.CharField(max_length=30, null=True)),
                ('message', models.TextField(max_length=200, null=True)),
            ],
        ),
    ]
