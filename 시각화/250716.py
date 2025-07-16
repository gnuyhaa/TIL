import streamlit as st
import pandas as pd

st.markdown("# 자동차 데이터")

df = pd.read_csv('./data/cars.csv')

st.markdown(
    '<p style="color:green; font-size:15px;">자동차 데이터 테이블</p>', unsafe_allow_html=True
    )
 

Manu_s = st.selectbox('제조사 선택',options = df['Manufacturer'])

col_s = st.selectbox('정렬할 컬럼 선택', options= df.columns)

v = st.radio('정렬 순서 선택', options=('오름차순', '내림차순'))

# 필터링 된 값 df 출력 

filtered_df = df[df['Manufacturer'] == Manu_s]

if v == '오름차순': 
    ascending_df = True
else:
    ascending_df = False

sorted_df = filtered_df.sort_values(by=col_s, ascending = ascending_df)

sorted_df