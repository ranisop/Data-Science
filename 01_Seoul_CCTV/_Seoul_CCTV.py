#%%
import pandas as pd

cctv_seoul = pd.read_excel('/Users/nani/Desktop/GitHub/DataScience/01_Seoul_CCTV/CCTV_in_Seoul.xlsx')
cctv_seoul.head()

# %%
#pop_seoul = pd.read_excel('/Users/nani/Desktop/GitHub/DataScience/01_Seoul_CCTV/population_in_Seoul.xls')
pop_seoul = pd.read_excel('/Users/nani/Desktop/GitHub/DataScience/01_Seoul_CCTV/population_in_Seoul.xls',
header=2, parse_cols='B,D,G,J,N')
pop_seoul

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

#########################################################
#########################################################

# %%
# 구별 CCTV 현황 정리
cctv_seoul.head()

# %%
cctv_seoul.sort_values(by='소계', ascending=True).head(5)

# %%
cctv_seoul.sort_values(by='소계', ascending=False).head(5)

# %%
# cctv_seoul['최근증가율'] = (cctv_seoul['2018년'] + cctv_seoul['2017년'] +
# cctv_seoul['2016년']) / (cctv_seoul['2015년'] + cctv_seoul['2014년'] + 
# cctv_seoul['2013년']) * 100
# cctv_seoul.sort_values(by='최근증가율', ascending=False).head(5)

# %%
cctv_seoul['최근증가율'] = (cctv_seoul['2018년'] + cctv_seoul['2017년'] +
cctv_seoul['2016년']) / (cctv_seoul['2015년'] + cctv_seoul['2014년'] + 
cctv_seoul['2013년'] + cctv_seoul['2012년'] + cctv_seoul['2011년 이전']) * 100
cctv_seoul.sort_values(by='최근증가율', ascending=False).head(5)

# 최근 3년간(2016~2018) CCTV가 그 이전 대비 많이 증가한 구는
# 중구, 영등포구, 성동구, 금천구, 광진구

# %%
# 서울시 인구 현황 정리
pop_seoul.head()

# %%
# 0행에 있는 합계 지우기
pop_seoul.drop([0], inplace=True)
pop_seoul.head()

# %%
# unique : 반복된 데이터는 하나로 나타내서 한 번 이상 나타난 데이터 확인
pop_seoul['구별'].unique()

# %%
# NaN 데이터 있는지, 어디 있는지 확인
pop_seoul[pop_seoul['구별'].isnull()]

# %%
# drop 명령으로 NaN이 있던 행 삭제(예: 26행에 있다면)
# pop_seoul.drop([26], inplace=True)
# pop_seoul.head()

# %%
pop_seoul['외국인비율'] = pop_seoul['외국인'] / pop_seoul['인구수'] * 100
pop_seoul['고령자비율'] = pop_seoul['고령자'] / pop_seoul['인구수'] * 100
pop_seoul.head()

# %%
pop_seoul.sort_values(by='인구수', ascending=False).head()

# %%
pop_seoul.sort_values(by='외국인', ascending=False).head()

# %%
pop_seoul.sort_values(by='외국인비율', ascending=False).head()

# %%
pop_seoul.sort_values(by='고령자', ascending=False).head()

# %%
pop_seoul.sort_values(by='고령자비율', ascending=False).head()

#########################################################
#########################################################

# %%
