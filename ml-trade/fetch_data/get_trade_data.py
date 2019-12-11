import requests
import os
from mytoolbox import logger, get_local_time
import time
import csv

def get_price_and_volume_data(data_path='./datasets/', coin_name='btc', first_flag=True):
    r_url = 'https://data.gateio.co/api2/1/ticker/{}_usdt'.format(coin_name)
    
    # 不存在目录则创建
    if not os.path.exists(data_path):
        os.mkdir(data_path)
    dataset = data_path + '{}_price_and_volume.csv'.format(coin_name)

    # 文件已经存在说明有表头
    if os.path.exists(dataset):
        first_flag = False

    try:
        r = requests.get(r_url)
        price_dict = eval(r.text)

        price_dict.update({'Timestamp': get_local_time()})
        price_dict.__delitem__('result')
        price_dict.__delitem__('elapsed')

        with open(dataset, 'a') as fp:
            w = csv.writer(fp)
            if first_flag:
                w.writerow(price_dict.keys())
            w.writerow(price_dict.values())
        return True

    except Exception as e:
        logger('err', e)
        return False
