# Generated by Django 3.1.13 on 2021-11-05 13:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0011_auto_20211105_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beneficiaryparent',
            old_name='phone_number',
            new_name='father_phone_number',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='beneficiary_code',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='tertiary_eduction_qualification',
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='beneficiary_id',
            field=models.UUIDField(default=uuid.UUID('58643ef8-10ed-446b-b237-f14bcc024c55'), editable=False),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='education_level',
            field=models.CharField(blank=True, choices=[('none', 'NONE'), ('primary', 'Primary'), ('basic', 'Basic'), ('secondary', "Secondary O'Level"), ('certificate', 'Certificate'), ('diploma', 'Diploma'), ('degree', 'Degree'), ('masters', 'Masters'), ('doctrate', 'Doctrate'), ('phd', 'PHD')], max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='beneficiaryparent',
            name='father_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name="Father's date of birth"),
        ),
        migrations.AddField(
            model_name='beneficiaryparent',
            name='father_village',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name="Father's Village"),
        ),
        migrations.AddField(
            model_name='beneficiaryparent',
            name='mother_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name="Mother's date of birth"),
        ),
        migrations.AddField(
            model_name='beneficiaryparent',
            name='mother_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='beneficiaryparent',
            name='mother_village',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name="Mother's Village"),
        ),
    ]