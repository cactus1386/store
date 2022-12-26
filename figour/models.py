from random import choices
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class fpfigours(models.Model):
    MOJOOD_LIST = {
        ('موجود است','موجود'),
        ("ناموجود است",'ناموجود'),
    }
    name = models.CharField(max_length=100)
    description = models.CharField(_("توضیحات"), max_length=1000)
    price = models.IntegerField()
    second_price = models.IntegerField(default=price)
    Discount = models.IntegerField(_("تخفیف"), default=0)
    pub_date = models.DateField(_("تاریخ انتشار"), auto_now_add=True, auto_now=False)
    photo = models.ImageField(upload_to='images/')
    mojood = models.CharField(_('موجودی'), max_length=20, choices=MOJOOD_LIST, default='موجود است')
    keifiat = models.IntegerField(_('کیفیت ساخت'), default=100)
    arzesh = models.IntegerField(_('ارزش خرید'), default=100)
    sohoolat = models.IntegerField(_('سهولت استفاده'), default=100)
    
    def __str__(self):
        return self.name
    
class comments(models.Model):
    figour = models.ForeignKey('fpfigours', verbose_name=_('محصول'), related_name='comments' ,on_delete=models.CASCADE)
    name = models.CharField(_('نام کاربر'), max_length=50)
    email = models.EmailField(max_length=255)
    massage = models.TextField()
    date = models.DateField(_('تاریخ انتشار'), auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.name
    
class about(models.Model):
    lorem1 = models.TextField(_("متن اول"))
    lorem2 = models.TextField(_("متن دوم"))   
    lorem3 = models.TextField(_("متن سوم")) 
    lorem4 = models.TextField(_("متن چهارم"))
    image = models.ImageField(upload_to='images/')
    
    

class fpporforoosh(models.Model):
    MOJOOD_LIST = {
        ('موجود است','موجود'),
        ("ناموجود است",'ناموجود'),
    }
    name = models.CharField(max_length=100)
    description = models.CharField(_("توضیحات"), max_length=1000)
    price = models.IntegerField()
    second_price = models.IntegerField(default=price)
    Discount = models.IntegerField(_("تخفیف"), default=0)
    pub_date = models.DateField(_("تاریخ انتشار"), auto_now_add=True, auto_now=False)
    photo = models.ImageField(upload_to='images/')
    mojood = models.CharField(_('موجودی'), max_length=20, choices=MOJOOD_LIST, default='موجود است')
    keifiat = models.IntegerField(_('کیفیت ساخت'), default=100)
    arzesh = models.IntegerField(_('ارزش خرید'), default=100)
    sohoolat = models.IntegerField(_('سهولت استفاده'), default=100)
    
    def __str__(self):
        return self.name
