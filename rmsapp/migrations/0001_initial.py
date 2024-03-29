# Generated by Django 4.2.5 on 2024-01-18 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accountsreportForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='advertisementform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField(max_length=50)),
                ('socialmedia', models.IntegerField()),
                ('notices', models.IntegerField()),
                ('brochures', models.IntegerField()),
                ('posters', models.IntegerField()),
                ('newspaper', models.IntegerField()),
                ('vehicle', models.IntegerField()),
                ('television', models.IntegerField()),
                ('radio', models.IntegerField()),
                ('adtotal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='barform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.IntegerField(blank=True, null=True)),
                ('foodlist', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('selectNumber', models.IntegerField()),
                ('total', models.IntegerField()),
                ('finalamt', models.IntegerField(blank=True, null=True)),
                ('gstval', models.IntegerField(blank=True, null=True)),
                ('nettol', models.IntegerField(blank=True, null=True)),
                ('payment', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='billdetailsform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.IntegerField(blank=True, null=True)),
                ('foodlist', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('selectNumber', models.IntegerField()),
                ('total', models.IntegerField()),
                ('finalamt', models.IntegerField(blank=True, null=True)),
                ('gstval', models.IntegerField(blank=True, null=True)),
                ('nettol', models.IntegerField(blank=True, null=True)),
                ('payment', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='diningform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tableno', models.CharField(max_length=50)),
                ('waiter', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('food', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('waiterallocation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='expensesentryform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField(blank=True, max_length=50, null=True)),
                ('particular', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('totalamount', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='gasmaintenanceform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gasnumber', models.IntegerField()),
                ('cpyname', models.CharField(max_length=50)),
                ('cpycontact', models.IntegerField()),
                ('gastaken', models.IntegerField()),
                ('takendate', models.DateField(max_length=200)),
                ('gasempty', models.IntegerField()),
                ('emptydate', models.DateField(max_length=200)),
                ('gasavailable', models.IntegerField()),
                ('gasamount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GroceriesEntryform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField(blank=True, max_length=50, null=True)),
                ('groceryname', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('total', models.IntegerField()),
                ('subtotal', models.IntegerField(blank=True, null=True)),
                ('gstval', models.IntegerField(blank=True, null=True)),
                ('grandtotal', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='hotelbookingform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(max_length=100)),
                ('dob', models.DateField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('proof', models.CharField(max_length=100)),
                ('children', models.IntegerField()),
                ('adult', models.IntegerField()),
                ('aged', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('dateofbooking', models.DateField(max_length=200)),
                ('dateofvacate', models.DateField(max_length=200)),
                ('totaldays', models.IntegerField()),
                ('total', models.IntegerField()),
                ('gstvalue', models.IntegerField()),
                ('nettotal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='incomeentryform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelroombooking', models.IntegerField()),
                ('date1', models.DateField(max_length=50)),
                ('amount1', models.IntegerField()),
                ('restaurantbill', models.IntegerField()),
                ('date2', models.DateField(max_length=50)),
                ('amount2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='onlineform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billno', models.IntegerField()),
                ('platform', models.CharField(max_length=50)),
                ('customername', models.CharField(max_length=50)),
                ('mobileno', models.IntegerField()),
                ('mail', models.CharField(max_length=50)),
                ('datetime', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('foodlist', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('total', models.IntegerField()),
                ('gstval', models.IntegerField()),
                ('nettol', models.IntegerField()),
                ('paymentmode', models.CharField(max_length=50)),
                ('deliverperson', models.CharField(max_length=50)),
                ('delivercontactno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='parcelform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billno', models.IntegerField()),
                ('foodlist', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('total', models.IntegerField()),
                ('gstval', models.IntegerField()),
                ('nettol', models.IntegerField()),
                ('waiter', models.CharField(max_length=50)),
                ('customername', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='receptionform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customervisitperday', models.IntegerField()),
                ('phonecallsfromroom', models.IntegerField()),
                ('requirements', models.CharField(max_length=50)),
                ('allocate', models.CharField(max_length=50)),
                ('roomchanginginformation', models.IntegerField()),
                ('phonecallsfromoutside', models.IntegerField()),
                ('dailyreporttomanager', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='registrationform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelname', models.CharField(max_length=100)),
                ('gstno', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='roomcancellationform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('roomno', models.IntegerField()),
                ('phonenumber', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('fromdate', models.DateField(max_length=200)),
                ('todate', models.DateField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='roommaintenanceform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomtype', models.CharField(max_length=50)),
                ('bed', models.CharField(max_length=50)),
                ('roomno', models.IntegerField()),
                ('pillow', models.IntegerField()),
                ('bedsheet', models.IntegerField()),
                ('restroomcleaning', models.CharField(max_length=50)),
                ('wateravailability', models.CharField(max_length=50)),
                ('tvavailability', models.CharField(max_length=50)),
                ('acchecking', models.CharField(max_length=50)),
                ('furniturechecking', models.CharField(max_length=50)),
            ],
        ),
    ]
