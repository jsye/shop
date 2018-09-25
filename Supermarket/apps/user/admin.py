"""
    user & supermarket 后台功能注册

"""

from django.contrib import admin

from user.models import Usermodel, Goods_cla, Goods_SKU, Goods_SPU, Goods_Photo, Goods_Unit, IndexFlashImg, IndexActive, \
    IndexZone, IndexZoneActive, CartInfo, Pays, CartCommodity, CartTransport, CartAddress


@admin.register(Usermodel)
class UserAdmin(admin.ModelAdmin):
    """
        用户
    """
    pass


@admin.register(Goods_cla)
class GoodsClassAdmin(admin.ModelAdmin):
    """
        商品分类
    """
    pass


@admin.register(Goods_SKU)
class GoodsSkuAdmin(admin.ModelAdmin):
    """
        商品SKU表
    """
    pass


@admin.register(Goods_SPU)
class GoodsSpuAdmin(admin.ModelAdmin):
    """
        商品SPU表
    """
    pass


@admin.register(Goods_Photo)
class GoodsPhotoAdmin(admin.ModelAdmin):
    """
        商品相册
    """
    pass


@admin.register(Goods_Unit)
class GoodsUnitAdmin(admin.ModelAdmin):
    """
        商品单位表
    """
    pass


@admin.register(IndexFlashImg)
class IndexFlashImgAdmin(admin.ModelAdmin):
    """
        首页轮播商品表
    """
    pass


@admin.register(IndexActive)
class IndexActiveAdmin(admin.ModelAdmin):
    """
        首页活动表
    """
    pass


@admin.register(IndexZone)
class IndexZoneAdmin(admin.ModelAdmin):
    """
        首页活动专区
    """
    pass


@admin.register(IndexZoneActive)
class IndexZoneActiveAdmin(admin.ModelAdmin):
    """
        首页专区活动商品表
    """
    pass


@admin.register(CartInfo)
class CartInfoActiveAdmin(admin.ModelAdmin):
    """
        订单信息
    """
    pass


@admin.register(Pays)
class PaysAdmin(admin.ModelAdmin):
    """
        支付方式
    """
    pass


@admin.register(CartCommodity)
class CartCommodityAdmin(admin.ModelAdmin):
    """
        订单商品表
    """
    pass


@admin.register(CartTransport)
class CartTransportAdmin(admin.ModelAdmin):
    """
        运输方式
    """
    pass


@admin.register(CartAddress)
class AddressAdmin(admin.ModelAdmin):
    """
        收费地址
    """
    pass
