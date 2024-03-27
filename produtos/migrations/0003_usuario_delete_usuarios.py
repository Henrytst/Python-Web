# Generated by Django 5.0.2 on 2024-02-13 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('idade', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
