# Generated by Django 3.2.9 on 2021-11-17 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0004_userprofilem_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilem',
            name='Branch_code',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
