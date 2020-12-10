# Generated by Django 2.2 on 2020-12-05 08:18

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('course', multiselectfield.db.fields.MultiSelectField(choices=[('django', 'django'), ('python', 'python'), ('mysql', 'mysql')], max_length=200)),
                ('location', multiselectfield.db.fields.MultiSelectField(choices=[('Hyderabad', 'Hyderabad'), ('Delhi', 'Delhi'), ('Bengalore', 'Bengalore')], max_length=200)),
                ('gender', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=100)),
            ],
        ),
    ]
