from pytive import Pytive, CommentType
n = 1
def message_test():
    live_id = 'lliveid'

    client = Pytive()
    client.login('mid', 'f')
    while n == 1:
        live_id = 'liveid'

        client = Pytive()
        client.login('mid', 'f')

        client.join_live(live_id)
        client.comment(live_id, CommentType.NORMAL, 'pog')

if __name__ == '__main__':
    message_test()
