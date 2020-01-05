#########################################################
## 2. Basic of Python(DataFrame)
#########################################################

# %%
import pandas as pd

df1 = pd.DataFrame({'A' : ['A0','A1','A2','A3'],
                    'B' : ['B0','B1','B2','B3'],
                    'C' : ['C0','C1','C2','C3'],
                    'D' : ['D0','D1','D2','D3']},
                    index=[0,1,2,3])

df2 = pd.DataFrame({'A' : ['A4','A5','A6','A7'],
                    'B' : ['B4','B5','B6','B7'],
                    'C' : ['C4','C5','C6','C7'],
                    'D' : ['D4','D5','D6','D7']},
                    index=[4,5,6,7])

df3 = pd.DataFrame({'A' : ['A8','A9','A10','A11'],
                    'B' : ['B8','B9','B10','B11'],
                    'C' : ['C8','C9','C10','C11'],
                    'D' : ['D8','D9','D10','D11']},
                    index=[8,9,10,11])

# %%
df1

# %%
df2

# %%
df3

# %%
# 열 방향으로 단순히 합치는 것은 concat 명령
# 단순하게 아무 옵션 없이 그냥 사용하면 열 방향으로 병합된다.
result = pd.concat([df1, df2, df3])
result

# %%
# keys 옵션으로 구분가능
# 이렇게 keys로 지정된 구분은 다중 idnex가 되어서 level을 형성한다.
result = pd.concat([df1, df2, df3], keys=['x','y','z'])
result

# %%
result.index

# %%
result.index.get_level_values(0)

# %%
result.index.get_level_values(1)

# %%
# concat 명령은 index를 기준으로 합쳐서 값을 가질 수 없는 곳에 NaN이 저장된다.
df4 = pd.DataFrame({'B' : ['B2','B3','B6','B7'],
                    'D' : ['D2','D3','D6','D7'],
                    'F' : ['F2','F3','F6','F7']},
                    index=[2,3,6,7])
result = pd.concat([df1, df4], axis=1)

# %%
df1

# %%
df4

# %%
result

# %%
# 공통된 index로 합치고, 공통되지 않은 index의 데이터는 버리도록 하는 옵션이 join='innder'
result = pd.concat([df1, df4], axis=1, join='inner')
result

# %%
# join_axes=[df1.index] 옵션으로 df1의 인덱스에 맞추도록 할 수도 있다.
result = pd.concat([df1, df4], axis=1, join_axes=[df1.index])
result

# %%
# 그럼 df4의 인덱스에도 맞춰보자.
result2 = pd.concat([df1, df4], axis=1, join_axes=[df4.index])
result2

# %%
# concat 명령을 사용하는데 열 방향으로 합치면서 ignore_index=True라고 옵션을 잡으면
# 두 데이터의 index를 무시하고 합친 후 다시 index를 부여한다.
# 이때는 열 기준으로 합치게 된다.
result = pd.concat([df1, df4], ignore_index=True)
result

#########################################################
#########################################################

# %%
left = pd.DataFrame({'key' : ['K0','K4','K2','K3'],
                    'A' : ['A0','A1','A2','A3'],
                    'B' : ['B0','B1','B2','B3']})

right = pd.DataFrame({'key' : ['K0','K1','K2','K3'],
                    'C' : ['C0','C1','C2','C3'],
                    'D' : ['D0','D1','D2','D3']})

# %%
left

# %%
right

# %%
# 두 데이터에 공통으로 있는 컬럼인 key를 기준으로 merge 명령에서 
# merge 기준을 설정하는 on 옵션으로 합치면 공통된 key에 대해서만 합치게 된다.
pd.merge(left, right, on='key')

# %%
# how 옵션으로 한쪽 데이터를 설정할 수 있다.
pd.merge(left, right, how='left', on='key')

# %%
pd.merge(left, right, how='right', on='key')

# %%
# merge한 데이터 결과를 모두 가지는 outer 옵션
# 마치 합집합처럼 merge가 되며 공통된 요소가 아닌 곳은 NaN 처리가 된다.
pd.merge(left, right, how='outer', on='key')

# %%
# outer의 반대인 inner 옵션도 있다.
# 교집합처럼 공통된 요소만 가진다.
pd.merge(left, right, how='inner', on='key')

# %%
