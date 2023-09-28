
import requests
import json


cookies = {
    'spravka': 'dD0xNjgwMjYyODIyO2k9MTg4LjIzMy4yMDguMjI2O0Q9QzFGRDExODIyRTJGNDc3NkMxMTBBRjlENUI5NTJGQjI0NURCMkRFODAxNTZEQjNBN0M5Nzg0ODdERUUyNjkyNjY1RDY0NkRDMUYwNDZCO3U9MTY4MDI2MjgyMjE0MDk1NjgyNDtoPTZhZDRjYmIyOGNjNjQ3OGRlY2Y4NGVhYzU2ODY3ZjIw',
    'gdpr': '0',
    '_ym_isad': '2',
    'suid': 'eb98b34f9d8ba4441fe6f5c5af1ce353.dfbed501f0888bab728eefd7b9121127',
    '_yasc': 'dB+jcNt4GAkpTdAJbRIGBu5qujsbavQpSmgCTSGt9G0+0CoNemB/C79QN2/U',
    '_csrf_token': 'c156ad1d296a3634a54e7b848629acfd5378ff9336784c6a',
    'autoru_sid': 'a%3Ag6426c6a62ftn06g696seep3bmcbd9dj.c9c5e59d6702cf7027016f99cc6c80e4%7C1680262822479.604800.s3PYmEqPREKvMORpJQx8gQ.ocFMx4S9R1OxTerUrfEMn3EqSvSjjQk-qRLcCUmwXIA',
    'autoruuid': 'g6426c6a62ftn06g696seep3bmcbd9dj.c9c5e59d6702cf7027016f99cc6c80e4',
    'from_lifetime': '1680264753266',
    'from': 'direct',
    'yuidlt': '1',
    'yandexuid': '3670429621675081043',
    'ys': 'wprid.1680262807782523-8394831345513987638-vla1-5806-vla-l7-balancer-8080-BAL-9621%23c_chck.141224802',
    'layout-config': '{"screen_height":768,"screen_width":1366,"win_width":1366,"win_height":323}',
    'count-visits': '4',
    '_ym_uid': '1680262815999703878',
    '_ym_d': '1680263901',
    'sso_status': 'sso.passport.yandex.ru:blocked',
    'cycada': '2oWV/0J8eUQq58ewF4rKzNMn5NPF8oW/fDmm0uYGIo8=',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://auto.ru/',
    'x-client-app-version': '324.0.11180366',
    'x-client-date': '1680264756276',
    'x-csrf-token': 'c156ad1d296a3634a54e7b848629acfd5378ff9336784c6a',
    'x-requested-with': 'XMLHttpRequest',
    'x-page-request-id': '83cbcd43bc7247958f1fa8844f346dac',
    'x-retpath-y': 'https://auto.ru/',
    'x-yafp': '{"a1":"WToBHtSgnIFiKA==;0","a2":";1","a3":"F5hEf70QLFjpvnZK/43+zQ==;2","a4":"MgLYPlKEnHhGTZIubAY9JK3O2BSx6zZEJLzLVI/ubWqoUQ==;3","a5":"uHmA63ro+gZ22w==;4","a6":"wIs=;5","a7":"oYcJkURqQEBMiA==;6","a8":"xyUj2j+IN1Y=;7","a9":"fJ9PrXimzfRX+g==;8","b1":"U2yqkC94y4M78w==;9","b2":"vLDxt0+AA6S8uw==;10","b3":"yBSeBe4huQvEcw==;11","b4":"fA7e1Yw4N6g=;12","b5":"/96l/BJRM5SlUg==;13","b6":"0Erw/BKxQD8=;14","b7":"FI3IVwiHwWT42g==;15","b8":"GKlcBL+U3ATNwQ==;16","b9":"nQjJ6/gpfnHt4w==;17","c1":"5Z6qBg==;18","c2":"NcIPV6GLAPD2lg9uvx2Iow==;19","c3":"qoeIIYjxCKzKgaKw8KWzqw==;20","c4":"w/hSNTSs6Gg=;21","c5":"HNCy0Ndd3DM=;22","c6":"MSfGsw==;23","c7":"xBiDvIYG0fk=;24","c8":"PXSCpFyUDzQ=;25","c9":"Vs31s3A/xY4=;26","d1":"5EazWJxcl54zHZPuZiT4lVx2dHykPfDA;27","d2":"oVY=;28","d3":"vdIZH/Btkd2wOA==;29","d4":"twjTrwOMueA=;30","d5":"gS6p7lCdTXj/Og==;31","d7":"SSZJ9UxOuYY=;32","d8":"Dos3HCaM/GJOPhG36LdEM8iICiMrBOmt5Cg=;33","d9":"/4YZcRQlxNE=;34","e1":"9WwQ3ThQZ44C3w==;35","e2":"A7DS1BpoIoaSNQ==;36","e3":"GcqgG/CV7TGi0w==;37","e4":"lWiRQ8H1O7s=;38","e5":"odP+0hpU7dUltA==;39","e6":"ieo2s3EgohE=;40","e7":"duXD3gFfD4kvAQ==;41","e8":"c513Ql929Z8=;42","e9":"NjmX+0XWSQg=;43","f1":"tQQxteJihWFdjw==;44","f2":"+RDZe4sH3ds=;45","f3":"/LcuTfrixyazdA==;46","f4":"VeSHiQK5hlA=;47","f5":"Yfb2pk9OENfuuA==;48","f6":"yKP4Qrzfn83J/g==;49","f7":"nNrTAZk6wo+h7g==;50","f8":"0otaFXdCso5ZZg==;51","f9":"ItXykY5uTr0=;52","g1":"TDl+jvksTa4=;53","g2":"t9J60gcxeiCCrA==;54","g3":"kVC7Rn6n1kE=;55","g4":"rpv+grXjxY+fvg==;56","g5":"LmrDZcqMFLM=;57","g6":"G16MybCd5dFWHw==;58","g7":"O8wF27NKQ1U=;59","g8":"bAUfS6ZCZOk=;60","g9":"0XqxhoP2YM4=;61","h1":"cpAwWQ4eNkxCZw==;62","h2":"iqAPHLYg+4KM+g==;63","h3":"ApMEaTh9VA38ag==;64","h4":"QVSxy9dPIGnrtg==;65","h5":"igRRjnd+7no=;66","h6":"kcmLQq94ArhmFw==;67","h7":"zrUzsqIyYqlhcVYc8P+cqnIamiBwM4Z50qudAi0OdNjIjbshIlcNWBlMQtqJOTK/kuo1GflSZF0JcF4ejg0O4Iu1PrKiMnWpNXEUHOX/h6p2GqIgMTOWedirlgI9Di3YgY30ITVXTFgcTEPanDk6v9fqNxnyUipdHHAQHscND+CdtTGytTJwqSBxVxz0/8+qVhqjIHUzm3nYq7ACIQ5j2JuN/iE5VxhYW0w=;68","h8":"DzW5Fyad41aaBQ==;69","h9":"zi+6KS1xshDIVg==;70","i1":"BOnJJLl8MWQ=;71","i2":"Bkjtl5cIvl1XXQ==;72","i3":"CbEpa59CQgYEYA==;73","i4":"iocVg7LsBo36Dg==;74","i5":"NSR+bpBsGuDHzA==;75","z1":"Z8rkjWWT241zFgbYpvmaYEWZyjjl2pV497BjOCkLO77bXS3S33iUXrfQXwg4U+JmRn7b+uBh/72fgc5AnEpYUg==;76","z2":"QM6UsZhX0oldrf/NoQ5w1WdIwbBtSHj8k/WPiuaY1wl40Dtoykw/0kWVVPTc1Xssb3HHLNyu8iak1UutWHAnmw==;77","z3":"kyERG9vQc52J8A==;78","z6":"akIU06mpOUQLmJ3p;79","z7":"Sgqe2ny7eCKbfiaV;80","z8":"y2zqjZiczDLj2ktz;81","z9":"6Rrt1PXj6Hr/Lg==;82","y1":"jqG8twywDjgK7A==;83","y2":"OLHWl1e5CmGDkA==;84","y3":"1xX4ZasvTQuwGg==;85","y4":"xIj79P4XgYg6Zw==;86","y5":"KaBNEE6Kt73gUA==;87","y6":"djImDNUNoGTuVA==;88","y7":"Cj20Lwaun8tkZcq3;89","y8":"At8Jtk1vNH1rAQ==;90","y9":"sRwjhmer/A5g0g==;91","y10":"tvBm6VcEX5KcEw==;92","x1":"ekBeGVKQWSJXUw==;93","x2":"/dmqOHmOjr+fYw==;94","x3":"phpCo01Czy2Oqw==;95","x4":"rBK/9uR78MKL6w==;96","x5":"5Iw1DezudQtrFfDR;97","z5":"A1kht780IoA=;98","z4":"tGgyauk5TTpjw6SMotA=;99","v":"6.3.1","pgrdt":"fz/2JGEJvbM7JGDcyUl3Cy0TQOg=;100","pgrd":"pqLjt2zPxgHRptCvF3K+6WxFtYMFfQovbo1F3XBH0c37tPV2uPDlrTVS+jsSo0HZJhunLrDZ1zNHX4Ey9pvJFwyb9PGFgVzcfBYYQx6LqY7Fd6Iq99HpKfhdbF3C9+i1rOuNmZ34iJeWZJET3hBiDmO9UKdNIa7q2D3GkkMkDz7P2COwSbYL1IRLwIZY/ufR2OAHwYTIcLZAMhutGKixVZUy3lQ="}',
    'content-type': 'application/json',
    'Origin': 'https://auto.ru',
    'Connection': 'keep-alive',
    # 'Cookie': 'spravka=dD0xNjgwMjYyODIyO2k9MTg4LjIzMy4yMDguMjI2O0Q9QzFGRDExODIyRTJGNDc3NkMxMTBBRjlENUI5NTJGQjI0NURCMkRFODAxNTZEQjNBN0M5Nzg0ODdERUUyNjkyNjY1RDY0NkRDMUYwNDZCO3U9MTY4MDI2MjgyMjE0MDk1NjgyNDtoPTZhZDRjYmIyOGNjNjQ3OGRlY2Y4NGVhYzU2ODY3ZjIw; gdpr=0; _ym_isad=2; suid=eb98b34f9d8ba4441fe6f5c5af1ce353.dfbed501f0888bab728eefd7b9121127; _yasc=dB+jcNt4GAkpTdAJbRIGBu5qujsbavQpSmgCTSGt9G0+0CoNemB/C79QN2/U; _csrf_token=c156ad1d296a3634a54e7b848629acfd5378ff9336784c6a; autoru_sid=a%3Ag6426c6a62ftn06g696seep3bmcbd9dj.c9c5e59d6702cf7027016f99cc6c80e4%7C1680262822479.604800.s3PYmEqPREKvMORpJQx8gQ.ocFMx4S9R1OxTerUrfEMn3EqSvSjjQk-qRLcCUmwXIA; autoruuid=g6426c6a62ftn06g696seep3bmcbd9dj.c9c5e59d6702cf7027016f99cc6c80e4; from_lifetime=1680264753266; from=direct; yuidlt=1; yandexuid=3670429621675081043; ys=wprid.1680262807782523-8394831345513987638-vla1-5806-vla-l7-balancer-8080-BAL-9621%23c_chck.141224802; layout-config={"screen_height":768,"screen_width":1366,"win_width":1366,"win_height":323}; count-visits=4; _ym_uid=1680262815999703878; _ym_d=1680263901; sso_status=sso.passport.yandex.ru:blocked; cycada=2oWV/0J8eUQq58ewF4rKzNMn5NPF8oW/fDmm0uYGIo8=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'same-origin',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

json_data = {
    'page_size': 40,
    'page': 5,
    'state': [
        'NEW',
        'USED',
    ],
    'lenta_session_id': '8d5bfc1af0f4de0962022c801d22a0cc',
    'geo_id': [],
}

response = requests.post(
    'https://auto.ru/-/ajax/desktop/getMixedPersonalizedOffersFeed/',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"page_size":40,"page":5,"state":["NEW","USED"],"lenta_session_id":"8d5bfc1af0f4de0962022c801d22a0cc","geo_id":[]}'
#response = requests.post(
#    'https://auto.ru/-/ajax/desktop/getMixedPersonalizedOffersFeed/',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)

with open(f'avtoru.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, ensure_ascii=False)
