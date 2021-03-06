# Generated by Django 3.1.4 on 2021-01-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('year', models.DateField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
