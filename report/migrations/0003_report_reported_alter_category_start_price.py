# Generated by Django 4.1.7 on 2023-04-11 05:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0002_category_alter_report_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='reported',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='start_price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(500), django.core.validators.MaxValueValidator(10000)]),
        ),
    ]