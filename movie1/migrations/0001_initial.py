# Generated by Django 2.1.2 on 2018-10-29 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(max_length=50)),
                ('actor_movie', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=30)),
                ('song_name', models.CharField(max_length=30)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie1.Movies')),
            ],
        ),
    ]
