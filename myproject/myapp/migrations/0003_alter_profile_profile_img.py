# Generated by Django 5.0.4 on 2024-04-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_profile_dob_alter_profile_fathers_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_img',
            field=models.ImageField(blank=True, default='images\\default_profile.png', upload_to='images'),
        ),
    ]
