# Generated by Django 5.0 on 2024-01-10 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='instagram_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='post',
            field=models.CharField(max_length=30),
        ),
    ]