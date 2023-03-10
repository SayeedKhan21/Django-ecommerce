# Generated by Django 4.1.5 on 2023-02-08 07:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_cart_uid_alter_cartitems_uid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('22a407aa-4609-458e-9380-36dcd7715502'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('coupon_code', models.CharField(max_length=10)),
                ('is_expired', models.BooleanField(default=False)),
                ('discount_price', models.IntegerField(default=100)),
                ('minimum_amount', models.IntegerField(default=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='cart',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('22a407aa-4609-458e-9380-36dcd7715502'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('22a407aa-4609-458e-9380-36dcd7715502'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('22a407aa-4609-458e-9380-36dcd7715502'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='colorvariant',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('22a407aa-4609-458e-9380-36dcd7715502'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('22a407aa-4609-458e-9380-36dcd7715502'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('22a407aa-4609-458e-9380-36dcd7715502'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sizevariant',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('22a407aa-4609-458e-9380-36dcd7715502'), editable=False, primary_key=True, serialize=False),
        ),
    ]
