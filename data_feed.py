# -*- encoding: utf-8 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import datetime    # For datetime objects
import os.path     # To manage paths
import sys         # To find out the script name (in argv[0])

# Import the backtrader platform
import backtrader as bt


if __name__ == '__main__':
    # create a cerebro entity
    cerebro = bt.Cerebro()

    # data are in a subfolder of the samples
    # need to find where the script is because
    # it could have been called from anywhere
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, "../../datas/orcl-1995-2014.txt")

    # create a data feed
    data = bt.feeds.YahooFinanceCSVData(
        dataname=datapath,
        # do not pass values before this date
        fromdate=datetime.datetime(2000, 1, 1),
        # do not pass values after this date
        todate=datetime.datetime(2000, 12, 31),
        reverse=False
    )

    # add the data feed to cerebro
    cerebro.adddata(data)

    # set our desired cash start
    cerebro.broker.setcash(100000.0)

    # print out the starting conditions
    print(f"Starting Portfolio Value: {cerebro.broker.getvalue()}")

    # run over everything
    cerebro.run()

    # print out the final result
    print(f"Final Portfolio Value: {cerebro.broker.getvalue()}")
