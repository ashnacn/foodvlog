from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    cat_name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    class Meta:
        ordering=('cat_name',)
        verbose_name='Category'
        verbose_name_plural='Categories'
    def get_url(self):
        return reverse('prod_cat',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.cat_name)
class Product(models.Model):
    P_name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    P_desc=models.TextField()
    P_price=models.IntegerField()
    P_stock=models.IntegerField()
    P_available=models.BooleanField()
    P_image=models.ImageField(upload_to='Product')
    P_category=models.ForeignKey(Category,on_delete= models.CASCADE)
    def get_url(self):
        return reverse('details',args=[self.P_category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.P_name)