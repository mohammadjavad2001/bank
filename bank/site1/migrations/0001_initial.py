from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('Transaction_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Transaction_type', models.CharField(max_length=50)),
                ('Destination_id', models.IntegerField()),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('done', models.BooleanField(default=False)),
                ('Origin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site1.customer')),
            ],
            options={
                'db_table': 'Transaction',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.IntegerField(primary_key=True, serialize=False)),
                ('balance', models.BigIntegerField()),
                ('createddate', models.DateField()),
                ('deleteddate', models.DateField()),
                ('Customerid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='site1.customer')),
            ],
            options={
                'db_table': 'Acoount',
            },
        ),
    ]
