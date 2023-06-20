import requests
import json
BVID = input('请输入bv号(BVxxxxxx)：')
url = 'https://api.bilibili.com/x/web-interface/view?bvid=' + BVID
res = requests.get(url)
jsdata = json.loads(res.content.decode('utf-8'))
data = jsdata['data']
stat = data['stat']
print ('标题：', data['title'])
print('播放量：', stat['view'])
print('弹幕：', stat['danmaku'])
print('点赞：', stat['like'])
print('投币：', stat['coin'])
print('分享：', stat['share'])