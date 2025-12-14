import streamlit as st

pages = [
    st.Page(page="pages/page1.py", title="Pendahuluan", icon="📝"),
    st.Page(page="pages/page2.py", title="Pembahasan", icon="📝"),
    st.Page(page="pages/page3.py", title="Simpulan dan Saran", icon="📝"),
    st.Page(page="pages/page4.py", title="Data World Bank", icon="🏦"),
]

pg = st.navigation(
    pages,
    position="sidebar"
)

pg.run()
