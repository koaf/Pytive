# pytive
Bot用

## TODO
- [x] 配信情報の取得
- [x] コメント機能
- [ ] フォロー/フォロー解除
- [x] 配信リクエスト

## 注意
このプロジェクトの使用によって生じたいかなる損害に対しても責任を負いません

## 使い方
### ログイン

```python
from pytive import Pytive

client = Pytive()
# クッキー
client.login('mr_idをここに', 'fをここに')
```
### メッセージ送信

```python
from pytive import CommentType

# ...mirrativ.com/live/'ここ'
live_id = ''

client.join_live(live_id)
client.comment(live_id, CommentType.NORMAL, 'pog')
```
### ライブリクエスト
```python
# ユーザーのID
user_id = ''

# countは 1 から 2147483646 までOK
client.request_live(user_id, count=1)
```
