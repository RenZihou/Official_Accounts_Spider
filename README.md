# Official_Accounts_Spider
### 爬取一些公众号文章，将其储存到本地以便日后查询、检索

---

#### 主要功能：
* 1，将公众号的全部历史文章爬取下来
* 2，每周更新文章
* 3，在本地以一定格式进行储存并建立索引
* 4，查询

#### 实现：
* 常见爬虫方法：
1. 搜狗搜索，最简洁但只能显示最近十条文章，故用于更新方法
2. 网页爬取，能做到爬取全部文章但较繁琐，故用于最开始
3. 自己创建一个公号，用其中的引用方法查看全部文章，最麻烦，不用

* 爬虫思路：

1. 登陆微信，并指定port，然后通过某种操作发送历史记录的请求（必须在微信程序内完成）
2. 获取历史记录的url：访问上述port下的json，提取其中的url即可
3. 难点：在不被封禁的情况下动态加载全部目录，需要慢慢摸索最佳sleep时间
4. 就在刚才动态加载的过程中，每篇文章的url已经存在于response中了，只需按照
```Python
for i in range(0, 10):
    urls.append(response_data['general_msg_list']['list'][i]['app_msg_ext_info']['content_url'])
```
的循环，把全部response中的url提取出来即可，为了方便后期管理还可以将标题等也保存下来：
```Python
for i in range(0, 10):
    urls.append({
      'title':response_data['general_msg_list']['list'][i]['app_msg_ext_info']['title'],
      'url':response_data['general_msg_list']['list'][i]['app_msg_ext_info']['content_url']
    })
```
5. 如果真的走到了这一步，一切就都好办了。只需要把上述urls里的文章一片片保存就可以了，而且，这些url是永久的（不同于历史记录的url总在变），
甚至不需要cookies就能查看。因而，总能把文章保存下来了，至于格式就根据个人需求选择了。

---

* 附：爬虫第三步的response格式：
	> {  
	"ret":0,  
	"errmsg":"ok",【如果不是ok的话就是被封了...】  
	"msg_count":10,【发送的目录数量，一般是10】  
	"can_msg_continue":1,【1表示没有加载完，可以继续加载】  
	"general_msg_list":  
	&emsp;{"list":[  
	&emsp;&emsp;{  
	&emsp;&emsp;&emsp;"comm_msg_info":{  
	&emsp;&emsp;&emsp;&emsp;"id":1000000000,【公众号的文章编码，即xpath中的id】  
	&emsp;&emsp;&emsp;&emsp;"type":49,  
	&emsp;&emsp;&emsp;&emsp;"datetime":0000000000,【时间戳】  
	&emsp;&emsp;&emsp;&emsp;"fakeid":"0000000000",【用户对应的，每人只有一个】  
	&emsp;&emsp;&emsp;&emsp;"status":2,【状态码】  
	&emsp;&emsp;&emsp;&emsp;"content":""  
	&emsp;&emsp;&emsp;},  
	&emsp;&emsp;&emsp;"app_msg_ext_info":{  
	&emsp;&emsp;&emsp;&emsp;"title":"...",【主标题】  
	&emsp;&emsp;&emsp;&emsp;"digest":"...",【副标题】  
	&emsp;&emsp;&emsp;&emsp;"content":"",  
	&emsp;&emsp;&emsp;&emsp;"fileid":000000000,【在全部公众号中的文章id】  
	&emsp;&emsp;&emsp;&emsp;"content_url":"...",  【文章url，不变（其中的scene参数会变，但不影响文章）】  
	&emsp;&emsp;&emsp;&emsp;"source_url":"",  
	&emsp;&emsp;&emsp;&emsp;"cover":"..."【封面图片url，不变】  
	&emsp;&emsp;&emsp;&emsp;"subtype":9,  
	&emsp;&emsp;&emsp;&emsp;"is_multi":0,  
	&emsp;&emsp;&emsp;&emsp;"multi_app_msg_item_list":[],  
	&emsp;&emsp;&emsp;&emsp;"author":"...",【作者】  
	&emsp;&emsp;&emsp;&emsp;"copyright_stat":11,  
	&emsp;&emsp;&emsp;&emsp;"duration":0,  
	&emsp;&emsp;&emsp;&emsp;"del_flag":1,【1表示未被删除】  
	&emsp;&emsp;&emsp;&emsp;"item_show_type":0,  
	&emsp;&emsp;&emsp;&emsp;"audio_fileid":0,  
	&emsp;&emsp;&emsp;&emsp;"play_url":"",  
	&emsp;&emsp;&emsp;&emsp;"malicious_title_reason_id":0,  
	&emsp;&emsp;&emsp;&emsp;"malicious_content_type":0  
	&emsp;&emsp;&emsp;}  
	&emsp;&emsp;},【此处还应有9篇文章，简洁起见略】  
	&emsp;]},  
	"next_offset":20,【下一次请求起始文章，每次请求+10】  
	"video_count":0,  
	"use_video_tab":0,  
	"real_type":0,  
	"home_page_list":[]  
	}  

* 附：动态页面加载的get方法参数：(注意headers中的None是要根据个人情况填上的)  
```Python
# Request headers:
headers = {
	'Accept': '*/*', 
	'Accept-Encoding': 'gzip, deflate, br', 
	'Accept-Language': 'zh-CN,zh;q=0.9', 
	'Connection': 'keep-alive', 
	'Cookie': {
		'ua_id': None, 
		'pgv_pvi': None, 
		'tvfe_boss_uuid': None, 
		'pgv_pvid': None, 
		'wxuin': None, 
		'devicetype': 'Windows10', 
		'version': None, 
		'lang': 'zh_CN', 
		'pass_ticket': None, 
		'wap_sid2': None, 
		'rewardsn': None, 
		'wxtokenkey': None
		}, 
	'Host': 'mp.weixin.qq.com', 
	'Referer': None, 
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36', 
	'X-Requested-With': 'XMLHttpRequest'
	}
# Query String Parameters:
params = {
	'action': 'getmsg', 
	'__biz': None, 
	'f': 'json', 
	'offset': None, 
	'count': '10', 
	'is_ok': '1', 
	'scene': None, 
	'uin': None, 
	'key': None, 
	'pass_ticket': None, 
	'wxtoken': None, 
	'appmsg_token': None, 
	'x5': '0'
	}
# The Get Method: 
data = requests.get(url, headers=headers, params=params)
```
* 一些注意点：
1. 由于历史记录的url是动态的，故可能会需要在一定时间后（原先url失效，具体多久还未测试）重新按照第二步的方法获取最新的url
2. headers会很重要，需要包含在get方法中（不知道为什么用的是get...）（包括：cookies，offset，user-agent等等）
