# Generated by Django 2.2 on 2023-01-02 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appclientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
    ]
