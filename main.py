from pytive import Pytive
from pytive import CommentType

client = Pytive()
# クッキー
client.login('otpU8lo9_A7zNCGQ8dYf4Myy0VDdngGummbJg_okIZto2Rlo-VrolzFxoNtl-d8J', '62000862-94A5-11ED-BB7C-D518079FA8D5')


n = 1
# ユーザーのID
user_id = '105178229'

# countは 1 から 2147483646 までOK
client.request_live(user_id, count=2147483645)