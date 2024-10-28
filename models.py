from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    photo=models.CharField(max_length=300)

class Wood(models.Model):
    CATEGORY=models.ForeignKey(Category,on_delete=models.CASCADE)
    wood_name=models.CharField(max_length=100)
    sqft_charge=models.BigIntegerField()
class Shapes(models.Model):
    CATEGORY = models.ForeignKey(Category, on_delete=models.CASCADE)
    shape=models.CharField(max_length=100)


class Diamension(models.Model):
    SHAPES=models.ForeignKey(Shapes,on_delete=models.CASCADE)
    height=models.BigIntegerField()
    width=models.BigIntegerField()
    total_wood_needed=models.BigIntegerField()

class Design(models.Model):
    WOOD=models.ForeignKey(Wood,on_delete=models.CASCADE)
    price=models.BigIntegerField()
    shape=models.CharField(max_length=100,default="")
    description=models.CharField(max_length=100)
    photo=models.CharField(max_length=300)
    design_name=models.CharField(max_length=100)


class Post(models.Model):
    post_name=models.CharField(max_length=100)
    DESIGN=models.ForeignKey(Design,on_delete=models.CASCADE)
    photo_1=models.CharField(max_length=100)
    photo_2= models.CharField(max_length=100)
    photo_3 = models.CharField(max_length=100)
    description_1=models.CharField(max_length=100)
    description_2 = models.CharField(max_length=100)
    description_3 = models.CharField(max_length=100)

class Product(models.Model):
    product_name=models.CharField(max_length=100)
    material=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    price = models.BigIntegerField()
    photo=models.CharField(max_length=100)
    Quantity = models.CharField(max_length=100)




class Customer(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobilenumber=models.BigIntegerField()
    place=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.BigIntegerField()

class Order(models.Model):
    DESIGN=models.ForeignKey(Design,on_delete=models.CASCADE)
    CUSTOMER_ID= models.ForeignKey(Customer,on_delete=models.CASCADE)
    date= models.DateField()
    status= models.CharField(max_length=100)
    totalamount= models.CharField(max_length=100)
    quantity=models.BigIntegerField()

class Customized_order(models.Model):
    CUSTOMER=models.ForeignKey(Customer, on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE)
    DIMENSION = models.ForeignKey(Diamension, on_delete=models.CASCADE)
    WOOD = models.ForeignKey(Wood, on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=100)


class Customized_payment(models.Model):
    CUSTOMIZED_ORDER = models.ForeignKey(Customized_order, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    date = models.DateField()
    status = models.CharField(max_length=100)

class Payment(models.Model):
    ORDER=models.ForeignKey(Order,on_delete=models.CASCADE)
    CUSTOMER_ID=models.ForeignKey(Customer,on_delete=models.CASCADE)
    price=models.BigIntegerField()
    date=models.DateField()
    status = models.CharField(max_length=100)

class review_and_rating(models.Model):
    CUSTOMER = models.ForeignKey(Customer,on_delete=models.CASCADE)
    DESIGN = models.ForeignKey(Design,on_delete=models.CASCADE)
    rating= models.CharField(max_length=100)
    review= models.CharField(max_length=100)
    date = models.DateField()






