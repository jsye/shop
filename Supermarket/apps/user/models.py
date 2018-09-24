"""
this is user models
                    --by zero

"""
from django.core import validators
from django.db import models

from user.helper import BaseModel

"""
this is usermodel table 

"""


class Usermodel(models.Model):
    sex_list = ((1, '男'),
                (2, '女'),
                (3, '保密'))
    name = models.CharField(max_length=20, null=True, blank=True,
                            verbose_name="妮称")

    mobile = models.CharField(max_length=11,
                              validators=[
                                  validators.RegexValidator(r'^1[3-9]\d{9}$', "手机号码格式错误"),
                                  validators.MinLengthValidator(11)
                              ],
                              verbose_name="手机号码")

    password = models.CharField(max_length=64, verbose_name='密码',
                                validators=[
                                    validators.MinLengthValidator(8)
                                ])

    sex = models.IntegerField(choices=sex_list, default=3, verbose_name='性别', null=True, blank=True)

    bthday = models.DateField(verbose_name='生日', null=True, blank=True)

    school = models.CharField(max_length=100, verbose_name='学校', null=True, blank=True,
                              editable=True)

    address = models.CharField(max_length=200, verbose_name='地址', editable=True,
                               null=True, blank=True)
    fromshome = models.CharField(max_length=100, verbose_name='故乡', null=True, blank=True)

    add_date = models.DateTimeField(verbose_name='添加时间', null=True, blank=True)

    update_date = models.DateTimeField(verbose_name='修改时间', null=True, blank=True)

    delete = models.BooleanField(default=False, verbose_name='删除')

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.mobile


"""
this is goods table 

"""


# 商品分类
class Goods_cla(BaseModel):
    # cla_id = models.SmallIntegerField(verbose_name="商品分类id")  # 注：这个字段orm 自动创建
    cla_name = models.CharField(verbose_name="商品分类名", max_length=100)
    cla_info = models.CharField(verbose_name="商品分类简介", max_length=200)

    def __str__(self):
        return self.cla_name

    class Mete:
        db_table = "Goods_cla"


# 商品SKU表
class Goods_SKU(BaseModel):
    # sku_id = models.SmallIntegerField(verbose_name="sku_id")   # 注：这个字段orm 自动创建
    sku_name = models.CharField(verbose_name="商品名", max_length=100)
    sku_info = models.CharField(verbose_name="商品简介", max_length=100)
    sku_price = models.DecimalField(verbose_name="商品价格", max_digits=None, decimal_places=3)
    sku_unit = models.ForeignKey(to='Goods_Unit', related_name='pk', on_delete=models.CASCADE, verbose_name="商品单位")
    sku_reserve = models.IntegerField(verbose_name="商品库存", max_length=10)
    sku_sales = models.IntegerField(verbose_name="销量", max_length=10)
    sku_logo = models.ImageField(verbose_name="logo", default=None)
    sku_Shelf = models.BooleanField(verbose_name="是否上架", default=False)
    sku_cla_id = models.ForeignKey(to='Goods_cla', related_name='pk', on_delete=models.CASCADE, verbose_name="商品分类ID")
    sku_spu_id = models.ForeignKey(to='Goods_SPU', related_name='pk', on_delete=models.CASCADE, verbose_name="商品SPU_ID")

    def __str__(self):
        return self.sku_name

    class Meta:
        db_table = "Goods_SKU"


#  商品SPU表
class Goods_SPU(models.Model):
    # spu_id = models.SmallIntegerField(verbose_name="商品spu_id")  #  注:这个由orm自动创建
    spu_name = models.CharField(verbose_name="商品SPU_name", max_length=50)
    spu_info = models.CharField(verbose_name="商品简介", max_length=100)

    def __str__(self):
        return self.spu_name

    class Meta:
        db_table = "Goods_SPU"


# 商品相册
class Goods_Photo(BaseModel):
    # photo_id = models.SmallIntegerField(verbose_name="商品相册ID")  # 注：些ID 由orm自动创建
    photo_goods_img = models.ImageField(verbose_name="商品图片", default=None)
    photo_goods_skuid = models.ForeignKey(to='Goods_SKU', related_name='pk', on_delete=models.CASCADE,
                                          verbose_name="商品SKU_ID")

    class Meta:
        db_table = "Goods_Photo"

    def __str__(self):
        return self.pk


# 商品单位表
class Goods_Unit(BaseModel):
    Goods_unit = ((0, ''), (1, '斤'), (2, '箱'), (3, '件'), (4, '条'), (5, '套'))

    # unit_goods_id = models.SmallIntegerField(verbose_name="商品单位id")  # 由orm自动创建
    unit_goods_unit = models.SmallIntegerField(verbose_name="商品单位", choices=Goods_unit, default=0)

    class Meta:
        db_table = "Goods_Unit"

    def __str__(self):
        return self.unit_goods_unit
