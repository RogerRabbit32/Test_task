# Generated by Django 4.1.2 on 2022-10-31 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration_Login', '0002_alter_user_email_alter_user_login_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='tg',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]