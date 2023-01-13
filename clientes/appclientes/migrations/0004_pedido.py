# Generated by Django 2.2 on 2023-01-13 21:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appclientes', '0003_cliente_endereco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateTimeField(default=django.utils.timezone.now)),
                ('valor', models.FloatField()),
                ('status', models.CharField(choices=[('P', 'Pedido realizado'), ('F', 'Fazendo'), ('E', 'Saiu para entrega')], max_length=1)),
                ('observacoes', models.CharField(blank=True, max_length=50, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appclientes.Cliente')),
            ],
        ),
    ]
