import requests
import bs4
import re
import json
 
def open(keywords, page):
      headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
 
      payload = {'q':keywords, 'sort':"sale-desc", 's':(page-1)*44}
      url = "https://s.taobao.com/search"
 
      res = requests.get(url, params = payload)
      return res
      
      
def get_item(res):
 
      g_page_config = re.search(r'g_page_config = (.*?);\n', res.text)
      page_config_json = json.loads(g_page_config.group(1))
      page_item = page_config_json['mods']['itemlist']['data']['auctions']
 
      result = []#��������ǹ�ע����Ϣ(ID,���⣬���ӣ��ۼۣ��������̼�)
      for each in page_item:
            dict1 = dict.fromkeys(('id','name',,'price'))
            dict1['id'] = each['nid']
            dict1['name'] = each['title']
            dict1['price'] = each['detail_url']
            result.append(dict1)
 
      return result
            
def count_sales(items):
      count = 0
      for each in items:
            if '###' in each['title']:#�涨ֻȡ�����С�###������Ʒ
                  count += int(re.search(r'\d+',each['sale']).group())
                  
      return count
 
def main():
 
      keywords = input("�����������ؼ��ʣ�")#����Ϊ������Ʒ����
      length = 10#�Ա���Ʒҳ��
      total = 0
      
      for each in range(length):
            res = open(keywords, each+1)
            items = get_item(res)
            total += count_sales(items)#��������
      print(total)
 
 
if __name__ == "__main__":
      main()