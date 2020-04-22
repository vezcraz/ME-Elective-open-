# Generated by Django 2.2.10 on 2020-04-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cdc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseCode', models.CharField(max_length=100)),
                ('CourseName', models.CharField(max_length=150)),
                ('Year', models.CharField(max_length=10)),
                ('Sem', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='courseList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BranchCode', models.CharField(max_length=100)),
                ('CourseCode', models.CharField(max_length=10)),
                ('CourseName', models.CharField(max_length=150)),
                ('Type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='courseOffered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseCode', models.CharField(max_length=15)),
                ('Tag', models.CharField(max_length=100)),
                ('CourseName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='regSem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Academic_year_start', models.CharField(max_length=4)),
                ('Registration_for_sem', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='stuCourseData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CampusID', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('CourseCode', models.CharField(max_length=15)),
            ],
        ),
    ]
