# Generated by Django 3.2.12 on 2022-05-23 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crew',
            name='crew_location1',
            field=models.CharField(blank=True, choices=[(11, '서울특별시'), (21, '부산광역시'), (22, '대구광역시'), (23, '인천광역시'), (24, '광주광역시'), (25, '대전광역시'), (26, '울산광역시'), (29, '세종특별자치시'), (31, '경기도'), (32, '강원도'), (33, '충청북도'), (34, '충청남도'), (35, '전라북도'), (36, '전라남도'), (37, '경상북도'), (38, '경상남도'), (39, '제주특별자치도')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='crew',
            name='crew_location2',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]