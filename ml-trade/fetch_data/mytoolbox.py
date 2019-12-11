import os
import time

def get_local_time():
    return str(time.strftime("%Y.%m.%d %H:%M", time.localtime()))

def logger(message_type, _message):
    if not os.path.exists('./logs/'):
        os.mkdir('./logs/')
    log_path = './logs/{}.log'.format(message_type)
    with open(log_path, 'a') as fp:
        write_message = '\n' + str(get_local_time()) + '\t' + str(_message)
        fp.write(write_message)
        print('write a log')
    return 0

