# Generated by Django 2.0.6 on 2018-11-12 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('can_publish', 'Can publish a blog post'),)},
        ),
    ]
