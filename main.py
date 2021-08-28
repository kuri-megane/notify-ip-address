import utils
from log import Log
from slack import Notify


def main():
    logger = Log()
    notifier = Notify(logger=logger)
    ip_address = utils.get_ip_address()
    logger.log_info(msg='IPアドレス通知 開始')
    logger.log_info(msg=f'IPアドレス: {ip_address}')
    notifier.send_with_text(text=f'IPアドレス: {ip_address}')
    logger.log_info(msg='IPアドレス通知 終了')


if __name__ == '__main__':
    main()
