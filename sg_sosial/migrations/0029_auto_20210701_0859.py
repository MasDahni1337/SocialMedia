# Generated by Django 3.0.2 on 2021-07-01 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sg_sosial', '0028_auto_20210701_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komenguna',
            name='isiKomen',
            field=models.CharField(max_length=300),
        ),
    ]
