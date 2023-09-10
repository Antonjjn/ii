import tkinter as tk


import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("42441186715bfe74ae3d17084c87e2b26e30dab7e558972b341ce9fb5cc38fc4",
                            "53ad9d44a6e4195e0cc1216d6949f0e791944b30d159a8b8fa12cccd6bd794f6",
                            testnet=True, futures=True)
    bitmex = BitmexClient("H3_jWwM6HUC1bWik18jq4yFs", "JSc1g47Q25_KiC20ENzYly87CEFkRdJTOmZe65GIADarpYc3", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
