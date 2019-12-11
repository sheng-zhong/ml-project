# main function
from multiprocessing import Pool
from get_trade_data import get_price_and_volume_data
import time

def get_datasets():
    while True:
        get_price_and_volume_data()
        time.sleep(60)

if __name__ == '__main__':
    get_datasets()
