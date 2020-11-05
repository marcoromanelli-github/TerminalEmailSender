from TerminalEmailSender.connection_manager import *


def test_0():
    conn_mng = ConnectionManager()
    conn_mng.connect_to_server()
    conn_mng.send_message()
    conn_mng.disconnect()


if __name__ == "__main__":
    test_0()