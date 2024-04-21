# Generated by Django 4.2.7 on 2024-02-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CusOrders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_code', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
    ]
