import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

# 1. 산점도 그래프
fig, ax = plt.subplots()
ax.scatter(df["sepal_length"], df["sepal_width"], color="blue", label="Sepal")
ax.set_xlabel("Sepal Length")
ax.set_ylabel("Sepal Width")
ax.set_title("Iris Sepal Dimensions")
ax.legend()

st.pyplot(fig)

# 2. 막대 그래프
fig2, ax2 = plt.subplots()
sns.histplot(data=df, x='petal_length', color='skyblue', kde = True, bins=20)
ax2.set_xlabel("petal_length")
ax2.set_ylabel("Count")
ax2.set_title('Petal Length Distribution')

st.pyplot(fig2)

# 3. boxplot 그래프
fig3, ax3 = plt.subplots()
sns.boxplot(data=df, x='species', y='petal_length' )
ax3.set_xlabel('species')
ax3.set_ylabel("petal_length")
ax3.set_title('Petal Length by Species')

st.pyplot(fig3)

# 4. 산점도 
fig4 = px.scatter(df, x='sepal_length', y='sepal_width', color='species', title = 'Interactive Iris Sepal Scatter Plot')

st.plotly_chart(fig4)

# 5. 선그래프
fig4 = px.line(df, x='sepal_length', y='sepal_width', color='species', title = 'Interactive Iris Sepal Line Chart')

st.plotly_chart(fig4)