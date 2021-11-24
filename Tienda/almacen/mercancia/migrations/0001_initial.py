# Generated by Django 3.2.9 on 2021-11-19 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=32)),
                ('marca', models.CharField(max_length=15)),
                ('modelo', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='Img')),
            ],
        ),
    ]
