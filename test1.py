#数据清洗之Excel
import pandas as pd
from pandas import Series,DataFrame

#将表格导入dataframe框架中
df = DataFrame(pd.read_excel('./data-example/data.xlsx'))

#对列进行重命名
df.rename(columns={0:'姓名',1:'性别',2:'年龄',3:'体重',4:'身高'},inplace= True)
#对整行为空的数据进行删除
df.dropna(how='all',inplace=True)
#用平均值填充体重缺失的值
df[u'体重'].fillna(int(df[u'体重'].mean()),inplace=True)

#对身高列的度量做统一
def format_height(df):
    if(df['身高']<3):
        return df['身高'] * 100
    else:
        return df['身高']
df['身高'] = df.apply(format_height,axis=1)
#姓名首字母统一改成大写
df.columns = df.columns.str.upper()

#对姓名列的非法字符做过滤
#英文名出现中文->删除非ASCII码的字符
df['姓名'].replace({r'[^\x00-\x7f]+':''},regex=True,inplace=True)
#英文名出现？和' ->删除问号和引号
df['姓名'].replace({r'\?+':''},regex=True,inplace=True)
df['姓名'].replace({r'\'+':''},regex=True,inplace=True)

#名字前出现空格->删除空格
df['姓名'] = df['姓名'].map(str.lstrip)

#将年龄的负数化成正数
def format_sex(df):
    return abs(df['年龄'])
df['年龄'] = df.apply(format_sex,axis=1)

#删除行记录重复的数据
df.drop_duplicates(['姓名'],inplace=True)

#保存清洗好的数据
df.to_excel('./data-example/data01.xlsx',index=False)




