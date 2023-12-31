# Generated by Django 4.2 on 2023-06-11 00:30

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
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('fecha_publicacion', models.DateField()),
            ],
        ),
    ]
