# Generated by Django 3.0.4 on 2020-03-23 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makers', '0001_initial'),
        ('hospitals', '0005_auto_20200320_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_per_week', models.PositiveIntegerField(default=0, verbose_name='cantidad por week')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makers.Maker')),
                ('need', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.Need')),
            ],
        ),
    ]
