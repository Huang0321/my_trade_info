import time
from gevent import monkey; monkey.patch_all()

import gevent

from client import binance, gateio
from trade_condition.condition1 import check_signal
from settings import SYMBOL
from utils import logger


def main():
    ba = binance.BinanceClient()
    gate = gateio.GateioClient()
    # 查询并记录开始的账户信息
    task1 = gevent.spawn(ba.fetch_symbol_balance, SYMBOL)
    task2 = gevent.spawn(gate.fetch_symbol_balance, SYMBOL)
    gevent.joinall([task1, task2])
    logger.info('start_balance: %s %s' % (task1.value, task2.value))
    while True:
        time.sleep(1)
        check_signal(ba, gate, SYMBOL)


if __name__ == "__main__":
    main()

