from django.db import models

# Create your models here.
class Category(models.Model):
    # create colons for table
    category_name = models.CharField(max_length=75)
    reg_date = models.DateTimeField(auto_now_add=True)

    # in admin panel instead of right category name will be Category object(1) if we don't return it as category_name
    def __str__(self):
        return self.category_name

# create product table
class Product(models.Model):
    # create colons table
    product_name = models.CharField(max_length=125)
    product_count = models.IntegerField()
    product_price = models.FloatField()
    # for saving pictures it's required to install additional library like "pillow"
    product_photo = models.ImageField(upload_to='media')
    product_description = models.TextField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_product_quantity = models.IntegerField()
    total_for_product = models.FloatField()

    def __str__(self):
        # we have to point it as str because 'Product' return us as a object
        return str(self.user_product)

    # python manage.py makemigrations create table with last modifications
    # python manage.py migrate  add new changes to actual sqlite table in our case