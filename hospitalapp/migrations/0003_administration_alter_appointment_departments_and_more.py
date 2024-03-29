# Generated by Django 4.2.5 on 2024-01-05 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0002_donation_alter_appointment_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='departments',
            field=models.CharField(choices=[('orthopedic', 'ORTHOPEDIC'), ('gynocology', 'GYNOCOLOGY'), ('cardiology', 'CARDIOLOGY'), ('neurology', 'NEUROLOGY'), ('ent', 'ENT')], max_length=20),
        ),
        migrations.AlterField(
            model_name='donation',
            name='bloodgroup',
            field=models.CharField(choices=[('ab', 'AB'), ('o', 'O+'), ('a', 'A+'), ('b', 'B+')], max_length=10),
        ),
    ]
