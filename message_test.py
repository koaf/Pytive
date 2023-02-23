from pytive import Pytive, CommentType

def message_test():
    live_id = 'f352rQVtAfY58XPv_lyTuA'

    client = Pytive()
    client.login('otpU8lo9_A7zNCGQ8dYf4Myy0VDdngGummbJg_okIZto2Rlo-VrolzFxoNtl-d8J', 'f352rQVtAfY58XPv_lyTuA')

    client.join_live(live_id)
    client.comment(live_id, CommentType.NORMAL, 'pog')

if __name__ == '__main__':
    message_test()
