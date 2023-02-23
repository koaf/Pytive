from logging import getLogger, basicConfig, DEBUG
from random import randrange, choices

import json
import requests
import string

from attrdict import AttrDict
from pytive import Pytive

logger = getLogger("Pytive")
basicConfig(
    level=DEBUG,
    format="[%(levelname)s] %(message)s"
)

session = requests.session()

def letters(length: int):
   return ''.join(choices(string.ascii_letters + string.digits, k=length))

def generate_test():
    client = Pytive()

    obtain_cookies = session.get(
        'https://www.mirrativ.com/api/user/me',
        headers=dict(**client.common_headers, **{
            'User-Agent': client.user_agent,
            'Accept-Encoding': 'gzip',
            'Accept': '*/*',
            'Connection': 'keep-alive'
        })
    )
    if obtain_cookies.status_code != 200:
        logger.error('Failed to obtain cookie')
        return

    user_id = AttrDict(json.loads(obtain_cookies.text)).user_id
    logger.info('UserId: ' + user_id)
    client.login(obtain_cookies.cookies.get('mr_id'), obtain_cookies.cookies.get('f'))

    profiler = session.post(
        'https://www.mirrativ.com/api/user/profile_edit',
        data={
            'user_id': user_id,
            'name': letters(10),
            'description': letters(30),
            'include_urge_users': '1',
            'dynamic_link': ''
        },
        files={
            (None, None)
        },
        headers=dict(**client.common_headers, **{
            'User-Agent': client.user_agent,
            'Accept-Encoding': 'gzip',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'x-referer': 'tutorial'
        }),
        cookies={
            'lang': client.lang,
            'mr_id': client.id,
            'f': client.unique
        }
    )
    if profiler.status_code != 200:
        logger.error('Failed to create profile')
        return

    if AttrDict(json.loads(profiler.text)).status.ok != 1:
        logger.error('Failed to create profile (maybe ip limit)')
        return

    if session.post(
        'https://www.mirrativ.com/api/user/post_demographic',
        data={
            # 1 = 男性
            # 2 = 女性
            # 3 = 無し
            'gender_type': randrange(1, 3),
            'generation': randrange(2000, 2008)
        },
        headers=dict(**client.common_headers, **{
            'User-Agent': client.user_agent,
            'Accept-Language': 'ja-JP',
            'Accept-Encoding': 'gzip',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'x-referer': 'tutorial'
        }),
        cookies={
            'lang': client.lang,
            'mr_id': client.id,
            'f': client.unique
        }
    ).status_code != 200:
        logger.error('統計の送信に失敗しました')
        return

    logger.info('{}:{}'.format(
        client.id,
        client.unique
    ))

if __name__ == '__main__':
    generate_test()
