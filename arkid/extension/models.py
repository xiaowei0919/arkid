from django.db import models
from arkid.common.model import BaseModel
from django.utils.translation import gettext_lazy as _


class Extension(BaseModel):

    class Meta(object):
        verbose_name = _("插件")
        verbose_name_plural = _("插件")

    type = models.CharField(max_length=64, default="base", verbose_name=_('类型'))
    labels = models.CharField(max_length=128, verbose_name=_('标签'))
    package = models.CharField(max_length=128, verbose_name=_('标识'), unique=True)
    ext_dir = models.CharField(max_length=1024, verbose_name=_('完整路径名'))
    name = models.CharField(max_length=128, verbose_name=_('名称'))
    version = models.CharField(max_length=128, verbose_name=_('版本'))
    is_active = models.BooleanField(default=False, verbose_name=_('是否启用'))
    is_allow_use_platform_config = models.BooleanField(default=False, verbose_name=_('是否允许租户启用平台配置'))


class TenantExtension(BaseModel):
    tenant = models.ForeignKey('core.Tenant', blank=False, on_delete=models.PROTECT, verbose_name=_('租户'))
    extension = models.ForeignKey('Extension', blank=False, on_delete=models.PROTECT, verbose_name=_('插件'))
    is_active = models.BooleanField(default=False, verbose_name=_('是否启用'))
    # 如果启用平台配置，运行时，平台租户的配置将会被添加到该租户的配置中
    use_platform_config = models.BooleanField(default=False, verbose_name=_('是否启用平台配置'))


class TenantExtensionConfig(BaseModel):

    class Meta(object):
        verbose_name = _("租户插件配置")
        verbose_name_plural = _("租户插件配置")

    tenant = models.ForeignKey('core.Tenant', blank=False, on_delete=models.PROTECT, verbose_name=_('租户'))
    extension = models.ForeignKey('Extension', blank=False, on_delete=models.PROTECT, verbose_name=_('插件'))
    config = models.JSONField(blank=True, default=dict, verbose_name=_('配置'))
