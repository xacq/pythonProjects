# Generated by Django 4.2.5 on 2023-09-27 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Direction', models.TextField()),
                ('Year', models.TextField()),
                ('Date', models.DateField()),
                ('Weekday', models.TextField()),
                ('Country', models.TextField()),
                ('Commodity', models.TextField()),
                ('Transport_Mode', models.TextField()),
                ('Measure', models.TextField()),
                ('Value', models.IntegerField()),
                ('Cumulative', models.IntegerField()),
            ],
        ),
    ]