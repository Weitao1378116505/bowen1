import requests
from kuangjia.data.MXshuju import shuju
class  MX(object):
    def mingxi(self,num):
        url= "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/electricInvoiceDetail"
        payload = "{\r\n  \"pageNum\": 1,\r\n  \"pageSize\": 10,\r\n  \"queryTerms\":\r\n  {\r\n  \t\"billingNo\":\"%s\"\r\n  }\r\n}"%(num)
        headers = {
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_electricInvoiceDetail",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "d6a5abdb98fd2ee203a4ddcd7ae47d07",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "47ad19cc-6ce9-42ec-b30d-bdc22069bc77,1f7162a0-740d-44f9-9342-a17bb024e25a",
            'Host': "mobileqa.dms.saic-gm.com",
            'cookie': "dapp.sgm.com:qa:=d6a5abdb98fd2ee203a4ddcd7ae47d07; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; dapp.sgm.com:qa:=d6a5abdb98fd2ee203a4ddcd7ae47d07; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f",
            'accept-encoding': "gzip, deflate",
            'content-length': "96",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        res = requests.post(url=url, headers=headers, data=payload)
        print(res.text)
        return res.json()
# if __name__=="__main__":
#     shuju()
#     print(shuju())
#     for i in shuju():
#         MX().mingxi(int(i[0]))