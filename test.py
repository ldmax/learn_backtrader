"""playground of backtrader: a popular backtest framework
written in python
"""
from __future__ import (absolute_import,
                        division, print_function, unicode_literals)
import backtrader as bt


if __name__ == "__main__":
    cerebro = bt.Cerebro()
    print(f"Starting Portfolio Value: {cerebro.broker.getvalue()}")

    cerebro.run()

    print(f"Final Portfolio Value: {cerebro.broker.getvalue()}")
