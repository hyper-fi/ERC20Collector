#!/usr/bin/env python
# encoding: utf-8
import os
import time

import requests  # type: ignore
import urllib3.util.connection as urllib3_cn
from dotenv import load_dotenv

urllib3_cn.HAS_IPV6 = False

load_dotenv(".env")

ETHER_SCAN_MAINNET_API_URL = "https://api.etherscan.io/v2/api"
ETHER_SCAN_API_SECRET = os.environ.get("API_KEY", 'null_api_key')


def get_erc20_token_balances(chain_id: int, address: str):
    url = ("{}?chainid={}&module=account&action=addresstokenbalance&address={}&tag=latest&apikey={}".
           format(ETHER_SCAN_MAINNET_API_URL, chain_id, address, ETHER_SCAN_API_SECRET))

    # proxies: dict = {}
    proxies = {"http": "http://127.0.0.1:1080", "https": "http://127.0.0.1:1080"}

    resp = requests.get(url, proxies=proxies, timeout=30)
    return resp.json()


def get_address_erc20_token_balance(chain_id: int, address: str, contract_addr: str):
    url = ("{}?chainid={}&module=account&action=tokenbalance&address={}&contractaddress={}&tag=latest&apikey={}".
           format(ETHER_SCAN_MAINNET_API_URL, chain_id, address, contract_addr, ETHER_SCAN_API_SECRET))

    # proxies: dict = {}
    proxies = {"http": "http://127.0.0.1:1080", "https": "http://127.0.0.1:1080"}

    resp = requests.get(url, proxies=proxies, timeout=30)
    return resp.json()


def get_address_erc20_token_balance_his(chain_id: int, address: str, contract_addr: str, blockno: int):
    url = ("{}?chainid={}&module=account&action=tokenbalancehistory&address={}&contractaddress={}&blockno={}&apikey={}".
           format(ETHER_SCAN_MAINNET_API_URL, chain_id, address, contract_addr, blockno, ETHER_SCAN_API_SECRET))

    # proxies: dict = {}
    proxies = {"http": "http://127.0.0.1:1080", "https": "http://127.0.0.1:1080"}

    resp = requests.get(url, proxies=proxies, timeout=30)
    return resp.json()


def get_token_holder_list(chain_id: int, contract_addr: str, page: int, offset: int):
    url = ("{}?chainid={}&module=token&action=tokenholderlist&contractaddress={}&page={}&offset={}&apikey={}"
           .format(ETHER_SCAN_MAINNET_API_URL, chain_id, contract_addr, page, offset, ETHER_SCAN_API_SECRET))

    # proxies: dict = {}
    proxies = {"http": "http://127.0.0.1:1080", "https": "http://127.0.0.1:1080"}

    resp = requests.get(url, proxies=proxies, timeout=30)
    return resp.json()


def get_token_holder_count(chain_id: int, contract_addr: str):
    url = ("{}?chainid={}&module=token&action=tokenholdercount&contractaddress={}&apikey={}"
           .format(ETHER_SCAN_MAINNET_API_URL, chain_id, contract_addr, ETHER_SCAN_API_SECRET))

    # proxies: dict = {}
    proxies = {"http": "http://127.0.0.1:1080", "https": "http://127.0.0.1:1080"}

    resp = requests.get(url, proxies=proxies, timeout=30)
    return resp.json()


def get_top_token_holders(chain_id: int, contract_addr: str, offset: int):
    url = ("{}?chainid={}&module=token&action=topholders&contractaddress={}&offset={}&apikey={}"
           .format(ETHER_SCAN_MAINNET_API_URL, chain_id, contract_addr, offset, ETHER_SCAN_API_SECRET))

    # proxies: dict = {}
    proxies = {"http": "http://127.0.0.1:1080", "https": "http://127.0.0.1:1080"}

    resp = requests.get(url, proxies=proxies, timeout=30)
    return resp.json()


if __name__ == "__main__":
    r = get_erc20_token_balances(1, "0xd2674da94285660c9b2353131bef2d8211369a4b")
    print(r)

    r = get_address_erc20_token_balance(1, "0xd2674da94285660c9b2353131bef2d8211369a4b",
                                        "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48")
    print(r)

    r = get_address_erc20_token_balance_his(1, "0xd2674da94285660c9b2353131bef2d8211369a4b",
                                            "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", 23180606)
    print(r)

    r = get_token_holder_list(1, "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", 1, 100)
    print(r)

    r = get_token_holder_count(1, "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48")
    print(r)

    r = get_top_token_holders(1, "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", 10)
    print(r)
