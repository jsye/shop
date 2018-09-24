import hashlib
from django.db import models


# 此函数为加密函数
def set_password(pwd):
    h = hashlib.md5(pwd.encode('utf-8'))
    return h.hexdigest()


class BaseModel(models.Model):
    """
        只能被继承的类
    """
    create_time = models.DateTimeField(verbose_name="创建时间",
                                       auto_now_add=True,
                                       )
    update_time = models.DateTimeField(verbose_name="更新时间",
                                       auto_now=True,
                                       )
    is_delete = models.BooleanField(verbose_name="是否删除",
                                    default=False,
                                    )

    class Meta:
        # 说明是一个抽象模型类
        abstract = True
