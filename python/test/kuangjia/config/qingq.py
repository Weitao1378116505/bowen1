import requests
from kuangjia.data.shuju1 import shuju1
class  QQ(object):
    def qing(self,bb):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch'
        paylo ="{\r\n \"pageNum\":\"%d\",\r\n \"pgeSize\":\"10\",\r\n \"queryTerms\":\r\n {\r\n  \"orderNo\":\"V2100880181219390\"\r\n }\r\n}"%(bb)
        header = {
            'Content-Type': "application/json",
            'x-dealer-code': "2100005",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrderSearch_partOrderDetailSearch",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "dcad356abf871524d1188de3bd15b985",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "e76ccddb-d301-460a-b039-3543c337b9ce,ba146151-c967-4632-963a-8fb91b9fb12a",
            'Host': "mobileqa.dms.saic-gm.com",
            'cookie': "dapp.sgm.com:qa:=45729e0e8d5bc30df68c5567cb654724; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; dapp.sgm.com:qa:=45729e0e8d5bc30df68c5567cb654724; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f",
            'accept-encoding': "gzip, deflate",
            'content-length': "96",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        res = requests.post(url=url, headers=header, data=paylo)
        return res.json()
if __name__=="__main__":
    shuju1()
    print(shuju1())
    for i in shuju1():
        QQ().qing(int(i[0]))