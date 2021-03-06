# Generated by Django 3.1.1 on 2020-10-11 18:19

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
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bp', models.IntegerField()),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bmi', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pulse', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('respiration', models.IntegerField()),
                ('height', models.IntegerField()),
                ('oxygen_saturation', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
