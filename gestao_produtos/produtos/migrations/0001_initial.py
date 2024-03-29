# Generated by Django 2.2.7 on 2019-11-26 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('quantidade', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('descricao', models.TextField()),
                ('photo', models.ImageField(blank='true', null='true', upload_to='clients_photos')),
            ],
        ),
    ]
