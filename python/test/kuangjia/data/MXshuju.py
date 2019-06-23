import xlrd

def shuju():
    bb=[]
    f=xlrd.open_workbook(r'C:\开大\test\kuangjia\data\MX.xlsx')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        bb.append(sheet.row_values(i))
    print(bb)
    return bb


if __name__=="__main__":
    shuju()