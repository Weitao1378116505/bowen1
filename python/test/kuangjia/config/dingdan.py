# 所有订单配置文件

import requests

from kuangjia.data import shuju
class Ding_Dan(object):
    def cha_mingxi(self,num):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch'
        header={'Content-Type': "application/json",
                'x-dealer-code': "2100005",
                'x-position-code': "D_PO_1028",
                'x-resource-code': "pol4s_partOrderSearch_partOrderDetailSearch",
                'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
                'x-user-code': "dhxc1u",
                'x-access-token': "dcad356abf871524d1188de3bd15b985",
                'cache-control': "no-cache",
                'Postman-Token': "7564707c-3bbf-4766-adc4-013094a6b2da"}
        pyloa="{\r\n \"pageNum\":\"%d\",\r\n \"pgeSize\":\"10\",\r\n \"queryTerms\":\r\n {\r\n  \"orderNo\":\"V2100880181219390\"\r\n }\r\n}"%(num)
        res=requests.post(url=url,headers=header,data=pyloa)
        return  res.json()


if __name__=="__main__":
    shuju.shuju()
    print(shuju.shuju())
    for i in shuju.shuju():
        Ding_Dan().cha_mingxi(int(i[0]))
