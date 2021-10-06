import utils
from log import Log
from slack import Notify


def main():
    logger = Log()
    notifier = Notify(logger=logger)
    logger.log_info(msg='ステータス通知 開始')
    local_ip_address = utils.get_local_ip_address()
    logger.log_info(msg=f'ローカルIPアドレス: {local_ip_address}')
    notifier.send_with_text(text=f'ローカルIPアドレス: {local_ip_address}')
    global_ip_address = utils.get_global_ip_address()
    logger.log_info(msg=f'グローバルIPアドレス: {global_ip_address}')
    notifier.send_with_text(text=f'グローバルIPアドレス: {global_ip_address}')
    disk_usage = utils.get_disk_usage()
    logger.log_info(msg=f'ディスク使用量\n{disk_usage}')
    notifier.send_with_text(text=f'ディスク使用量\n{disk_usage}')
    logger.log_info(msg='ステータス通知 終了')


if __name__ == '__main__':
    main()
