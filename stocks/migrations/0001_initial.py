# Generated by Django 3.0.1 on 2019-12-19 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(null=True, verbose_name='Quantidade')),
                ('unity', models.IntegerField(null=True, verbose_name='Unidade_de_Medida')),
                ('registered_at', models.TimeField(auto_now=True, verbose_name='Data_de_Cadastro')),
            ],
        ),
    ]
