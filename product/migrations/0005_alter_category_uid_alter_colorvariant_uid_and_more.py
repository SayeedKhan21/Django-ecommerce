# Generated by Django 4.1.5 on 2023-02-04 11:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_colorvariant_sizevariant_alter_category_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('81898eb4-67b5-4208-9536-bb5a2eb12496'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='colorvariant',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('81898eb4-67b5-4208-9536-bb5a2eb12496'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, null=True, to='product.colorvariant'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, to='product.sizevariant'),
        ),
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('81898eb4-67b5-4208-9536-bb5a2eb12496'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('81898eb4-67b5-4208-9536-bb5a2eb12496'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sizevariant',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('81898eb4-67b5-4208-9536-bb5a2eb12496'), editable=False, primary_key=True, serialize=False),
        ),
    ]
