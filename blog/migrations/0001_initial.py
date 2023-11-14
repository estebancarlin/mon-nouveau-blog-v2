# Generated by Django 2.2.28 on 2022-11-14 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id_lieu', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('disponibilite', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id_animal', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('etat', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('race', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=200)),
                ('lieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Lieu')),
            ],
        ),
    ]
