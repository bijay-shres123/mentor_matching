# Generated by Django 4.1 on 2022-09-26 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0010_alter_preference_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preference',
            options={'ordering': ('rank',)},
        ),
        migrations.AlterField(
            model_name='basemodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='std_mnt_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]