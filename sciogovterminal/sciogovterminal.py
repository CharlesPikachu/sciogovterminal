'''
Function:
    在终端看中华人民共和国国务院新闻办公室
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import os
import sys
import pynput
import platform
import requests
from bs4 import BeautifulSoup


'''在终端看中华人民共和国国务院新闻办公室'''
class SciogovTerminal():
    def __init__(self, url, max_characters=1000, **kwargs):
        if not url.startswith('http://www.scio.gov.cn/'): raise ValueError('Only support url start with http://www.scio.gov.cn/')
        self.url = url
        self.max_characters = max_characters
    '''运行'''
    def run(self):
        # 爬取文章
        article_info = self.crawler(self.url)
        # 排版
        contents, cur_content = [], f'标题: {article_info["title"]}\n日期: {article_info["date"]}'
        for content in article_info['contents']:
            if len(cur_content) > self.max_characters: 
                contents.append(cur_content)
                cur_content = content
            else:
                cur_content = cur_content + '\n' + content
        # 在终端浏览
        self.clearterminal()
        self.page_pointer, self.contents = -1, contents
        print("\n\n在终端看中华人民共和国国务院新闻办公室\n\n操作简介: 输入<↑>或<←>查看上一页; 输入<↓>或<→>查看下一页; 输入<q>退出程序。\n\n作者: Charles\n\n微信公众号: Charles的皮卡丘\n\n")
        # --上一页
        def previouspage(self):
            self.page_pointer = max(0, self.page_pointer-1)
            self.clearterminal()
            print('\x1b[6;30;42m' + '分界线' + '+' * 100 + '分界线' + '\x1b[0m')
            print('\x1b[6;30;42m' + self.contents[self.page_pointer] + '\x1b[0m')
            print('\x1b[6;30;42m' + '分界线' + '+' * 100 + '分界线' + '\x1b[0m')
        # --下一页
        def nextpage(self):
            self.page_pointer = min(len(self.contents)-1, self.page_pointer+1)
            self.clearterminal()
            print('\x1b[6;30;42m' + '分界线' + '+' * 100 + '分界线' + '\x1b[0m')
            print('\x1b[6;30;42m' + self.contents[self.page_pointer] + '\x1b[0m')
            print('\x1b[6;30;42m' + '分界线' + '+' * 100 + '分界线' + '\x1b[0m')
        # --退出
        def quitsys(self):
            self.clearterminal()
            sys.exit()
        # --主循环
        while True:
            with pynput.keyboard.Events() as event:
                key = event.get()
            if hasattr(key.key, 'char'):
                if isinstance(key, pynput.keyboard.Events.Release) and key.key.char == 'q':
                    quitsys(self)
            else:
                if isinstance(key, pynput.keyboard.Events.Release) and (key.key.name == 'up' or key.key.name == 'left'):
                    previouspage(self)
                elif isinstance(key, pynput.keyboard.Events.Release) and (key.key.name == 'down' or key.key.name == 'right'):
                    nextpage(self)
            
    '''清除终端内容'''
    def clearterminal(self):
        if 'windows' in platform.system().lower():
            os.system('cls')
        else:
            os.system('clear')
    '''爬虫部分'''
    def crawler(self, url):
        # 请求链接获得内容
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        # 解析返回的内容
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        soup = soup.find('div', class_='Article')
        # --标题
        title = soup.find('div', class_='Articletitle').text.strip()
        # --时间来源
        date = soup.find('div', class_='date').text.strip()
        # --正文
        contents = []
        for item in soup.find_all('p'):
            content = item.text.strip()
            if content == '分享到：': break
            contents.append(content)
        # --整合
        article_info = {
            'title': title,
            'date': date,
            'contents': contents,
        }
        # 返回解析的内容
        return article_info


'''run'''
if __name__ == '__main__':
    client = SciogovTerminal(url='http://www.scio.gov.cn/m/37234/Document/1720965/1720965.htm')
    client.run()