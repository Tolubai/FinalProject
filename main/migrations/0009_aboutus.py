# Generated by Django 3.2.5 on 2021-07-19 11:35

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210719_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('images', models.ImageField(blank=True, null=True, upload_to=main.models.upload_to)),
            ],
        ),
    ]
