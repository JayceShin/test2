# Generated by Django 3.0.2 on 2020-01-12 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inception', '0003_calculator'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(verbose_name='image')),
                ('item', models.TextField(verbose_name='item')),
                ('result', models.TextField(verbose_name='result')),
            ],
        ),
    ]
