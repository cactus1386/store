from django.db import models
from django.utils.translation import gettext as _
from random import choices

# Create your models here.
class product(models.Model):
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

# class bSecondLine(models.Model):
#     MOJOOD_LIST = {
#         ('موجود است','موجود'),
#         ("ناموجود است",'ناموجود'),
#     }
#     name = models.CharField(max_length=100)
#     description = models.CharField(_("توضیحات"), max_length=1000)
#     price = models.IntegerField()
#     second_price = models.IntegerField(default=price)
#     Discount = models.IntegerField(_("تخفیف"), default=0)
#     pub_date = models.DateField(_("تاریخ انتشار"), auto_now_add=True, auto_now=False)
#     photo = models.ImageField(upload_to='images/')
#     mojood = models.CharField(_('موجودی'), max_length=20, choices=MOJOOD_LIST, default='موجود است')
#     keifiat = models.IntegerField(_('کیفیت ساخت'), default=100)
#     arzesh = models.IntegerField(_('ارزش خرید'), default=100)
#     sohoolat = models.IntegerField(_('سهولت استفاده'), default=100)

#     def __str__(self):
#         return self.name

# class cThirdLine(models.Model):
#     MOJOOD_LIST = {
#         ('موجود است','موجود'),
#         ("ناموجود است",'ناموجود'),
#     }
#     name = models.CharField(max_length=100)
#     description = models.CharField(_("توضیحات"), max_length=1000)
#     price = models.IntegerField()
#     second_price = models.IntegerField(default=price)
#     Discount = models.IntegerField(_("تخفیف"), default=0)
#     pub_date = models.DateField(_("تاریخ انتشار"), auto_now_add=True, auto_now=False)
#     photo = models.ImageField(upload_to='images/')
#     mojood = models.CharField(_('موجودی'), max_length=20, choices=MOJOOD_LIST, default='موجود است')
#     keifiat = models.IntegerField(_('کیفیت ساخت'), default=100)
#     arzesh = models.IntegerField(_('ارزش خرید'), default=100)
#     sohoolat = models.IntegerField(_('سهولت استفاده'), default=100)

#     def __str__(self):
#         return self.name
    
    
# class dfourthline(models.Model):
#     MOJOOD_LIST = {
#         ('موجود است','موجود'),
#         ("ناموجود است",'ناموجود'),
#     }
#     name = models.CharField(max_length=100)
#     description = models.CharField(_("توضیحات"), max_length=1000)
#     price = models.IntegerField()
#     second_price = models.IntegerField(default=price)
#     Discount = models.IntegerField(_("تخفیف"), default=0)
#     pub_date = models.DateField(_("تاریخ انتشار"), auto_now_add=True, auto_now=False)
#     photo = models.ImageField(upload_to='images/')
#     mojood = models.CharField(_('موجودی'), max_length=20, choices=MOJOOD_LIST, default='موجود است')
#     keifiat = models.IntegerField(_('کیفیت ساخت'), default=100)
#     arzesh = models.IntegerField(_('ارزش خرید'), default=100)
#     sohoolat = models.IntegerField(_('سهولت استفاده'), default=100)

#     def __str__(self):
#         return self.name

# class eFifthLine(models.Model):
#     MOJOOD_LIST = {
#         ('موجود است','موجود'),
#         ("ناموجود است",'ناموجود'),
#     }
#     name = models.CharField(max_length=100)
#     description = models.CharField(_("توضیحات"), max_length=1000)
#     price = models.IntegerField()
#     second_price = models.IntegerField(default=price)
#     Discount = models.IntegerField(_("تخفیف"), default=0)
#     pub_date = models.DateField(_("تاریخ انتشار"), auto_now_add=True, auto_now=False)
#     photo = models.ImageField(upload_to='images/')
#     mojood = models.CharField(_('موجودی'), max_length=20, choices=MOJOOD_LIST, default='موجود است')
#     keifiat = models.IntegerField(_('کیفیت ساخت'), default=100)
#     arzesh = models.IntegerField(_('ارزش خرید'), default=100)
#     sohoolat = models.IntegerField(_('سهولت استفاده'), default=100)

#     def __str__(self):
#         return self.name

# class fSixthLine(models.Model):
#     MOJOOD_LIST = {
#         ('موجود است','موجود'),
#         ("ناموجود است",'ناموجود'),
#     }
#     name = models.CharField(max_length=100)
#     description = models.CharField(_("توضیحات"), max_length=1000)
#     price = models.IntegerField()
#     second_price = models.IntegerField(default=price)
#     Discount = models.IntegerField(_("تخفیف"), default=0)
#     pub_date = models.DateField(_("تاریخ انتشار"), auto_now_add=True, auto_now=False)
#     photo = models.ImageField(upload_to='images/')
#     mojood = models.CharField(_('موجودی'), max_length=20, choices=MOJOOD_LIST, default='موجود است')
#     keifiat = models.IntegerField(_('کیفیت ساخت'), default=100)
#     arzesh = models.IntegerField(_('ارزش خرید'), default=100)
#     sohoolat = models.IntegerField(_('سهولت استفاده'), default=100)

#     def __str__(self):
#         return self.name

# class gseventhLine(models.Model):
#     MOJOOD_LIST = {
#         ('موجود است','موجود'),
#         ("ناموجود است",'ناموجود'),
#     }
#     name = models.CharField(max_length=100)
#     description = models.CharField(_("توضیحات"), max_length=1000)
#     price = models.IntegerField()
#     second_price = models.IntegerField(default=price)
#     Discount = models.IntegerField(_("تخفیف"), default=0)
#     pub_date = models.DateField(_("تاریخ انتشار"), auto_now_add=True, auto_now=False)
#     photo = models.ImageField(upload_to='images/')
#     mojood = models.CharField(_('موجودی'), max_length=20, choices=MOJOOD_LIST, default='موجود است')
#     keifiat = models.IntegerField(_('کیفیت ساخت'), default=100)
#     arzesh = models.IntegerField(_('ارزش خرید'), default=100)
#     sohoolat = models.IntegerField(_('سهولت استفاده'), default=100)
    
#     def __str__(self):
#         return self.name


# class heightLine(models.Model):
#     MOJOOD_LIST = {
#         ('موجود است','موجود'),
#         ("ناموجود است",'ناموجود'),
#     }
#     name = models.CharField(max_length=100)
#     description = models.CharField(_("توضیحات"), max_length=1000)
#     price = models.IntegerField()
#     second_price = models.IntegerField(default=price)
#     Discount = models.IntegerField(_("تخفیف"), default=0)
#     pub_date = models.DateField(_("تاریخ انتشار"), auto_now_add=True, auto_now=False)
#     photo = models.ImageField(upload_to='images/')
#     mojood = models.CharField(_('موجودی'), max_length=20, choices=MOJOOD_LIST, default='موجود است')
#     keifiat = models.IntegerField(_('کیفیت ساخت'), default=100)
#     arzesh = models.IntegerField(_('ارزش خرید'), default=100)
#     sohoolat = models.IntegerField(_('سهولت استفاده'), default=100)
    
#     def __str__(self):
#         return self.name
