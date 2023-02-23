from pytive import Pytive
from pytive import CommentType

client = Pytive()
# クッキー
client.login('mid', 'f')


n = 1
# ユーザーのID
user_id = '105178229'

# countは 1 から 2147483646 までOK

client.request_live(user_id, count=2147483645)
client.unfollow(125044709)

