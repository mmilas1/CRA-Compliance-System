# Generated by Django 5.2 on 2025-06-11 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0002_delete_testmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compliant', models.BooleanField()),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.requirement')),
            ],
        ),
    ]
