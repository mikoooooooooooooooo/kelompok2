import streamlit as st

st.subheader("KESIMPULAN DAN SARAN")

st.markdown(
    """
    <div style="text-align: justify;">
    <b>Kesimpulan:</b> Penelitian ini bertujuan untuk menganalisis pengaruh faktor
    makroekonomi dan non-ekonomi terhadap aliran Foreign Direct Investment (FDI)
    di empat negara ASEAN, yaitu Indonesia, Malaysia, Thailand, dan Vietnam selama
    periode 2004–2023 dengan menggunakan pendekatan regresi data panel.
    Berdasarkan hasil pemilihan model melalui uji Chow, uji Lagrange Multiplier,
    dan uji Hausman, Random Effect Model (REM) ditetapkan sebagai model terbaik
    dalam menjelaskan hubungan antar variabel.

    Hasil pengujian secara simultan (uji F) menunjukkan bahwa seluruh variabel
    independen yang digunakan dalam penelitian ini secara bersama-sama
    berpengaruh signifikan terhadap FDI di negara-negara ASEAN. Nilai Adjusted
    R-squared sebesar 39,09% mengindikasikan bahwa variasi FDI dapat dijelaskan
    oleh variabel GDP per kapita, nilai tukar, inflasi, suku bunga deposito,
    ekspor, kestabilan politik, dan pengendalian korupsi, sementara sisanya
    dipengaruhi oleh faktor lain di luar model penelitian.

    Secara parsial, hasil penelitian menunjukkan bahwa GDP per kapita, nilai
    tukar, inflasi, dan suku bunga deposito berpengaruh signifikan terhadap FDI.
    GDP per kapita berpengaruh positif, yang menunjukkan bahwa semakin tinggi
    tingkat pendapatan dan daya beli masyarakat, semakin besar daya tarik suatu
    negara bagi investor asing. Nilai tukar yang signifikan menunjukkan bahwa
    stabilitas dan pergerakan kurs mata uang menjadi pertimbangan penting dalam
    keputusan investasi asing. Inflasi yang signifikan mengindikasikan bahwa
    tingkat inflasi yang terkelola masih dapat diterima investor sebagai bagian
    dari dinamika ekonomi. Sebaliknya, suku bunga deposito berpengaruh negatif
    terhadap FDI, yang menunjukkan bahwa tingkat suku bunga yang tinggi dapat
    mengurangi daya tarik investasi asing karena meningkatkan biaya modal.

    Sementara itu, variabel ekspor, kestabilan politik, dan pengendalian korupsi
    tidak menunjukkan pengaruh signifikan terhadap FDI pada tingkat signifikansi
    5%. Temuan ini mengindikasikan bahwa dalam periode dan negara yang diteliti,
    investor asing cenderung lebih mempertimbangkan faktor ekonomi makro
    dibandingkan faktor institusional dan politik.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align: justify;">
    <b>Saran:</b>

    <br><b>Bagi Pemerintah dan Pembuat Kebijakan</b><br>
    Pemerintah di negara-negara ASEAN, khususnya Indonesia, Malaysia, Thailand,
    dan Vietnam, perlu memprioritaskan kebijakan yang mendorong pertumbuhan
    ekonomi berkelanjutan dan peningkatan GDP per kapita, karena terbukti menjadi
    faktor utama yang menarik FDI. Selain itu, stabilitas nilai tukar dan
    pengendalian inflasi perlu terus dijaga untuk menciptakan iklim investasi
    yang kondusif. Pemerintah juga perlu berhati-hati dalam menetapkan tingkat
    suku bunga deposito agar tidak terlalu tinggi sehingga dapat menghambat
    masuknya investasi asing.

    <br><br><b>Bagi Investor Asing</b><br>
    Investor asing diharapkan dapat menjadikan indikator makroekonomi seperti GDP
    per kapita, stabilitas nilai tukar, inflasi, dan suku bunga sebagai
    pertimbangan utama dalam mengambil keputusan investasi di kawasan ASEAN.
    Meskipun faktor politik dan institusional tidak terbukti signifikan secara
    statistik dalam penelitian ini, investor tetap perlu mempertimbangkannya
    sebagai faktor risiko jangka panjang.

    <br><br><b>Bagi Peneliti Selanjutnya</b><br>
    Penelitian selanjutnya disarankan untuk menambahkan variabel lain yang
    berpotensi memengaruhi FDI, seperti keterbukaan perdagangan, kualitas
    infrastruktur, tingkat pendidikan tenaga kerja, kebijakan pajak, atau indeks
    kemudahan berusaha. Selain itu, penggunaan periode waktu yang lebih panjang,
    metode estimasi alternatif, atau pemisahan analisis per negara dapat
    memberikan pemahaman yang lebih mendalam mengenai determinan FDI di kawasan
    ASEAN.

    <br><br><b>Bagi Pengembangan Kebijakan Regional ASEAN</b><br>
    ASEAN sebagai kawasan ekonomi regional diharapkan dapat meningkatkan kerja
    sama dalam menciptakan iklim investasi yang lebih terintegrasi, transparan,
    dan stabil guna meningkatkan daya saing kawasan dalam menarik FDI di tengah
    persaingan global.
    </div>
    """,
    unsafe_allow_html=True
)
