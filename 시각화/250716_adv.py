import streamlit as st
import pandas as pd

cols = st.columns(4)

with cols[0]:
    st.markdown(
        """
<img src="https://cdn-icons-png.flaticon.com/512/15/15050.png" width = "50" height = "50" >
            """,
        unsafe_allow_html=True,
    )
    st.metric("All Spendings", "$574.34")

with cols[1]:
    st.metric("Spent this month", "$682.5")
    st.markdown(
        """
<img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqoVk1Oq-aKC5f0btVTv-gK7aW8l9CNWIyQKW7QfPfFF-46T6SZKVb1PeakAhGfqP-fv0&usqp=CAU" width= "50" height = "50" > """,
        unsafe_allow_html=True,
    )

with cols[2]:
    st.markdown(
        """
<img src = "https://img.freepik.com/premium-vector/uptrend-graph-stock-icon-line_419328-1954.jpg" width= "50" height = "60"> """,
        unsafe_allow_html=True,
    )
    st.metric("Earnings", "$350.40")

with cols[3]:
    st.markdown(
        """
    <img src = "https://cdn-icons-png.flaticon.com/512/3106/3106921.png" width= "50" height = "60"> """,
        unsafe_allow_html=True,
    )
    st.metric("New clients", "321")

cols2 = st.columns(3)

with cols2[0]:
    st.metric("This month eamings", "$682.5")
    st.markdown("""
<img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMtIA7djmPcxukMGOPAoj71ivD3yLpmMm3_g&s"> """,
unsafe_allow_html=True)

with cols2[1]:
    st.metric("Spent this month", "$682.5")
    st.markdown("""
<img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMtIA7djmPcxukMGOPAoj71ivD3yLpmMm3_g&s"> """,
unsafe_allow_html=True)
    
with cols2[2]:
    st.markdown(
        "<p style=font-weight:bold; font-size:20px;>Your Transfers</p>",
        unsafe_allow_html=True,
    )
    st.markdown("""
- **From Alex Manda**
- **To Laura Santos**
- **From Jandon S.**
""")
    

cols3,cols4 = st.columns([2,1])
with cols3:
    st.metric("Total sapent", "$682.5")
    st.markdown("""
<img src = "https://i.namu.wiki/i/d1A_wD4kuLHmOOFqJdVlOXVt1TWA9NfNt_HA0CS0Y_N0zayUAX8olMuv7odG2FiDLDQZIRBqbPQwBSArXfEJlQ.webp"> """,
unsafe_allow_html=True)
    

with cols4:
    st.markdown(
        "<p style=font-weight:bold; font-size:20px; >Your trancations</p>",
        unsafe_allow_html=True,
    )
    st.markdown("""
- **Public Transport**
- **Grocery Store**
- **Public Transport**
""")
