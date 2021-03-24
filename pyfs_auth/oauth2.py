# -*- coding: utf-8 -*-

from pyfs_base import BaseFeishu
from .app_access_token import AppAccessToken, final_app_access_token


class OAuth2(BaseFeishu):
    def __init__(self, appid=None, secret=None, ticket=None, tenant_key=None, token=None, storage=None):
        super(Authen, self).__init__(appid=appid, secret=secret, ticket=ticket, tenant_key=tenant_key, token=token, storage=storage)
        # 移动应用接入 - 接入流程, Refer: https://open.feishu.cn/document/uAjLw4CM/uYjL24iN/mobile-app/mobile-app-overview
        # 第二步：获取 access_token
        self.SUITE_PASSPORT_OAUTH_TOKEN = self.PASSPORT_DOMAIN + '/suite/passport/oauth/token'
        # 第三步：获取用户信息
        self.SUITE_PASSPORT_OAUTH_USERINFO = self.PASSPORT_DOMAIN + '/suite/passport/oauth/userinfo'

    def get_access_info(self, code=None, grant_type='authorization_code', appid=None, secret=None, code_verifier=None):
        return self.post(self.SUITE_PASSPORT_OAUTH_TOKEN, data={
            'grant_type': grant_type,
            'client_id': appid,
            'client_secret': secret,
            'code': code,
            'code_verifier': code_verifier,
        }, content_type='application/x-www-form-urlencoded')

    def get_userinfo(self, access_token=None, code=None, grant_type='authorization_code', appid=None, secret=None, code_verifier=None):
        if not access_token:
            access_token = self.get_access_info(code=code, grant_type=grant_type, appid=appid, secret=secret, code_verifie=code_verifier)
        return self.post(self.SUITE_PASSPORT_OAUTH_USERINFO, data={
            'token': access_token,
        })


oauth2 = OAuth2()
get_access_info = oauth2.get_access_info
get_userinfo = oauth2.get_userinfo
