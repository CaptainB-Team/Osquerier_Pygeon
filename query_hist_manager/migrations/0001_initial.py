# Generated by Django 3.0.5 on 2020-04-25 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QueryHistItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('query_text', models.TextField()),
                ('response_text', models.TextField()),
                ('time_issued', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
