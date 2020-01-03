#%%
import pandas as pd

cctv_seoul = pd.read_excel('/Users/nani/Desktop/GitHub/DataScience/01_Seoul_CCTV/CCTV_in_Seoul.xlsx')
cctv_seoul.head()

# %%
#pop_seoul = pd.read_excel('/Users/nani/Desktop/GitHub/DataScience/01_Seoul_CCTV/population_in_Seoul.xls')
pop_seoul = pd.read_excel('/Users/nani/Desktop/GitHub/DataScience/01_Seoul_CCTV/population_in_Seoul.xls',
header=2, parse_cols='B,D,G,J,N')
pop_seoul.head()

# %%
cctv_seoul.columns

# %%
pop_seoul.columns

# %%
cctv_seoul.rename(columns={cctv_seoul.columns[0] : '구별'}, inplace=True)
cctv_seoul.head()

# %%
pop_seoul.rename(columns={pop_seoul.columns[0] : '구별',
pop_seoul.columns[1] : '인구수',
pop_seoul.columns[2] : '한국인',
pop_seoul.columns[3] : '외국인',
pop_seoul.columns[4] : '고령자'}, inplace=True)
pop_seoul.head()


# %%
import pandas as pd
import numpy as np      

s = pd.Series([1,3,5,np.nan,6,8])
s
# pandas의 데이터 유형 중 기초가 되는 것이 Series이다.
# 대괄호로 만들고, list 데이터로 만들 수 있다.

# %%
dates = pd.date_range('20200101', periods=6)
dates
# 날짜형 데이터인 date_range
# 기본 날짜를 지정하고 periods 옵션으로 6일간이라고 지정한다.

# %%
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A','B','C','D'])
df
# DataFrame 유형의 데이터를 만든다.
# 6행 4열의 random 변수를 만들고, 컬럼에는 A,B,C,D를 넣고, 인덱스(행)는 dates 만든거를 넣는다.

# %%
df.index

# %%
df.columns

# %%
df.values

# %%
df.info()

# %%
df.describe()

# %%
df.sort_values(by='B', ascending=False)

# %%
df

# %%
df['A']

# %%
df[0:3]

# %%
df['2020-01-02':'20200104']

# %%
df.loc[dates[0]]
# loc는 location 옵션으로 슬라이싱할 때 loc 옵션을 이용해서 위치 값을 지정할 수 있다.

# %%
df.loc[:,['A','B']]

# %%
df.loc['20200102':'20200104',['A','C']]

# %%
df.loc['20200102':'20200104',['A','B']]

# %%
df.loc['20200102',['A','B']]

# %%
df.loc[dates[0],'A']

# %%
df.iloc[3]
# loc 명령과 달리 행과 열의 번호를 이용해서 데이터에 바로 접근하고 싶을 수 있는데,
# 그 명령이 iloc이다.
# iloc을 사용하면 행이나 열의 범위를 지정하면 된다.

# %%
df.iloc[3:5, 0:2]

# %%
df.iloc[[1,2,4],[0,2]]

# %%
df.iloc[1:3,:]

# %%
df.iloc[:,1:3]

# %%
df

# %%
df[df.A > 0]
# 특정 조건을 만족하는 데이터만 얻을 수 있다.
# 컬럼을 지정할 때 df['A']처럼 할 수도 있고, df.A와 같이 할 수도 있다.

# %%
df[df > 0]
# 데이터 전체에서 조건을 걸면 만족하지 않은 곳은 NaN 처리가 된다.

# %%
