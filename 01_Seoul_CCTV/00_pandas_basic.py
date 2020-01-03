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
df2 = df.copy()
# DataFrame을 복사할 때 그냥 = 기호를 이용해서 복사하면 실제 데이터의 내용이 복사되는 것이 아니라
# 데이터 위치만 복사되기 때문에 원본 데이터는 하나만 있게 된다.

# %%
df2['E'] = ['one','one','two','three','four','three']
df2
# 원래 있는 DataFrame에 새로운 컬럼 추가하기

# %%
df2['E'].isin(['two','four'])
# 컬럼에서 데이터 있는지 조건을 걸고 싶을 때 isin 사용

# %%
df2[df2['E'].isin(['two','four'])]

# %%
df

# %%
df.apply(np.cumsum)
# 통계 느낌의 데이터를 볼 때는 특정 함수를 적용시킨다. => apply 명령
# 누적합을 알고 싶을 때, numpy의 cumsum 사용

# %%
df.apply(lambda x: x.max() - x.min())
# 최대값과 최소값의 차이를 알고 싶다면 one-line 함수인 lambda 사용

# %%
