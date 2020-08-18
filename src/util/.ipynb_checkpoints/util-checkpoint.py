from glob import glob
import pandas as pd

pd.options.display.max_columns = None
pd.options.display.float_format = '{:.2f}'.format


class SD:

    def __init__(self):
        self.__PATH = '../data/sd/'
        self.__COLUMNS = ['Customer_Code(GAW)', 'Product_Code', 'Inner_Code',
                          '分析コード', 'Ship_Complete_Date', 'SO_Date',
                          'Supplier_Code(GAW)', 'SO_Quantity',
                          'Sales_Amount(Subsidiary_Currency)',
                          'Purchase_Amount(Subsidiary_Currency)',
                          'MONTH', '年度']
        self.__RENAMED = ['CustCode', 'ProductCode', 'InnerCode',
                          'ClassifyCode', 'Ssd', 'SoDate',
                          'SupplierCode', 'Qty',
                          'Sales',
                          'Purchase',
                          'Month', 'Year']

    def get_SD(self, year):
        '''
        year range is FY15 to FY19
        '''
        path = glob(self.__PATH + '*' + year + '*')[0]
        sd = pd.read_csv(path, dtype=object, sep='\t', encoding='utf_8',
                         usecols=self.__COLUMNS)
        renamed = {col: re for col, re in zip(self.__COLUMNS, self.__RENAMED)}
        sd = sd.rename(columns=renamed)
        sd = sd.astype({'Qty': int, 'Sales': float, 'Purchase': float})
        sd['Rec'] = 1
        return sd
    
    def get_SDs(self, years):
        '''
        years must be list, for example ['FY15', 'FY16']
        '''
        sds = []
        for year in years:
            sd = self.get_SD(year)
            sds.append(sd)
        
        sds = pd.concat(sds)
        return sds


class SO:

    def __init__(self):
        self.__PATH = '../data/so/'
        self.__COLUMNS = ['CUST_CD', 'PRODUCT_CD', 'INNER_CD',
                          'CLASSIFY_CD', 'VIA_SHIP_DATE', 'SO　DATE',
                          'SUPPLIER_CD', 'SO_QTY',
                          'EXCLUDE_TAX_SALES_AMOUNT_RMB',
                          'PURCHASE_AMOUNT_RMB',
                          'Month']
        self.__RENAMED = ['CustCode', 'ProductCode', 'InnerCode',
                          'ClassifyCode', 'Ssd', 'SoDate',
                          'SupplierCode', 'Qty',
                          'Sales',
                          'Purchase',
                          'Month']

    def get_SO(self, year):
        '''
        year range is FY17 to FY19
        '''
        path = glob(self.__PATH + '*' + year + '*')[0]
        so = pd.read_csv(path, dtype=object, sep='\t', encoding='utf_8',
                         usecols=self.__COLUMNS)
        renamed = {col: re for col, re in zip(self.__COLUMNS, self.__RENAMED)}
        so = so.rename(columns=renamed)
        so = so.astype({'Qty': int, 'Sales': float, 'Purchase': float})
        return so

    
class ClassifyCode:
    
    def __init__(self):
        self.__PATH = '../data/mst/ClassifyCode.xlsx'
    
    def get_master(self):
        classify_code = pd.read_excel(self.__PATH, dtype=object)
        return classify_code

    
class Customer:
    
    def __init__(self):
        self.__PATH = '../data/mst/CustomerSegment.xlsx'
    
    def get_master(self):
        customer = pd.read_excel(self.__PATH, dtype=object)
        return customer
