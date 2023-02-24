from pytive import Pytive
from pytive import CommentType

client = Pytive()

comment = client.comments(live_id)
print(comment)
