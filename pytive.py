from logging import getLogger, basicConfig, INFO
from typing import Optional
from enum import Enum

import requests
import secrets
import uuid

from attrdict import AttrDict

logger = getLogger('Pytive')
basicConfig(
    level=INFO,
    format='[%(levelname)s] %(message)s'
)

class CommentType(Enum):
    NORMAL: int = 1
    JOIN_LOG: int = 3

class Pytive:
    def __init__(self):
        self.session = requests.session()
        self.user_agent = 'MR_APP/9.85.0/StiffCock/F4-RT/9'
        self.common_headers = {
            'HTTP_X_TIMEZONE': 'Asia/Tokyo',
            'x-idfv': secrets.token_hex(int(17 / 2)),
            'x-ad': str(uuid.uuid4()),
            'x-hw': 'intel',
            'x-network-status': '2',
            'x-os-push': '1',
            'x-client-unixtime': '', # TODO
            'x-adjust-adid': secrets.token_hex(int(33 / 2)),
            'x-unity-framework': '4.13.0'
        }

        self.lang   = 'ja'
        self.id     = ''
        self.unique = ''

    def login(self, id: str, unique: str):
        self.id = id
        self.unique = unique

    def get_my_profile(self) -> Optional[AttrDict]:
        resp = self.session.get(
            'https://www.mirrativ.com/api/user/me',
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'x-referer': 'my_page',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )
        if resp.status_code != 200:
            return None
        return AttrDict(resp.json())

    def get_user_profile(self, user_id: str) -> Optional[AttrDict]:
        resp = self.session.get(
            'https://www.mirrativ.com/api/user/profile',
            params={
                'user_id': user_id
            },
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'x-referer': 'profile',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )
        if resp.status_code != 200:
            return None
        return AttrDict(resp.json())

    def get_season_rating(self) -> Optional[AttrDict]:
        resp = self.session.get(
            'https://www.mirrativ.com/api/season_rating/status',
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'x-referer': 'home.select',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )
        if resp.status_code != 200:
            return None
        return AttrDict(resp.json())

    def get_mission_status(self) -> Optional[AttrDict]:
        resp = self.session.get(
            'https://www.mirrativ.com/api/mission/status',
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'x-referer': 'home.select',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )
        if resp.status_code != 200:
            return None
        return AttrDict(resp.json())

    def get_onlive_apps(self) -> Optional[AttrDict]:
        resp = self.session.get(
            'https://www.mirrativ.com/api/app/onlive_apps',
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'x-referer': 'home.select',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )
        if resp.status_code != 200:
            return None
        return AttrDict(resp.json())

    def get_urge_users(self) -> Optional[AttrDict]:
        resp = self.session.get(
            'https://www.mirrativ.com/api/graph/urge_users',
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'x-referer': 'home.follow',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )
        if resp.status_code != 200:
            return None
        return AttrDict(resp.json())

    def get_catalog(self, cursor: str = ''):
        resp = self.session.get(
            'https://www.mirrativ.com/api/live/catalog',
            params={
                'id': '2',
                'cursor': cursor
            },
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'x-referer': 'home',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )
        if resp.status_code != 200:
            return None
        return AttrDict(resp.json())

    def get_info(self, live_id: str) -> Optional[AttrDict]:
        resp = self.session.get(
            'https://www.mirrativ.com/api/live/live',
            params={
                'live_id': live_id
            },
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'x-referer': 'live_view',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )
        if resp.status_code != 200:
            return None
        return AttrDict(resp.json())

    def get_status(self, live_id: str) -> Optional[AttrDict]:
        resp = self.session.get(
            'https://www.mirrativ.com/api/live/get_streaming_url',
            params={
                'live_id': live_id
            },
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'x-referer': 'live_view',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )
        if resp.status_code != 200:
            return None
        return AttrDict(resp.json())

    def get_comments(self, live_id: str) -> Optional[AttrDict]:
        resp = self.session.get(
            'https://www.mirrativ.com/api/live/live_comments',
            params={
                'live_id': live_id
            },
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'x-referer': 'live_view',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )
        if resp.status_code != 200:
            return None
        return AttrDict(resp.json())

    def get_online_users(self, live_id: str, page: int = 1):
        resp = self.session.get(
            'https://www.mirrativ.com/api/live/online_users',
            params={
                'live_id': live_id,
                'page': str(page)
            },
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'x-referer': 'live_view',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )
        if resp.status_code != 200:
            return None
        return AttrDict(resp.json())

    def get_collaborators(self, live_id: str) -> Optional[AttrDict]:
        resp = self.session.get(
            'https://www.mirrativ.com/api/collab/collaborating_users',
            params={
                'live_id': live_id
            },
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'x-referer': 'live_view',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )
        if resp.status_code != 200:
            return None
        return AttrDict(resp.json())

    def join_live(self, live_id: str):
        live_info = self.get_info(live_id)
        if live_info is None:
            logger.error('配信情報の取得に失敗しました')
            return

        if self.session.get(
            'https://www.mirrativ.com/api/event/notice',
            params={
                'type': '2',
                'live_id': live_id
            },
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        ).status_code != 200:
            return

        live_comments = self.get_comments(live_id)
        if live_comments is None:
            logger.error('コメントの取得に失敗しました')
            return

        live_status = self.get_status(live_id)
        if live_info is None:
            logger.error('配信情報の取得に失敗しました')
            return

        if live_status.status.ok != 1 | live_status.is_live == 0:
            logger.error('配信は終了しています')
            return

        if live_status.is_private == 1:
            logger.error('この配信はプライベートです')
            return

        # Send JoinLog
        self.comment(live_id, 3, '')

    def leave_live(self, live_id: str):
        self.session.post(
            'https://www.mirrativ.com/api/live/leave',
            data={
                'live_id': live_id
            },
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )

    def request_live(self, user_id: str, count: int = 1) -> Optional[AttrDict]:
        if count < 1:
            count = 1
        elif count > 2147483646:
            count = 2147483646

        resp = self.session.post(
            'https://www.mirrativ.com/api/user/post_live_request',
            data={
                'count': str(count),
                'user_id': user_id,
                'where': 'profile'
            },
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'x-referer': 'profile',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )
        if resp.status_code != 200:
            logger.error('ライブリクエストに失敗しました (Code: {})'.format(resp.status_code))
            return None
        return AttrDict(resp.json())

    def comment(self, live_id: str, type: int, message: str):
        if live_id is None:
            return

        resp = self.session.post(
            'https://www.mirrativ.com/api/live/live_comment',
            data={
                'live_id': live_id,
                'comment': message,
                'type': '1',
                # 'from_catalog_id': '2'
            },
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'x-referer': 'live_view',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )
        if resp.status_code != 200:
            logger.error('コメントの送信に失敗しました (Code: {})'.format(resp.status_code))

    # TODO 🤔
    def follow(self, user_id: str) -> Optional[AttrDict]:
        resp = self.session.post(
            'https://www.mirrativ.com/api/graph/follow',
            data={
                'user_id': user_id
            },
            headers=dict(**self.common_headers, **{
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'ja-jp',
                'Connection': 'keep-alive',
                'x-referer': 'live_view',
                'Cookie': 'lang={}; mr_id={}; f={};'.format(self.lang, self.id, self.unique)
            })
        )
        if resp.status_code != 200:
            logger.error('フォローに失敗しました')
            return None
        return AttrDict(resp.json())
