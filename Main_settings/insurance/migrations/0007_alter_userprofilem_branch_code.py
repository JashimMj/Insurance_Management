# Generated by Django 3.2.9 on 2021-11-17 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0006_alter_userprofilem_branch_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilem',
            name='Branch_code',
            field=models.IntegerField(blank=True, max_length=30, null=True),
        ),
    ]