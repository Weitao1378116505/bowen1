from selenium import webdriver
from time import sleep
a=webdriver.Chrome()
a.get("https://qzone.qq.com/")
a.switch_to_frame('login_frame')
sleep(2)
a.find_element_by_xpath('//*[@id="img_out_1678665473"]').click()
sleep(2)


a.get('https://user.qzone.qq.com/572086992')
sleep(2)
a.find_element_by_xpath('//*[@id="friendship_promote_layer"]/table/tbody/tr[1]/td[2]/a').click()
# aa=a.window_handles
# a.current_window_handle(aa[-1])

sleep(1)
# a.find_element_by_xpath('//*[@id="menuContainer"]/div/ul/li[4]/a').click()
# sleep(2)
b=['   踏着祥云踩着梦那是我的盖世英雄。   ','  其实你根本就不是我喜欢的类型只是碰巧撞进了我的心。']
#  "别人口中的你有多坏我从未相信。",
# "不愿意醒来时，台灯投射在墙上只有我孤独的身影。",
#    "爱是一种遇见，不能等待，也不能准备",
   # "女人总爱找茬跟男人闹，是希望闹过之后他能心存歉意，对她更好些。进入恋爱之前，女人都可以淑女，一旦自认抓牢了男人，她开始对他刁蛮任性。她不是脾气不好，她只是用“发脾气”来证明自己的拥有。当女人开始生出折腾他的欲望，说明，她真的爱上了",
   # "世界这么大，能遇见，不容易。",
   # "我打算爱你很久很久 没有想要放弃的念头",
   # "找不到坚持下去的理由，那就找一个重新开始的理由，生活本来就这么简单。避免失望的最好办法，就是不寄希望于任何人、任何事。人生是一场相逢，又是一场遗忘，最终我们都会成为岁月里的风景。",
   # "你的微笑像是子弹先是击穿我的胸膛 再射入心脏。"]
for i in b:
    a.find_element_by_xpath('//*[@id="pageContent"]/div[1]/div[3]/div/div[2]/div[1]/div/b/b/textarea').send_keys(i)
    sleep(8)
    # js = "var q=document.documentElement.scrollTop=0"
    # a.execute_script(js)
    # sleep(3)
    # a.find_element_by_xpath('//*[@id="pageContent"]/div[1]/div[3]/div/div[2]/div[1]/div/b/b/textarea').send_keys(i)
    # sleep(3)
    a.find_element_by_xpath('//*[@id="pageContent"]/div[1]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]/a')
    sleep(3)
