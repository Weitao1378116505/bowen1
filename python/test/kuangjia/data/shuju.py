import xlrd

def shuju():
    aa=[]
    f=xlrd.open_workbook(r'C:\开大\test\kuangjia\data\dingdan.xlsx')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        aa.append(sheet.row_values(i))
    return aa

if __name__=="__main__":
    shuju()
#     print(shuju())