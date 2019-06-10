from urllib import request, parse
import json

"""
需求：使用爬虫，用金沙词霸翻译接口做翻译器
url：http://fy.iciba.com/
"""


def translate(word):
    url = 'http://fy.iciba.com/ajax.php?a=fy'
    form = {}
    form['f'] = 'auto'
    form['t'] = 'auto'
    form['w'] = word
    data = parse.urlencode(form).encode('utf-8')
    response = request.urlopen(url, data)
    html = response.read().decode('utf-8')
    translate_content = json.loads(html)
    try:
        for mean in translate_content['content']['word_mean']:
            return mean
    except:
        return translate_content['content']['out']


if __name__ == '__main__':
    while True:
        word = input('输入需要翻译的中/英文：')
        print(translate(word))


