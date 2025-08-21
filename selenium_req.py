#!/usr/bin/env python
# encoding: utf-8
import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def post_using_fetch(driver, url, data: str):
    js_code = f"""
    var result;
    fetch('{url}', {{
        method: 'POST',
        headers: {{
            'Content-Type': 'application/json',
        }},
        body: {data}
    }})
    .then(response => response.json())
    .then(data => {{
        result = data;
    }})
    .catch(error => {{
        result = {{error: error.message}};
    }});

    var start = Date.now();
    while (result === undefined && Date.now() - start < 5000) {{
    }}
    return result;
    """
    return driver.execute_script(js_code)


def web_get_erc20_token_balances():
    chrome_options = ChromeOptions()

    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
    chrome_options.add_argument('--proxy-server=http://127.0.0.1:1080')

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    data = {
        "dataTableModel": {
            "draw": 1,
            "columns": [{
                "data": "TokenName",
                "name": "",
                "searchable": True,
                "orderable": True,
                "search": {
                    "value": "",
                    "regex": False
                }
            }, {
                "data": "ContractAddress",
                "name": "",
                "searchable": True,
                "orderable": False,
                "search": {
                    "value": "",
                    "regex": False
                }
            }, {
                "data": "Price",
                "name": "",
                "searchable": True,
                "orderable": True,
                "search": {
                    "value": "",
                    "regex": False
                }
            }, {
                "data": "Change24H",
                "name": "",
                "searchable": True,
                "orderable": False,
                "search": {
                    "value": "",
                    "regex": False
                }
            }, {
                "data": "Balance",
                "name": "",
                "searchable": True,
                "orderable": True,
                "search": {
                    "value": "",
                    "regex": False
                }
            }, {
                "data": "Value",
                "name": "",
                "searchable": True,
                "orderable": True,
                "search": {
                    "value": "",
                    "regex": False
                }
            }, {
                "data": "More",
                "name": "",
                "searchable": True,
                "orderable": False,
                "search": {
                    "value": "",
                    "regex": False
                }
            }],
            "order": [{
                "column": 5,
                "dir": "desc"
            }],
            "start": 0,
            "length": 10,
            "search": {
                "value": "",
                "regex": False
            }
        },
        "model": {
            "address": "0xd2674da94285660c9b2353131bef2d8211369a4b",
            "hideZeroAssets": False,
            "filteredContract": "",
            "showEthPrice": False
        }
    }

    try:
        fetch_result = post_using_fetch(driver, "https://etherscan.io/address-token-holding.aspx/GetAssetDetails",
                                        json.dumps(data))
        print(fetch_result)

    finally:
        driver.quit()


if __name__ == "__main__":
    web_get_erc20_token_balances()
