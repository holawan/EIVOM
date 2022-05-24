# Generated by Django 3.2.12 on 2022-05-24 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
                ('user', models.ManyToManyField(blank=True, related_name='like_genres', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('original_title', models.CharField(max_length=100)),
                ('poster_path', models.CharField(max_length=200, null=True)),
                ('backdrop_path', models.CharField(max_length=200, null=True)),
                ('overview', models.TextField()),
                ('release_date', models.DateField()),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('popularity', models.FloatField()),
                ('runtime', models.IntegerField(null=True)),
                ('tagline', models.CharField(max_length=300, null=True)),
                ('actor_id', models.JSONField(null=True)),
                ('actors', models.JSONField(null=True)),
                ('actors_path', models.JSONField(null=True)),
                ('view_count', models.IntegerField(default=0)),
                ('director', models.TextField()),
                ('cluster', models.IntegerField(default=0)),
                ('genres', models.ManyToManyField(related_name='movie_genres', to='movies.Genre')),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('rate', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_reviews', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
