# Generated by Django 4.0.4 on 2022-05-25 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
