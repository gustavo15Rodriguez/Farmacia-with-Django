# Generated by Django 2.2.4 on 2019-08-12 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('num_boleta', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('fecha', models.EmailField(max_length=254)),
                ('num_ordenpedido', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('descuento', models.IntegerField()),
                ('cod_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Clientes')),
                ('codi_empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empleado.Empleado')),
            ],
        ),
    ]
