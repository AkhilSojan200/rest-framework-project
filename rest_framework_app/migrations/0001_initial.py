# Generated by Django 5.0.3 on 2024-06-15 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.TextField(max_length=250)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
