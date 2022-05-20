# Generated by Django 3.2.12 on 2022-05-20 02:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crewname', models.CharField(max_length=10, unique=True)),
                ('crewintro', models.CharField(max_length=30)),
                ('crew_image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='thumbnails/')),
                ('crew_location1', models.CharField(choices=[(11, '서울특별시'), (21, '부산광역시'), (22, '대구광역시'), (23, '인천광역시'), (24, '광주광역시'), (25, '대전광역시'), (26, '울산광역시'), (29, '세종특별자치시'), (31, '경기도'), (32, '강원도'), (33, '충청북도'), (34, '충청남도'), (35, '전라북도'), (36, '전라남도'), (37, '경상북도'), (38, '경상남도'), (39, '제주특별자치도')], max_length=10)),
                ('crew_location2', models.CharField(max_length=5)),
                ('crew_leader', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='leader_user', to=settings.AUTH_USER_MODEL)),
                ('movies', models.ManyToManyField(blank=True, to='movies.Movie')),
                ('user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CrewArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crews.crew')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CrewReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crews.crewarticle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]