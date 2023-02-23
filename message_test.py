from pytive import Pytive, CommentType

def message_test():
    live_id = 'lliveid'

    client = Pytive()
    client.login('mid', 'f')

    client.join_live(live_id)
    client.comment(live_id, CommentType.NORMAL, 'pog')

if __name__ == '__main__':
    message_test()
