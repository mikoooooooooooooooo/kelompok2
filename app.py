import streamlit as st

pages = [
    st.Page(page="pages/page1.py", title="Pendahuluan (Alma)", icon="📝"),
    st.Page(page="pages/page2.py", title="Pembahasan (Jess)", icon="📝"),
    st.Page(page="pages/page3.py", title="Simpulan dan Saran (Chick)", icon="📝"),
    st.Page(page="pages/page4.py", title="Data World Bank (MixX)", icon="🏦"),
]

pg = st.navigation(
    pages,
    position="sidebar"
)

pg.run()
