from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15),
                                                       MaxValueValidator(100)],
                                           null=True, blank=True)
    phone_number = PhoneNumberField()
    STATUS_CHOICES = (
        ('gold', 'Gold'), #75%
        ('silver', 'Silver'), #50%
        ('bronze', 'Bronze'), #25%
        ('simple', 'Simple'), #0%
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='simple')
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, '

class Category(models.Model):
    category_image = models.ImageField(upload_to='category_images')
    category_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_sub')
    sub_category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_category_name

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, verbose_name="Название")
    price = models.PositiveIntegerField()
    article_number = models.PositiveIntegerField(unique=True)
    description = models.TextField()
    video = models.FileField(upload_to='product_video', null=True, blank=True)
    product_type = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    def get_avg_rating(self):
        review = self.product_reviews.all()
        if review.exists():
            return round(sum([i.stars for i in review]) / review.count(), 1)
        return 0

    def get_count_people(self):
        return self.product_reviews.count()

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return f'{self.product}, {self.image},'

class ReView(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_reviews')
    text = models.TextField()
    stars = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.product}'

class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)