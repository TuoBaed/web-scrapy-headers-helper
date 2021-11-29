# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 10:22:25 2021

@author: 
"""
from collections import OrderedDict
from pprint import pprint as pp



def get_headers_dict_format(string_headers):
    """
    convert request headers in browsers into OrderedDict type
    
    Parameters
    ----------
    string_headers : str
        str type headers in browser

    Returns
    -------
    headers : OrderedDict
        OrderedDict type headers

    """
    headers = OrderedDict()
    for item in string_headers.split("\n"):
        if item:
            key, value = item.split(": ", maxsplit=1)
            # print(key)
            # print(value)
            headers[key] = value
    
    return headers


if __name__ == "__main__":
    string_headers = """
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cache-control: no-cache
pragma: no-cache
sec-ch-ua: "Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"
sec-ch-ua-arch: "x86"
sec-ch-ua-full-version: "94.0.4606.61"
sec-ch-ua-mobile: ?0
sec-ch-ua-model: ""
sec-ch-ua-platform: "Windows"
sec-ch-ua-platform-version: "10.0.0"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
service-worker-navigation-preload: true
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36
"""

    another_string = """
accept: */*
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cache-control: no-cache
content-length: 2044
content-type: application/json
origin: https://www.youtube.com
pragma: no-cache
referer: https://www.youtube.com/playlist?list=PLkuKHvw9NmzSPKGTC4kj5AxyZMsc5iXPT
sec-ch-ua: "Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"
sec-ch-ua-arch: "x86"
sec-ch-ua-full-version: "94.0.4606.61"
sec-ch-ua-mobile: ?0
sec-ch-ua-model: 
sec-ch-ua-platform: "Windows"
sec-ch-ua-platform-version: "10.0.0"
sec-fetch-dest: empty
sec-fetch-mode: same-origin
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36
x-goog-visitor-id: Cgs3RVJXV1NWQkRlMCjQvemKBg%3D%3D
x-youtube-client-name: 1
x-youtube-client-version: 2.20210929.06.00"""


    headers = get_headers_dict_format(string_headers)
    pp(dict(headers))
    another_headers = get_headers_dict_format(another_string)
    pp(dict(another_headers))
        