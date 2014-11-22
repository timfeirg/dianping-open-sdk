# -*- coding: utf-8 -*-

"""
File: dianping_sign.py
Author: timfeirg
Email: kkcocogogo@gmail.com
Github: https://github.com/timfeirg/
Description: payload in, url out
"""

import hashlib
import urllib

appkey = '123423453456'
secret = '1234asdf1234asdf1234asdf'


def sign(base_url, payload):
    """generate a signed dianping api request url based on appkey & secret:
    payload -- http get request parameters in the form of a dictionary
    """
    codec = appkey
    for k, v in sorted(payload.items()):
        codec += k + v

    codec += secret
    sign = (hashlib.sha1(codec).hexdigest()).upper()
    payload.update(
        {
            'appkey': appkey,
            'sign': sign,
        }
    )
    query = urllib.urlencode(payload)
    url = base_url + '?' + query
    return url

if __name__ == '__main__':
    base_url = (
        'http://api.dianping.com/'
        'v1/business/get_batch_businesses_by_id'
    )
    payload = {
        'business_ids': '123456,33333',
    }
    url = sign(base_url, payload)
    print(url)
