# Generated by Django 3.1.7 on 2021-05-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_no', models.IntegerField(unique=True)),
                ('status', models.CharField(choices=[('savings', 'savings'), ('current', 'current')], default='ordered', max_length=10)),
                ('acc_type', models.CharField(choices=[('savings', 'savings'), ('current', 'current')], max_length=10)),
                ('bal', models.FloatField(default=0)),
                ('user', models.CharField(max_length=10)),
            ],
        ),
    ]