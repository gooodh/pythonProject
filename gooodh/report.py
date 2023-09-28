
from bs4 import BeautifulSoup

import requests

import json
import csv
from datetime import datetime

cur_time = datetime.now().strftime('%d_%m_%Y_%H_%M')

def get_result():
    with open('report.txt', encoding='utf-8') as file:
        for line in file:
            if 'Произошла ошибка' in line:
                lists = line.split('Кадастровый номер:', 1)
                for lin in lists:
                    print(lin.split('Произошла ошибка:', 0))
    
    
    
if __name__ == '__main__':
   
    # get_source_html()
    get_result()