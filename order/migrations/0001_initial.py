# Generated by Django 3.0.8 on 2020-08-04 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market', '0002_auto_20200804_1302'),
        ('recipient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_created_datetime', models.DateTimeField(auto_now_add=True)),
                ('delivery_datetime', models.DateTimeField()),
                ('delivery_address', models.CharField(max_length=200, verbose_name='address')),
                ('status', models.CharField(choices=[('CREATED', 'created'), ('DELIVERED', 'delivered'), ('PROCESSED', 'processed'), ('CANCELLED', 'cancelled')], max_length=200, verbose_name='status')),
                ('product_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.ProductSets')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipient.Recipient')),
            ],
        ),
    ]
