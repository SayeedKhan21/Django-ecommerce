# Generated by Django 4.1.5 on 2023-02-04 07:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_slug_product_slug_alter_category_uid_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='product_image',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='category',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('cc69ccf1-8ae3-4d98-a94f-3aa762020408'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('cc69ccf1-8ae3-4d98-a94f-3aa762020408'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='product.product'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('cc69ccf1-8ae3-4d98-a94f-3aa762020408'), editable=False, primary_key=True, serialize=False),
        ),
    ]