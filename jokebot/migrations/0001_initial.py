# Generated by Django 3.2.7 on 2021-09-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JokeBotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joke', models.CharField(choices=[('stupid', 'stupid'), ('fat', 'fat'), ('dumb', 'dump')], default='stupid', max_length=10)),
                ('user_id', models.CharField(max_length=20)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('count', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
