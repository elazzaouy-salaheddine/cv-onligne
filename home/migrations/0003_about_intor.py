# Generated by Django 3.2 on 2021-05-03 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_about_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='intor',
            field=models.TextField(default='daa'),
            preserve_default=False,
        ),
    ]
