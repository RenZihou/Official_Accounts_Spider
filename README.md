# Official_Accounts_Spider
### 爬取一些公众号文章，将其储存到本地以便日后查询、检索
***
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
3. 难点：在不被封禁的情况下动态加载全部目录【我自己手动尝试，加载到第50个就被封了...qwq】
4. 就在刚才动态加载的过程中，每篇文章的url已经存在于response中了，只需按照
```Python
for i in range(0, 10):
    urls.append(response_data['general_msg_list']['list'][i]['app_msg_ext_info']['content_url'])
```
的循环，把全部response中的url提取出来即可，为了方便后期管理还可以将标题等也保存下来：
```Python
for i in range(0,10):
    urls.append({
      'title':response_data['general_msg_list']['list'][i]['app_msg_ext_info']['title'],
      'url':response_data['general_msg_list']['list'][i]['app_msg_ext_info']['content_url']
    })
```
5. 如果真的走到了这一步，一切就都好办了。只需要把上述urls里的文章一片片保存就可以了，而且，这些url是永久的（不同于历史记录的url总在变），
甚至不需要cookies就能查看。因而，总能把文章保存下来了，至于格式就根据个人需求选择了。
