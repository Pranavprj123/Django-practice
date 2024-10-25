from django.db import models
from autoslug import AutoSlugField
class HsnCode(models.Model):
    index = models.BigAutoField(primary_key=True)
    item_code = models.BigIntegerField(verbose_name='Item Code',null=True) 
    item_name = models.TextField(verbose_name='Item Name',null=True) 
    item_type = models.TextField(verbose_name='Item Type',null=True) 
    GSTe = models.DecimalField(max_digits=5,decimal_places=2,verbose_name=r'GST %e',null=True)
    hsn_code = models.BigIntegerField(max_length=10,default=True)
    GST = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='GST %',null=True)
    class Meta:
        db_table = 'HSN_CODE'
    def __str__(self) -> str:
        return f'{self.item_code}-{self.GSTe}%--{self.hsn_code}--{self.GST}'

TYPE_CHOICE = [
    ('CPB','Corporate branding'),
    ('PSB','Personal branding'),
    ('PB',' Product branding'),
    ('RB','Retail branding'),
    ('GPB','Geographic branding'),
    ('SB','Service branding'),
]
class Brand(models.Model):
    logo = models.ImageField(upload_to='images/brand/logo')
    name = models.CharField(max_length=20)
    tagline = models.CharField(max_length=50)
    since  = models.DateField()
    types =  models.CharField(max_length=20,choices=TYPE_CHOICE)
    origin  = models.CharField(max_length=30)
    def __str__(self) -> str:
        return f'{self.name} "{self.tagline}" {self.since}'
    class Meta:
        db_table = 'Brand'


class Product(models.Model):    
    name = models.CharField(max_length=50)  
    slug = AutoSlugField(populate_from='name', unique=True)
    def slugify_function(self, content):
        return content.replace('_', '-').lower()
    price_inclusive = models.DecimalField(decimal_places=2,max_digits=10)
    description = models.TextField(default='default Description')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    gst_rate = models.DecimalField(max_digits=5,decimal_places=2,default=5.00)
    hsn_code = models.CharField(max_length=10,default='default',blank=True)
    quantity =  models.IntegerField(default=1)
    features = models.JSONField(blank=True)
    # def save(self,commit=False):
    #     data = get_object_or_404(HsnCode,item_code=self.hsn_code)
    #     if (data):
    #         self.gst_rate = data.GSTe
    #     super().save()
    @property
    def price_exclusive(self):
        return self.price_inclusive / (1 + (self.gst_rate / 100))
    @property
    def gst_amount(self):
        return self.price_inclusive - self.price_exclusive
    
    def __str__(self):
        return f'({self.name}) from {self.brand.name}'
    # image = models.ImageField(upload_to='products/')
    class Meta:
        db_table = 'Product'

class ProductImages(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/product/images')
    def __str__(self) -> str:
        return f'image of {self.product.name}'
    class Meta:
        db_table = 'Product_Images'


class Category(models.Model):
    name = models.CharField(max_length=20,unique=True)
    description = models.CharField(max_length=70)
    product = models.ManyToManyField(Product)
    class Meta:
        db_table = 'Category'
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.description}'
        