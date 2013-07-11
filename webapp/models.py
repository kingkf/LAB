from django.db import models

# Create your models here.
class Group_Primary_Table(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    onesentence = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    weibosite = models.URLField(blank=True, null=True)
    renrensite = models.URLField(blank=True, null=True)
    doubansite = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to = 'group_logo/')
    '''class Meta:
        ordering = ['name']'''
    def __unicode__(self):
        return self.name

class Incubator_Primary_Table(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    onesentence = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    weibosite = models.URLField(blank=True, null=True)
    renrensite = models.URLField(blank=True, null=True)
    tencentsite = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to = 'incubator_logo/')
    '''class Meta:
        ordering = ['name']'''
    def __unicode__(self):
        return self.name

class Product_Primary_Table(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    onesentence = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    weibosite = models.URLField(blank=True, null=True) 
    renrensite = models.URLField(blank=True, null=True) 
    doubansite = models.URLField(blank=True, null=True) 
    downloadsite = models.URLField(blank=True, null=True) 
    downloadtime = models.IntegerField(max_length=100) 
    logo = models.ImageField(upload_to = 'product_logo/') 
    '''class Meta:
        ordering = ['name']'''
    def __unicode__(self):
        return self.name

class Group_Pic_Table(models.Model):
    group = models.ForeignKey(Group_Primary_Table)
    pic = models.ImageField(upload_to = 'group_pic/') 
    '''class Meta:
        ordering = ['pic']'''
    def __unicode__(self):
        return self.pic

class Incubator_Pic_Table(models.Model):
    incubator = models.ForeignKey(Incubator_Primary_Table)
    pic = models.ImageField(upload_to = 'incubator_pic/') 
    '''class Meta:
        ordering = ['pic']'''
    def __unicode__(self):
        return self.pic

class Group_Product_Table(models.Model):
    group = models.ForeignKey(Group_Primary_Table)
    product = models.ForeignKey(Product_Primary_Table) 
    '''class Meta:
        ordering = ['group']'''
    def __unicode__(self):
        return self.product
        
class Group_Information_Table(models.Model):
    group = models.ForeignKey(Group_Primary_Table)
    manager = models.CharField(max_length=100)
    establish_date = models.DateField()
    range = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    scale = models.IntegerField(max_length=100)
    phone = models.IntegerField(max_length=100)
    email = models.EmailField(max_length=40)
    barcode = models.ImageField(upload_to = 'group_barcode/')
    '''class Meta
        ordering = ['establish_date']'''
    def __unicode__(self):
        return self.group

class Incubator_Information_Table(models.Model):
    incubator = models.ForeignKey(Incubator_Primary_Table)
    resourece = models.CharField(max_length=500)
    qqnum = models.IntegerField(max_length=100)
    phone = models.IntegerField(max_length=100)
    email = models.EmailField(max_length=40)
    barcode = models.ImageField(upload_to = 'incubator_barcode/')
    '''class Meta
        ordering = ['establish_date']'''
    def __unicode__(self):
        return self.incubator

class Product_Pic_Table(models.Model):
    product = models.ForeignKey(Product_Primary_Table) 
    pic = models.ImageField(upload_to = 'product_pic/') 
    '''class Meta:
        ordering = ['pic']'''
    def __unicode__(self):
        return self.pic

class Product_Information_Table(models.Model):
    product = models.ForeignKey(Product_Primary_Table)
    group = models.ForeignKey(Group_Primary_Table)
    type = models.CharField(max_length=100)
    version = models.CharField(max_length=100) 
    online_date = models.DateField()
    update_date = models.DateField() 
    requiresystem = models.CharField(max_length=100) 
    language = models.CharField(max_length=100) 
    size = models.IntegerField(max_length=100)
    barcode = models.ImageField(upload_to = 'product_barcode/')
    '''class Meta:
        ordering = ['update_date']'''
    def __unicode__(self):
        return self.product

class hotbanner(models.Model):
    
    """docstring for hotbanner
    def __init__(self, arg):
        super(hotbanner, self).__init__()
        self.arg = arg"""
        
