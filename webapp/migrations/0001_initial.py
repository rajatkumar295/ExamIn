# Generated by Django 3.0.3 on 2020-04-02 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=10)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('dateofbirth', models.DateField()),
                ('address', models.TextField()),
            ],
        ),
    ]
