# Generated by Django 3.1.13 on 2021-11-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0008_agentdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentdetail',
            name='agend_ID',
            field=models.CharField(default='4991B4B', max_length=100, verbose_name='Agent Id'),
        ),
    ]
