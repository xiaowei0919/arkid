from rest_framework import views
from ..serializers import loginpage as lp
from common import loginpage as model
from openapi.utils import extend_schema
from django.http.response import JsonResponse
from api.v1.views.login import (
    LoginView,
    MobileLoginView,
    UserNameRegisterView,
    MobileRegisterView,
)
from api.v1.views.tenant import TenantViewSet
from tenant.models import Tenant, TenantConfig
from external_idp.models import ExternalIdp
from api.v1.serializers.tenant import TenantExtendSerializer
from system.models import SystemConfig


@extend_schema(tags=['login page'])
class LoginPage(views.APIView):
    @extend_schema(responses=lp.LoginPagesSerializer)
    def get(self, request):
        tenant_uuid = request.query_params.get('tenant', None)
        tenant = Tenant.objects.filter(uuid=tenant_uuid).first()

        data = model.LoginPages()
        if tenant:
            data.setTenant(TenantExtendSerializer(instance=tenant).data)

            # 获取 tenant的登录注册配置
            tenant_config = TenantConfig.objects.get(
                is_del=False,
                tenant=tenant,
            )
            if not tenant_config:
                mobile_login_register_enabled = (True,)
                secret_login_register_enabled = (True,)
                secret_login_register_field_names = ['username', 'email']
            else:
                mobile_login_register_enabled = tenant_config.data.get(
                    'mobile_login_register_enabled', True
                )
                secret_login_register_enabled = tenant_config.data.get(
                    'secret_login_register_enabled', True
                )
                secret_login_register_field_names = tenant_config.data.get(
                    'secret_login_register_field_names', ['username', 'email']
                )

            if mobile_login_register_enabled:
                data.addForm(
                    model.LOGIN, TenantViewSet().mobile_login_form(tenant_uuid)
                )
                data.addForm(
                    model.REGISTER, TenantViewSet().mobile_register_form(tenant_uuid)
                )
            if secret_login_register_enabled:
                data.addForm(
                    model.LOGIN,
                    TenantViewSet().native_field_login_form(
                        request, tenant_uuid, secret_login_register_field_names
                    ),
                )
            for field_name in secret_login_register_field_names:
                data.addForm(
                    model.REGISTER,
                    TenantViewSet().native_field_register_form(tenant_uuid, field_name),
                )

            external_idps = ExternalIdp.valid_objects.filter(tenant=tenant)
            for idp in external_idps:
                if idp.type not in ['miniprogram']:
                    data.addExtendButton(
                        model.LOGIN,
                        model.Button(
                            img=idp.data['img_url'],
                            tooltip=idp.type,
                            redirect=model.ButtonRedirect(
                                url=idp.data['login_url'],
                            ),
                        ),
                    )
            if data.getPage(model.LOGIN) and data.getPage(model.LOGIN).get(
                'extend', None
            ):
                data.setExtendTitle(model.LOGIN, '第三方登录')
        else:
            data.addForm(model.LOGIN, LoginView().login_form())
            data.addForm(model.LOGIN, MobileLoginView().login_form())
            system_config = self.get_system_config()
            is_open_register = system_config.get('is_open_register', True)
            if is_open_register == True:
                data.addForm(
                    model.REGISTER, UserNameRegisterView().username_register_form()
                )
                data.addForm(
                    model.REGISTER, MobileRegisterView().mobile_register_form()
                )

        if data.getPage(model.REGISTER):
            data.addBottom(
                model.LOGIN,
                model.Button(prepend='还没有账号，', label='立即注册', gopage=model.REGISTER),
            )
            data.addBottom(
                model.REGISTER,
                model.Button(prepend='已有账号，', label='立即登录', gopage=model.LOGIN),
            )

        if data.getPage(model.LOGIN):
            data.addBottom(model.LOGIN, model.Button(label='忘记密码', gopage='password'))

        pages = lp.LoginPagesSerializer(data=data)
        pages.is_valid()
        return JsonResponse(pages.data)

    def get_system_config(self):
        # 获取基础配置信息
        result = {'is_open_register': True}
        systemconfig = SystemConfig.active_objects.first()
        if systemconfig:
            result = systemconfig.data
        return result
