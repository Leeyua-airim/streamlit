import numpy as np
import altair as alt #?
import pandas as pd 
import streamlit as st

st.header('st.write')

st.write('마크다운을 기본으로 하는 문자열 입니다.')
st.write('*볼드*')
st.write('이모지 :sunglasses:')
st.write(1234)

# 데이터 프레임 생성
df = pd.DataFrame({
    '첫 번째 cloumn' : [1,2,3,4],
    'second column' : [10,20,30,40]    
})

# 화면 출력 
st.write(df)

st.write('Below is a DataFrame : ', df, 'Above is a dataframe')

st.latex(r'''
    a
''')
# 
df2 = pd.DataFrame(
    np.random.randn(10,3),
    columns=['a', 'b', 'c']
)
st.write(df2)

# 시각화 또한 가능 
c = alt.Chart(df2).mark_circle().encode(
    x='a', 
    y='b', 
    size='c',
    color='c',
    tooltip=['a','b','c'])

st.write(c)