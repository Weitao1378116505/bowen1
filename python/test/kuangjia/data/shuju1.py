import xlrd

def shuju1():
    bb=[]
    f=xlrd.open_workbook(r'C:\开大\test\kuangjia\data\qingqiu.xlsx')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        bb.append(sheet.row_values(i))
    return bb


if __name__=="__main__":
    shuju1()
#     print(shuju())