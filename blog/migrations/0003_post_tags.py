# Generated by Django 5.0.2 on 2024-02-22 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.tag'),
        ),
    ]
