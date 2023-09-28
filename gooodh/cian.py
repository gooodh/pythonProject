import requests
import json

cookies = {
    '_CIAN_GK': '0a1794fd-5df0-4ae6-a442-e02715652c7d',
    '__cf_bm': 'jF82wsK6JOTXP2PzIm0fncnhPOt3R4Q6VD_wgY0A6Us-1677479741-0-AUbdKQTuZk+O8bDugg/5rWm10lTQlLAcn0J+TGtUwZJKwzV0Go9ob/ftD77jLm8Usv5D4p0ppqw7H4G+yxnJusA=',
    'session_region_id': '4998',
    'login_mro_popup': '1',
    'sopr_utm': '%7B%22utm_source%22%3A+%22yandex%22%2C+%22utm_medium%22%3A+%22organic%22%7D',
    'sopr_session': 'fbdffa35da3d47a2',
    '_gcl_au': '1.1.628487639.1677479750',
    'yaref': '1',
    'uxfb_usertype': 'searcher',
    'uxs_uid': 'fa995440-b668-11ed-a4e1-430a26aafa91',
    '_ga': 'GA1.2.1506588949.1677479753',
    '_gid': 'GA1.2.744101200.1677479753',
    'tmr_lvid': '53bb9cb48b37659af8bcd219f456536e',
    'tmr_lvidTS': '1677479753442',
    '_ym_uid': '1677479754611996417',
    '_ym_d': '1677479754',
    '_ym_visorc': 'b',
    '_ym_isad': '2',
    'adrdel': '1',
    'adrcid': 'A7QFbdjedOCnmLceTQnrbow',
    'afUserId': '3beacc6e-8a55-409a-a6dd-d7668a3fa4b0-p',
    'AF_SYNC': '1677479756544',
    'viewpageTimer': '205.073',
    'session_main_town_region_id': '4998',
    'cookie_agreement_accepted': '1',
    'pview': '2',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Origin': 'https://krasnodar.cian.ru',
    'Alt-Used': 'api.cian.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://krasnodar.cian.ru/',
    # 'Cookie': '_CIAN_GK=0a1794fd-5df0-4ae6-a442-e02715652c7d; __cf_bm=jF82wsK6JOTXP2PzIm0fncnhPOt3R4Q6VD_wgY0A6Us-1677479741-0-AUbdKQTuZk+O8bDugg/5rWm10lTQlLAcn0J+TGtUwZJKwzV0Go9ob/ftD77jLm8Usv5D4p0ppqw7H4G+yxnJusA=; session_region_id=4998; login_mro_popup=1; sopr_utm=%7B%22utm_source%22%3A+%22yandex%22%2C+%22utm_medium%22%3A+%22organic%22%7D; sopr_session=fbdffa35da3d47a2; _gcl_au=1.1.628487639.1677479750; yaref=1; uxfb_usertype=searcher; uxs_uid=fa995440-b668-11ed-a4e1-430a26aafa91; _ga=GA1.2.1506588949.1677479753; _gid=GA1.2.744101200.1677479753; tmr_lvid=53bb9cb48b37659af8bcd219f456536e; tmr_lvidTS=1677479753442; _ym_uid=1677479754611996417; _ym_d=1677479754; _ym_visorc=b; _ym_isad=2; adrdel=1; adrcid=A7QFbdjedOCnmLceTQnrbow; afUserId=3beacc6e-8a55-409a-a6dd-d7668a3fa4b0-p; AF_SYNC=1677479756544; viewpageTimer=205.073; session_main_town_region_id=4998; cookie_agreement_accepted=1; pview=2',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

json_data = {
    't': 'pageview',
    'v': '1',
    'cid': '0a1794fd-5df0-4ae6-a442-e02715652c7d',
    'dl': 'https%3A%2F%2Fkrasnodar.cian.ru%2Fcat.php%3Fdeal_type%3Drent%26engine_version%3D2%26offer_type%3Dflat%26p%3D8%26region%3D4998%26type%3D2',
    'rid': '8C6877FC-B669-11ED-8F45-0AB657FA0059',
    'ua': 'Mozilla%2F5.0%20(X11%3B%20Linux%20x86_64%3B%20rv%3A109.0)%20Gecko%2F20100101%20Firefox%2F110.0',
    'ec': 'page',
    'ea': 'newpage',
    'el': 'open',
    'sc': {
        '_type': 'flatrent',
        'engine_version': {
            'type': 'term',
            'value': 2,
        },
        'region': {
            'type': 'terms',
            'value': [
                4998,
            ],
        },
        'page': {
            'type': 'term',
            'value': 8,
        },
        'for_day': {
            'type': 'term',
            'value': '1',
        },
    },
    'event': 'newpage',
    'referrer': '',
    'join_id': '3aea4225-4d71-4e9b-8286-4913dcd9583b',
    'user': {},
    'page': {
        'listingType': 'extended',
        'pageNumber': 8,
        'queryString': '/cat.php?deal_type%3Drent%26engine_version%3D2%26offer_type%3Dflat%26p%3D8%26region%3D4998%26type%3D2',
        'offersQty': 14853,
        'siteType': 'desktop',
        'extra': {
            'extended_type': [
                'outskirts',
            ],
            'mlSearchSessionGuid': '804a9d8a-7edf-455f-806b-f534c072f23d',
            'searchRequestId': 'ba4fe980-4daa-4e70-bbc1-d9adda789d53',
        },
        'mlRankingGuid': '1fff580d-eab3-48d0-86ee-5e8a64e599de',
        'mlRankingModelVersion': 'v3',
        'pageType': 'Listing',
    },
    'products': [
        {
            'id': 283920229,
            'offerType': 'offer',
            'position': 1,
            'extra': {
                'parentId': 0,
            },
        },
        {
            'id': 279751528,
            'offerType': 'offer',
            'position': 2,
            'extra': {
                'parentId': 0,
            },
        },
        {
            'id': 281308015,
            'offerType': 'offer',
            'position': 3,
            'extra': {
                'parentId': 8775,
            },
        },
        {
            'id': 270897941,
            'offerType': 'offer',
            'position': 1,
            'extra': {
                'extended_type': [
                    'outskirts',
                ],
                'parentId': 0,
                'sutochno_feed_test': True,
                'sutochno_url': 'https://sochi.cian.ru/rent/flat/270897941/',
            },
        },
        {
            'id': 255459067,
            'offerType': 'offer',
            'position': 4,
            'extra': {
                'parentId': 149284,
            },
        },
        {
            'id': 276707322,
            'offerType': 'offer',
            'position': 5,
            'extra': {
                'parentId': 0,
            },
        },
        {
            'id': 279354088,
            'offerType': 'offer',
            'position': 6,
            'extra': {
                'parentId': 0,
            },
        },
        {
            'id': 281993074,
            'offerType': 'offer',
            'position': 2,
            'extra': {
                'extended_type': [
                    'outskirts',
                ],
                'parentId': 0,
                'sutochno_feed_test': True,
                'sutochno_url': 'https://sochi.cian.ru/rent/flat/281993074/',
            },
        },
        {
            'id': 280640079,
            'offerType': 'offer',
            'position': 7,
            'extra': {
                'parentId': 0,
            },
        },
        {
            'id': 277276271,
            'offerType': 'offer',
            'position': 8,
            'extra': {
                'parentId': 0,
            },
        },
        {
            'id': 226573261,
            'offerType': 'offer',
            'position': 9,
            'extra': {
                'parentId': 0,
            },
        },
        {
            'id': 281913178,
            'offerType': 'offer',
            'position': 3,
            'extra': {
                'extended_type': [
                    'outskirts',
                ],
                'parentId': 0,
                'sutochno_feed_test': True,
                'sutochno_url': 'https://sochi.cian.ru/rent/flat/281913178/',
            },
        },
        {
            'id': 279802122,
            'offerType': 'offer',
            'position': 10,
            'extra': {
                'parentId': 0,
            },
        },
        {
            'id': 257766414,
            'offerType': 'offer',
            'position': 11,
            'extra': {
                'parentId': 0,
            },
        },
        {
            'id': 203947807,
            'offerType': 'offer',
            'position': 12,
            'extra': {
                'parentId': 15739,
            },
        },
        {
            'id': 276211018,
            'offerType': 'offer',
            'position': 13,
            'extra': {
                'parentId': 0,
                'sutochno_feed_test': True,
                'sutochno_url': 'https://sochi.cian.ru/rent/flat/276211018/',
            },
        },
        {
            'id': 282900955,
            'offerType': 'offer',
            'position': 14,
            'extra': {
                'parentId': 0,
            },
        },
        {
            'id': 284009179,
            'offerType': 'offer',
            'position': 15,
            'extra': {
                'parentId': 0,
            },
        },
        {
            'id': 278586792,
            'offerType': 'offer',
            'position': 16,
            'extra': {
                'parentId': 49744,
            },
        },
        {
            'id': 276219288,
            'offerType': 'offer',
            'position': 17,
            'extra': {
                'parentId': 0,
                'sutochno_feed_test': True,
                'sutochno_url': 'https://sochi.cian.ru/rent/flat/276219288/',
            },
        },
        {
            'id': 284152120,
            'offerType': 'offer',
            'position': 4,
            'extra': {
                'extended_type': [
                    'outskirts',
                ],
                'parentId': 8773,
            },
        },
        {
            'id': 284107259,
            'offerType': 'offer',
            'position': 18,
            'extra': {
                'parentId': 0,
            },
        },
        {
            'id': 275788700,
            'offerType': 'offer',
            'position': 19,
            'extra': {
                'parentId': 0,
            },
        },
        {
            'id': 271514311,
            'offerType': 'offer',
            'position': 20,
            'extra': {
                'parentId': 0,
                'sutochno_feed_test': True,
                'sutochno_url': 'https://sochi.cian.ru/rent/flat/271514311/',
            },
        },
        {
            'id': 273924588,
            'offerType': 'offer',
            'position': 21,
            'extra': {
                'parentId': 18095,
            },
        },
        {
            'id': 273247750,
            'offerType': 'offer',
            'position': 22,
            'extra': {
                'parentId': 15851,
            },
        },
        {
            'id': 283236041,
            'offerType': 'offer',
            'position': 23,
            'extra': {
                'parentId': 0,
            },
        },
        {
            'id': 267199041,
            'offerType': 'offer',
            'position': 24,
            'extra': {
                'parentId': 0,
                'sutochno_feed_test': True,
                'sutochno_url': 'https://sochi.cian.ru/rent/flat/267199041/',
            },
        },
    ],
}

response = requests.post('https://api.cian.ru/ebc-analytics/event-enrichment/', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"t":"pageview","v":"1","cid":"0a1794fd-5df0-4ae6-a442-e02715652c7d","dl":"https%3A%2F%2Fkrasnodar.cian.ru%2Fcat.php%3Fdeal_type%3Drent%26engine_version%3D2%26offer_type%3Dflat%26p%3D8%26region%3D4998%26type%3D2","rid":"8C6877FC-B669-11ED-8F45-0AB657FA0059","ua":"Mozilla%2F5.0%20(X11%3B%20Linux%20x86_64%3B%20rv%3A109.0)%20Gecko%2F20100101%20Firefox%2F110.0","ec":"page","ea":"newpage","el":"open","sc":{"_type":"flatrent","engine_version":{"type":"term","value":2},"region":{"type":"terms","value":[4998]},"page":{"type":"term","value":8},"for_day":{"type":"term","value":"1"}},"event":"newpage","referrer":"","join_id":"3aea4225-4d71-4e9b-8286-4913dcd9583b","user":{},"page":{"listingType":"extended","pageNumber":8,"queryString":"/cat.php?deal_type%3Drent%26engine_version%3D2%26offer_type%3Dflat%26p%3D8%26region%3D4998%26type%3D2","offersQty":14853,"siteType":"desktop","extra":{"extended_type":["outskirts"],"mlSearchSessionGuid":"804a9d8a-7edf-455f-806b-f534c072f23d","searchRequestId":"ba4fe980-4daa-4e70-bbc1-d9adda789d53"},"mlRankingGuid":"1fff580d-eab3-48d0-86ee-5e8a64e599de","mlRankingModelVersion":"v3","pageType":"Listing"},"products":[{"id":283920229,"offerType":"offer","position":1,"extra":{"parentId":0}},{"id":279751528,"offerType":"offer","position":2,"extra":{"parentId":0}},{"id":281308015,"offerType":"offer","position":3,"extra":{"parentId":8775}},{"id":270897941,"offerType":"offer","position":1,"extra":{"extended_type":["outskirts"],"parentId":0,"sutochno_feed_test":true,"sutochno_url":"https://sochi.cian.ru/rent/flat/270897941/"}},{"id":255459067,"offerType":"offer","position":4,"extra":{"parentId":149284}},{"id":276707322,"offerType":"offer","position":5,"extra":{"parentId":0}},{"id":279354088,"offerType":"offer","position":6,"extra":{"parentId":0}},{"id":281993074,"offerType":"offer","position":2,"extra":{"extended_type":["outskirts"],"parentId":0,"sutochno_feed_test":true,"sutochno_url":"https://sochi.cian.ru/rent/flat/281993074/"}},{"id":280640079,"offerType":"offer","position":7,"extra":{"parentId":0}},{"id":277276271,"offerType":"offer","position":8,"extra":{"parentId":0}},{"id":226573261,"offerType":"offer","position":9,"extra":{"parentId":0}},{"id":281913178,"offerType":"offer","position":3,"extra":{"extended_type":["outskirts"],"parentId":0,"sutochno_feed_test":true,"sutochno_url":"https://sochi.cian.ru/rent/flat/281913178/"}},{"id":279802122,"offerType":"offer","position":10,"extra":{"parentId":0}},{"id":257766414,"offerType":"offer","position":11,"extra":{"parentId":0}},{"id":203947807,"offerType":"offer","position":12,"extra":{"parentId":15739}},{"id":276211018,"offerType":"offer","position":13,"extra":{"parentId":0,"sutochno_feed_test":true,"sutochno_url":"https://sochi.cian.ru/rent/flat/276211018/"}},{"id":282900955,"offerType":"offer","position":14,"extra":{"parentId":0}},{"id":284009179,"offerType":"offer","position":15,"extra":{"parentId":0}},{"id":278586792,"offerType":"offer","position":16,"extra":{"parentId":49744}},{"id":276219288,"offerType":"offer","position":17,"extra":{"parentId":0,"sutochno_feed_test":true,"sutochno_url":"https://sochi.cian.ru/rent/flat/276219288/"}},{"id":284152120,"offerType":"offer","position":4,"extra":{"extended_type":["outskirts"],"parentId":8773}},{"id":284107259,"offerType":"offer","position":18,"extra":{"parentId":0}},{"id":275788700,"offerType":"offer","position":19,"extra":{"parentId":0}},{"id":271514311,"offerType":"offer","position":20,"extra":{"parentId":0,"sutochno_feed_test":true,"sutochno_url":"https://sochi.cian.ru/rent/flat/271514311/"}},{"id":273924588,"offerType":"offer","position":21,"extra":{"parentId":18095}},{"id":273247750,"offerType":"offer","position":22,"extra":{"parentId":15851}},{"id":283236041,"offerType":"offer","position":23,"extra":{"parentId":0}},{"id":267199041,"offerType":"offer","position":24,"extra":{"parentId":0,"sutochno_feed_test":true,"sutochno_url":"https://sochi.cian.ru/rent/flat/267199041/"}}]}'
#response = requests.post('https://api.cian.ru/ebc-analytics/event-enrichment/', cookies=cookies, headers=headers, data=data)

with open(f'cian.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, ensure_ascii=False)