import requests
import json


def get_data():

    cookies = {
        'SMSError': '',
        'authError': '',
        'SMSError': '',
        'authError': '',
        'MVID_GUEST_ID': '21697382951',
        'BIGipServeratg-ps-prod_tcp80': '2416237578.20480.0000',
        '_ym_d': '1666855387',
        '_ym_uid': '1666855387547000238',
        '_ga': 'GA1.3.1666855387.1666855387',
        '_gid': 'GA1.3.1666855387.1666855387',
        'sub_id1_c': '99333',
        'sub_id2_c': 'b31cbb10202d9d3eb2c802bc68054a30dcd87a3d',
        'partnerSrc': 'advcake',
        'advcake_click_id': 'b31cbb10202d9d3eb2c802bc68054a30dcd87a3d',
        'advcake_utm_partner': '99333',
        'advcake_utm_webmaster': 'gdeslon',
        '__cpatrack': 'advcake_cpa',
        '__SourceTracker': 'advcake__cpa',
        'admitad_deduplication_cookie': 'advcake__cpa',
        '__allsource': 'advcake',
        '__sourceid': 'advcake',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_content%3Dgdeslon%26utm_medium%3Dcpa%26utm_source%3Dadvcake%26utm_campaign%3D99333%26advcake_params%3Db31cbb10202d9d3eb2c802bc68054a30dcd87a3d%26sub_id1%3D99333%26sub_id2%3Db31cbb10202d9d3eb2c802bc68054a30dcd87a3d',
        'advcake_track_id': '23276f9f-b0fb-3591-e238-001fa650f0b9',
        'advcake_session_id': '27598b68-bc41-ef2f-471e-8c66c66db40f',
        '__lhash_': 'abd4491263a1f9f1366e98c16e91ab25',
        '__zzatgib-w-mvideo': 'MDA0dBA=Fz2+aQ==',
        '__zzatgib-w-mvideo': 'MDA0dBA=Fz2+aQ==',
        'deviceType': 'desktop',
        'cfidsgib-w-mvideo': 'BeN62z4BCE7cidwN0yfDsWKElpWExoyUHWfaqlSDGVDC6Nyod9Vw+wE08ZfDTZz8mqQrRAoFZSB3oWfkvcmgZE8Ci4JG6qz0So4VQNfNniJr1PwkdND7YwRMldbHOJqTi5euqI7RePGT1HDP3g7xTjahDPMqebVH7OGLQQ==',
        'cfidsgib-w-mvideo': 'BeN62z4BCE7cidwN0yfDsWKElpWExoyUHWfaqlSDGVDC6Nyod9Vw+wE08ZfDTZz8mqQrRAoFZSB3oWfkvcmgZE8Ci4JG6qz0So4VQNfNniJr1PwkdND7YwRMldbHOJqTi5euqI7RePGT1HDP3g7xTjahDPMqebVH7OGLQQ==',
        'gsscgib-w-mvideo': 'YaUx8as72vVZ+FL/7+9Eq9OOkGMyBYWqjXkORskjgSENtUrmv0qSEqCxQyEuHItxhb3z4QcgmeMM7vxdR3eHvyr5XEv5oB9cdudOikAu5/0nzouHEitxGYNnNq/V4lYmlbrRo5STsvKrIFv1OinVtC85fEEQSqWUfVy2Ifa/D3b9MTP2pnWilG6R7inrdI9Mfy8+SN9dEgrJR4Cj9grcePisK/MVtCTzC0MeyaF2Iw82JGPpo9KthXN3WvZVZg==',
        'gsscgib-w-mvideo': 'YaUx8as72vVZ+FL/7+9Eq9OOkGMyBYWqjXkORskjgSENtUrmv0qSEqCxQyEuHItxhb3z4QcgmeMM7vxdR3eHvyr5XEv5oB9cdudOikAu5/0nzouHEitxGYNnNq/V4lYmlbrRo5STsvKrIFv1OinVtC85fEEQSqWUfVy2Ifa/D3b9MTP2pnWilG6R7inrdI9Mfy8+SN9dEgrJR4Cj9grcePisK/MVtCTzC0MeyaF2Iw82JGPpo9KthXN3WvZVZg==',
        'fgsscgib-w-mvideo': 'lUAz213a981351bf5c28f73c46dbfaa155d4d7a8',
        'fgsscgib-w-mvideo': 'lUAz213a981351bf5c28f73c46dbfaa155d4d7a8',
        'afUserId': 'aa2152e7-26f2-4c38-b60c-a04835c45fcc-p',
        'cfidsgib-w-mvideo': 'qI0pOrJ8u8U8yVDd1XmleWPx1E5MArEMlyDe+wKcHfA/KZw1PpDJF1RAKdn9tvldIHt9KPGxjlYIGrwGD+9cG1L6CjUsLyU/8+bKuPKOMXphZ5H3u0cnyhtFUAstZudM6Cc0BbktWOyXCYLzu5NoR4JaXVMU8EYkU8YMyg==',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'MVID_AB_PDP_CHAR': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_2246',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '5400000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '29',
        'MVID_REGION_SHOP': 'S955',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TIMEZONE_OFFSET': '7',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'bIPs': '1949759381',
        'flacktory': 'no',
        'searchType2': '2',
        'uxs_uid': '55caaf00-55c8-11ed-a2a5-15d71f503181',
        'AF_SYNC': '1666855445493',
        'tmr_lvid': 'd563f20f9efe5e4d0943c65204a50029',
        'tmr_lvidTS': '1666855502503',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '97777d67-cc34-40d8-8e1c-d27edcd05019',
        'flocktory-uuid': '9ec87e83-2be4-408e-9697-dd2c3fdf9c9b-4',
        '_gid': 'GA1.2.1666855387.1666855387',
        'SMSError': '',
        'authError': '',
        '_sp_ses.d61c': '*',
        '_ym_isad': '2',
        'MVID_AB_TOP_SERVICES': '1',
        '__ttl__widget__ui': '1667034472208-46c879ebd6d2',
        'cookie_ip_add': '5.166.107.202',
        '_ga': 'GA1.2.1666855387.1666855387',
        'tmr_detect': '0%7C1667034751972',
        'JSESSIONID': 'KwNjjcvLTTCvpL2zJgyGLc8QQYGspwzDwhpZqBjy5k2N8pBSkkpl!-632423972',
        'tmr_reqNum': '234',
        '_ga_CFMZTSS5FM': 'GS1.1.1667033606.6.1.1667035055.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1667033608.6.1.1667035055.49.0.0',
        'mindboxDeviceUUID': 'f7ec0b89-4867-41a2-a3a5-1c00bf303d46',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22f7ec0b89-4867-41a2-a3a5-1c00bf303d46%22%7D',
        '_sp_id.d61c': 'f33d5e8c-f2c0-4c3c-bf5a-3c728aa70dee.1666855440.3.1667035063.1666957932.b6f801a0-a2e4-42d3-836f-d9bd4a97019b.d0f937b6-9f0c-4a79-8862-225ae24ee45f.9dbc61e7-1cbf-4edc-a33a-cd2477e122eb.1667033603377.60',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'SMSError=; authError=; SMSError=; authError=; MVID_GUEST_ID=21697382951; BIGipServeratg-ps-prod_tcp80=2416237578.20480.0000; _ym_d=1666855387; _ym_uid=1666855387547000238; _ga=GA1.3.1666855387.1666855387; _gid=GA1.3.1666855387.1666855387; sub_id1_c=99333; sub_id2_c=b31cbb10202d9d3eb2c802bc68054a30dcd87a3d; partnerSrc=advcake; advcake_click_id=b31cbb10202d9d3eb2c802bc68054a30dcd87a3d; advcake_utm_partner=99333; advcake_utm_webmaster=gdeslon; __cpatrack=advcake_cpa; __SourceTracker=advcake__cpa; admitad_deduplication_cookie=advcake__cpa; __allsource=advcake; __sourceid=advcake; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_content%3Dgdeslon%26utm_medium%3Dcpa%26utm_source%3Dadvcake%26utm_campaign%3D99333%26advcake_params%3Db31cbb10202d9d3eb2c802bc68054a30dcd87a3d%26sub_id1%3D99333%26sub_id2%3Db31cbb10202d9d3eb2c802bc68054a30dcd87a3d; advcake_track_id=23276f9f-b0fb-3591-e238-001fa650f0b9; advcake_session_id=27598b68-bc41-ef2f-471e-8c66c66db40f; __lhash_=abd4491263a1f9f1366e98c16e91ab25; __zzatgib-w-mvideo=MDA0dBA=Fz2+aQ==; __zzatgib-w-mvideo=MDA0dBA=Fz2+aQ==; deviceType=desktop; cfidsgib-w-mvideo=BeN62z4BCE7cidwN0yfDsWKElpWExoyUHWfaqlSDGVDC6Nyod9Vw+wE08ZfDTZz8mqQrRAoFZSB3oWfkvcmgZE8Ci4JG6qz0So4VQNfNniJr1PwkdND7YwRMldbHOJqTi5euqI7RePGT1HDP3g7xTjahDPMqebVH7OGLQQ==; cfidsgib-w-mvideo=BeN62z4BCE7cidwN0yfDsWKElpWExoyUHWfaqlSDGVDC6Nyod9Vw+wE08ZfDTZz8mqQrRAoFZSB3oWfkvcmgZE8Ci4JG6qz0So4VQNfNniJr1PwkdND7YwRMldbHOJqTi5euqI7RePGT1HDP3g7xTjahDPMqebVH7OGLQQ==; gsscgib-w-mvideo=YaUx8as72vVZ+FL/7+9Eq9OOkGMyBYWqjXkORskjgSENtUrmv0qSEqCxQyEuHItxhb3z4QcgmeMM7vxdR3eHvyr5XEv5oB9cdudOikAu5/0nzouHEitxGYNnNq/V4lYmlbrRo5STsvKrIFv1OinVtC85fEEQSqWUfVy2Ifa/D3b9MTP2pnWilG6R7inrdI9Mfy8+SN9dEgrJR4Cj9grcePisK/MVtCTzC0MeyaF2Iw82JGPpo9KthXN3WvZVZg==; gsscgib-w-mvideo=YaUx8as72vVZ+FL/7+9Eq9OOkGMyBYWqjXkORskjgSENtUrmv0qSEqCxQyEuHItxhb3z4QcgmeMM7vxdR3eHvyr5XEv5oB9cdudOikAu5/0nzouHEitxGYNnNq/V4lYmlbrRo5STsvKrIFv1OinVtC85fEEQSqWUfVy2Ifa/D3b9MTP2pnWilG6R7inrdI9Mfy8+SN9dEgrJR4Cj9grcePisK/MVtCTzC0MeyaF2Iw82JGPpo9KthXN3WvZVZg==; fgsscgib-w-mvideo=lUAz213a981351bf5c28f73c46dbfaa155d4d7a8; fgsscgib-w-mvideo=lUAz213a981351bf5c28f73c46dbfaa155d4d7a8; afUserId=aa2152e7-26f2-4c38-b60c-a04835c45fcc-p; cfidsgib-w-mvideo=qI0pOrJ8u8U8yVDd1XmleWPx1E5MArEMlyDe+wKcHfA/KZw1PpDJF1RAKdn9tvldIHt9KPGxjlYIGrwGD+9cG1L6CjUsLyU/8+bKuPKOMXphZ5H3u0cnyhtFUAstZudM6Cc0BbktWOyXCYLzu5NoR4JaXVMU8EYkU8YMyg==; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_2246; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=5400000100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=29; MVID_REGION_SHOP=S955; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TIMEZONE_OFFSET=7; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; bIPs=1949759381; flacktory=no; searchType2=2; uxs_uid=55caaf00-55c8-11ed-a2a5-15d71f503181; AF_SYNC=1666855445493; tmr_lvid=d563f20f9efe5e4d0943c65204a50029; tmr_lvidTS=1666855502503; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=97777d67-cc34-40d8-8e1c-d27edcd05019; flocktory-uuid=9ec87e83-2be4-408e-9697-dd2c3fdf9c9b-4; _gid=GA1.2.1666855387.1666855387; SMSError=; authError=; _sp_ses.d61c=*; _ym_isad=2; MVID_AB_TOP_SERVICES=1; __ttl__widget__ui=1667034472208-46c879ebd6d2; cookie_ip_add=5.166.107.202; _ga=GA1.2.1666855387.1666855387; tmr_detect=0%7C1667034751972; JSESSIONID=KwNjjcvLTTCvpL2zJgyGLc8QQYGspwzDwhpZqBjy5k2N8pBSkkpl!-632423972; tmr_reqNum=234; _ga_CFMZTSS5FM=GS1.1.1667033606.6.1.1667035055.0.0.0; _ga_BNX5WPP3YK=GS1.1.1667033608.6.1.1667035055.49.0.0; mindboxDeviceUUID=f7ec0b89-4867-41a2-a3a5-1c00bf303d46; directCrm-session=%7B%22deviceGuid%22%3A%22f7ec0b89-4867-41a2-a3a5-1c00bf303d46%22%7D; _sp_id.d61c=f33d5e8c-f2c0-4c3c-bf5a-3c728aa70dee.1666855440.3.1667035063.1666957932.b6f801a0-a2e4-42d3-836f-d9bd4a97019b.d0f937b6-9f0c-4a79-8862-225ae24ee45f.9dbc61e7-1cbf-4edc-a33a-cd2477e122eb.1667033603377.60',
        'pragma': 'no-cache',
        'referer': 'https://www.mvideo.ru/product-list-page?q=30062056',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://www.mvideo.ru/bff/products/listing?categoryId=118&offset=0&limit=24&filterParams=WyJza2lka2EiLCIiLCJkYSJd&filterParams=WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==&doTranslit=true',
        cookies=cookies, headers=headers).json()

    # response = requests.get(
    #     'https://www.mvideo.ru/bff/products/listing?categoryId=118&offset=0&limit=24&filterParams=WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==&doTranslit=true',
    #     params=params,
    #     cookies=cookies, headers=headers).json()

    products_ids = response.get('body').get('products')

    # with open(f'index.html', 'w', encoding='utf-8') as file:
    #     file.write(response.text)


    with open('1_products_ids.json', 'w', encoding='utf-8') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()
    with open('2_items.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
    # print(len(response.get('body').get('products')))

    products_ids_str = ','.join(products_ids)



    response = requests.get(f'https://www.mvideo.ru/bff/products/prices?productIds={products_ids_str}&addBonusRubles=true&isPromoApplied=true', cookies=cookies, headers=headers).json()

    with open('3_prices.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
#
#     items_prices = {}
#
#     material_prices = response.get('body').get('materialPrices')
#
#     for item in material_prices:
#         item_id = item.get('price').get('productId')
#         item_base_price = item.get('price').get('basePrice')
#         item_sale_price = item.get('price').get('salePrice')
#         item_bonus = item.get('bonusRubles').get('total')
#
#         items_prices[item_id] = {
#             'item_basePrice': item_base_price,
#             'item_salePrice': item_sale_price,
#             'item_bonus': item_bonus
#         }
#
#     with open('4_items_prices.json', 'w', encoding='utf-8') as file:
#         json.dump(items_prices, file, indent=4, ensure_ascii=False)
#
#
# def get_result():
#     with open('2_items.json', encoding='utf-8') as file:
#         products_data = json.load(file)
#
#     with open('4_items_prices.json', encoding='utf-8') as file:
#         products_prices = json.load(file)
#
#     products_data = products_data.get('body').get('products')
#
#     for item in products_data:
#         product_id = item.get('productId')
#
#         if product_id in products_prices:
#             prices = products_prices[product_id]
#
#         item['item_basePrice'] = prices.get('item_basePrice')
#         item['item_salePrice'] = prices.get('item_salePrice')
#         item['item_bonus'] = prices.get('item_bonus')
#
#     with open('5_result.json', 'w', encoding='utf-8') as file:
#         json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    # get_result()


if __name__ == '__main__':
    main()
