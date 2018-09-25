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

# 用户信息表
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
    headimg = models.ImageField(upload_to='shop/%Y%m/%d', default='default/shop1.png', verbose_name="用户头像")

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
        # 后台显示的名称
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

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

    class Meta:
        db_table = "Goods_cla"
        # 后台显示的名称
        verbose_name = "商品分类"
        verbose_name_plural = verbose_name


# 商品SKU表
class Goods_SKU(BaseModel):
    # sku_id = models.SmallIntegerField(verbose_name="sku_id")   # 注：这个字段orm 自动创建
    sku_name = models.CharField(verbose_name="商品名", max_length=100)
    sku_info = models.CharField(verbose_name="商品简介", max_length=100)
    sku_price = models.DecimalField(verbose_name="商品价格", max_digits=10, decimal_places=3)
    sku_unit = models.ForeignKey(to='Goods_Unit', related_name='pk', on_delete=models.CASCADE, verbose_name="商品单位")
    sku_reserve = models.IntegerField(verbose_name="商品库存")
    sku_sales = models.IntegerField(verbose_name="销量")
    sku_logo = models.ImageField(verbose_name="logo", default=None)
    sku_Shelf = models.BooleanField(verbose_name="是否上架", default=False)
    sku_cla_id = models.ForeignKey(to='Goods_cla', related_name='pk', on_delete=models.CASCADE, verbose_name="商品分类ID")
    sku_spu_id = models.ForeignKey(to='Goods_SPU', related_name='pk', on_delete=models.CASCADE, verbose_name="商品SPU_ID")

    def __str__(self):
        return self.sku_name

    class Meta:
        db_table = "Goods_SKU"
        # 后台显示的名称
        verbose_name = "商品SKU表"
        verbose_name_plural = verbose_name


#  商品SPU表
class Goods_SPU(models.Model):
    # spu_id = models.SmallIntegerField(verbose_name="商品spu_id")  #  注:这个由orm自动创建
    spu_name = models.CharField(verbose_name="商品SPU_name", max_length=50)
    spu_info = models.TextField(verbose_name="商品详情", max_length=100)

    def __str__(self):
        return self.spu_name

    class Meta:
        db_table = "Goods_SPU"
        # 后台显示的名称
        verbose_name = "商品SPU表"
        verbose_name_plural = verbose_name


# 商品相册
class Goods_Photo(BaseModel):
    # photo_id = models.SmallIntegerField(verbose_name="商品相册ID")  # 注：些ID 由orm自动创建
    photo_goods_img = models.ImageField(verbose_name="商品图片", default=None)
    photo_goods_skuid = models.ForeignKey(to='Goods_SKU', related_name='pk', on_delete=models.CASCADE,
                                          verbose_name="商品SKU_ID")

    class Meta:
        db_table = "Goods_Photo"
        #  后台显示名称
        verbose_name = "商品相册"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pk




# 商品单位表
class Goods_Unit(BaseModel):
    Goods_unit = ((0, ''), (1, '斤'), (2, '箱'), (3, '件'), (4, '条'), (5, '套'))

    # unit_goods_id = models.SmallIntegerField(verbose_name="商品单位id")  # 由orm自动创建
    unit_goods_unit = models.SmallIntegerField(verbose_name="商品单位", choices=Goods_unit, default=0)

    class Meta:
        db_table = "Goods_Unit"
        #  后台显示名称
        verbose_name = "商品单位表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.unit_goods_unit


"""
  首页轮播图
"""


# 首页轮播商品表

class IndexFlashImg(BaseModel):
    flashName = models.CharField(verbose_name="首页轮播商品", max_length=50)
    goods = models.CharField(verbose_name="商品", max_length=50)
    img = models.ImageField(verbose_name="图片URL")
    order = models.SmallIntegerField(verbose_name="排序")

    def __str__(self):
        return self.flashName

    class Meta:
        db_table = 'IndexFlashImg'
        #  后台显示名称
        verbose_name = "首页轮播商品表"
        verbose_name_plural = verbose_name


# 首页活动表

class IndexActive(models.Model):
    name = models.CharField(verbose_name="活动名称", max_length=100)
    img = models.ImageField(verbose_name="活动商品图片")
    urladdr = models.URLField(verbose_name="活动url")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "IndexActive"
        #  后台显示名称
        verbose_name = "首页活动表"
        verbose_name_plural = verbose_name


# 首页活动专区

class IndexZone(BaseModel):
    ZoneName = models.CharField(verbose_name="活动专区名称", max_length=50)
    ZoneInfo = models.CharField(verbose_name="活动专区简介", max_length=200)
    order = models.SmallIntegerField(verbose_name="排序")
    Shelf = models.BooleanField(verbose_name="是否上架", default=False)

    def __str__(self):
        return self.ZoneName

    class Meta:
        db_table = 'IndexZone'
        #  后台显示名称
        verbose_name = "首页活动专区"
        verbose_name_plural = verbose_name


# 首页专区活动商品表

class IndexZoneActive(BaseModel):
    ZoneId = models.ForeignKey(to='IndexZone', on_delete=models.CASCADE, verbose_name="专区ID")
    skuId = models.ForeignKey(to='Goods_Photo', verbose_name='专区商品skuid')

    def __str__(self):
        return self.pk

    class Meta:
        db_table = 'IndexZoneActive'
        #  后台显示名称
        verbose_name = "首页专区活动商品表"
        verbose_name_plural = verbose_name

"""
    订单信息表
"""


# 订单信息
class CartInfo(BaseModel):
    status_list = ((0, '待付款'),
                   (1, '退发货'),
                   (2, '待收货'),
                   (3, '待评价'),
                   (4, '已完成'))
    number = models.SmallIntegerField(verbose_name="订单编号")
    money = models.DecimalField(verbose_name="订单金额", max_digits=10, decimal_places=2)
    userId = models.CharField(verbose_name="用户ID", max_length=50)
    ReceiptUser = models.CharField(verbose_name="收货人姓名", max_length=20)
    phone = models.CharField(verbose_name="手机号码", max_length=11,
                             validators=[
                                 validators.MinLengthValidator(11),
                                 validators.RegexValidator(r'^1[3-9]\d{9}$', '手机号码格式错误！')
                             ])
    address = models.CharField(verbose_name="收货地址", max_length=200)
    status = models.BooleanField(verbose_name="收货状态", choices=status_list)
    transport = models.ForeignKey(to='CartTransport', verbose_name="运输方式")
    pay = models.ForeignKey(to='Pays', verbose_name="付款方式")
    cash = models.DecimalField(verbose_name="实付金额", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.status

    class Meta:
        db_table = "CartInfo"
        #  后台显示名称
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name


# 支付方式

class Pays(BaseModel):
    name = models.CharField(max_length=20, verbose_name="名称")
    photo = models.ImageField(verbose_name="图片")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Pays"
        #  后台显示名称
        verbose_name = "支付方式"
        verbose_name_plural = verbose_name


# 订单商品表
class CartCommodity(models.Model):
    CartId = models.ForeignKey(to="CartInfo", verbose_name="订单ID")
    CartSkuId = models.ForeignKey(to='Goods_Photo', verbose_name="商品SKUID")
    CartNumber = models.SmallIntegerField(verbose_name="商品数量")
    CartPrice = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="商品价格")

    def __str__(self):
        return self.CartSkuId

    class Meta:
        db_table = 'CartCommodity'
        #  后台显示名称
        verbose_name = "订单商品表"
        verbose_name_plural = verbose_name

# 运输方式

class CartTransport(BaseModel):
    name = models.CharField(verbose_name="运输名称", max_length=100)
    TPrice = models.DecimalField(verbose_name="动费", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'CartTransport'
        #  后台显示名称
        verbose_name = "运输方式"
        verbose_name_plural = verbose_name


#  收费地址
class CartAddress(BaseModel):
    userID = models.CharField(verbose_name="用户ID", max_length=20)
    name = models.CharField(verbose_name="收货人姓名", max_length=20)
    phone = models.CharField(verbose_name='手机号码', max_length=11,
                             validators=[
                                 validators.MinLengthValidator(11),
                                 validators.RegexValidator(r'^1[3-9]\d{9}$', '手机号码格式错误！')
                             ])
    address = models.ForeignKey(to='CartInfo', verbose_name="详细地址")
    defaultAddr = models.BooleanField(verbose_name="设置默认地址", default=False)

    def __str__(self):
        return self.userID

    class Meta:
        db_table = 'CartAddress'
        #  后台显示名称
        verbose_name = "收费地址"
        verbose_name_plural = verbose_name

