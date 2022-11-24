import re
from typing import List, Iterable
import requests


if __name__ == '__main__':
    url: str = input('Сюда скопируйте URL сайта: ')
    rec_links = requests.get(url).text
    pattern: str = r'(<h3.*>)(.*)(<.*h3>)'
    tag_iter: Iterable = re.finditer(pattern, rec_links)
    tag_list: List = list(map(lambda mach_obj: mach_obj.group(2), tag_iter))
    print(tag_list)
