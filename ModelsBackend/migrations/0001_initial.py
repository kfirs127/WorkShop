# Generated by Django 4.0.4 on 2022-06-16 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('apartmentNum', models.IntegerField()),
                ('zipCode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.UUIDField(null=True)),
                ('storeId', models.IntegerField(null=True)),
            ],
            options={
                'unique_together': {('userId', 'storeId')},
            },
        ),
        migrations.CreateModel(
            name='BankModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountNumber', models.IntegerField()),
                ('branch', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='DiscountModel',
            fields=[
                ('discountID', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100, null=True)),
                ('productID', models.IntegerField(null=True)),
                ('percent', models.FloatField(null=True)),
                ('type', models.CharField(choices=[('Product', 'Product'), ('Category', 'Category'), ('Store', 'Store'), ('Composite', 'Composite')], max_length=100)),
                ('composite_type', models.CharField(choices=[('Max', 'Max'), ('Add', 'Add'), ('XOR', 'XOR')], max_length=100, null=True)),
                ('decide', models.IntegerField(choices=[(1, 1), (2, 2)], null=True)),
                ('dID1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firstDiscountID', to='ModelsBackend.discountmodel')),
                ('dID2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondDiscountID', to='ModelsBackend.discountmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Initialized',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_initialized', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LoginDateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.UUIDField()),
                ('username', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('storeId', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RuleModel',
            fields=[
                ('rule_class', models.CharField(choices=[('DiscountComposite', 'DiscountComposite'), ('Price', 'Price'), ('PurchaseComposite', 'PurchaseComposite'), ('Quantity', 'Quantity'), ('Weight', 'Weight')], max_length=100, null=True)),
                ('ruleID', models.IntegerField(primary_key=True, serialize=False)),
                ('rule_kind', models.CharField(choices=[('Discount', 'Discount'), ('Purchase', 'Purchase')], max_length=100)),
                ('simple_rule_type', models.CharField(choices=[('Store', 'Store'), ('Category', 'Category'), ('Product', 'Product')], max_length=100, null=True)),
                ('composite_rule_type', models.CharField(choices=[('Or', 'Or'), ('And', 'And')], max_length=100, null=True)),
                ('filter_type', models.CharField(max_length=100, null=True)),
                ('at_least', models.IntegerField(null=True)),
                ('at_most', models.IntegerField(null=True)),
                ('ruleID1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firstRuleID', to='ModelsBackend.rulemodel')),
                ('ruleID2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondRuleID', to='ModelsBackend.rulemodel')),
            ],
        ),
        migrations.CreateModel(
            name='StoreModel',
            fields=[
                ('storeID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ModelsBackend.addressmodel')),
                ('bankAccount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ModelsBackend.bankmodel')),
            ],
        ),
        migrations.CreateModel(
            name='StoreTransactionModel',
            fields=[
                ('storeId', models.IntegerField()),
                ('storeName', models.CharField(max_length=100)),
                ('transactionId', models.IntegerField(primary_key=True, serialize=False)),
                ('paymentId', models.IntegerField()),
                ('deliveryId', models.IntegerField(null=True)),
                ('date', models.DateField(auto_now=True)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserTransactionModel',
            fields=[
                ('userID', models.UUIDField()),
                ('transactionId', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('totalAmount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.TextField(null=True)),
                ('userid', models.UUIDField(primary_key=True, serialize=False)),
                ('isLoggedIn', models.BooleanField(default=False)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.cartmodel')),
                ('transactions', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.usertransactionmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MemberModel',
            fields=[
                ('usermodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('member_password', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('is_admin', models.BooleanField(null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.addressmodel')),
                ('bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.bankmodel')),
            ],
            options={
                'abstract': False,
            },
            bases=('ModelsBackend.usermodel',),
        ),
        migrations.CreateModel(
            name='TransactionsInStoreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.storemodel')),
                ('transactionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.storetransactionmodel')),
            ],
        ),
        migrations.CreateModel(
            name='StoreTransactionsInUserTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storeTransaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.storetransactionmodel')),
                ('userTransaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.usertransactionmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsInStoreTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.productmodel')),
                ('transactionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.storetransactionmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsInStoreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.productmodel')),
                ('storeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.storemodel')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsInBagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('bag_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.bagmodel')),
                ('product_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.productmodel')),
            ],
        ),
        migrations.CreateModel(
            name='DiscountRulesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discountID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ModelsBackend.discountmodel')),
                ('ruleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.rulemodel')),
            ],
        ),
        migrations.CreateModel(
            name='BagsInCartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storeID', models.IntegerField()),
                ('bag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.bagmodel')),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.cartmodel')),
            ],
        ),
        migrations.AddField(
            model_name='storemodel',
            name='founderId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ModelsBackend.membermodel'),
        ),
        migrations.AddField(
            model_name='storemodel',
            name='managers',
            field=models.ManyToManyField(related_name='managers', to='ModelsBackend.membermodel'),
        ),
        migrations.AddField(
            model_name='storemodel',
            name='owners',
            field=models.ManyToManyField(related_name='owners', to='ModelsBackend.membermodel'),
        ),
        migrations.CreateModel(
            name='StoreAppointersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.storemodel')),
                ('assigner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='assigner', to='ModelsBackend.membermodel')),
                ('assingee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='assingee', to='ModelsBackend.membermodel')),
            ],
        ),
        migrations.CreateModel(
            name='RulesInStoreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.rulemodel')),
                ('storeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.storemodel')),
            ],
            options={
                'unique_together': {('storeID', 'ruleID')},
            },
        ),
        migrations.CreateModel(
            name='ProductKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100, null=True)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.productmodel')),
            ],
            options={
                'unique_together': {('product_id', 'keyword')},
            },
        ),
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('read', models.BooleanField(default=False)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.membermodel')),
            ],
        ),
        migrations.CreateModel(
            name='DiscountsInStoreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discountID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.discountmodel')),
                ('storeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.storemodel')),
            ],
            options={
                'unique_together': {('storeID', 'discountID')},
            },
        ),
        migrations.CreateModel(
            name='BidOfferModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newPrice', models.FloatField()),
                ('active', models.BooleanField(default=True)),
                ('isAccepted', models.BooleanField(default=False)),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.productmodel')),
                ('storeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.storemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('permissionsGuys', models.ManyToManyField(related_name='permissionsGuys', to='ModelsBackend.membermodel')),
            ],
        ),
        migrations.CreateModel(
            name='StoreUserPermissionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointManager', models.BooleanField(default=False)),
                ('appointOwner', models.BooleanField(default=False)),
                ('closeStore', models.BooleanField(default=False)),
                ('stockManagement', models.BooleanField(default=False)),
                ('changePermission', models.BooleanField(default=False)),
                ('rolesInformation', models.BooleanField(default=False)),
                ('purchaseHistoryInformation', models.BooleanField(default=False)),
                ('discount', models.BooleanField(default=False)),
                ('bid', models.BooleanField(default=False)),
                ('storeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.storemodel')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsBackend.membermodel')),
            ],
            options={
                'unique_together': {('userID', 'storeID')},
            },
        ),
    ]
