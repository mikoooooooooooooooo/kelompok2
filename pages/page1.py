import streamlit as st # import modul Streamlit untuk membuat web app

# Judul utama halaman
st.title("Determinasi Investasi Asing Langsung di 4 (Empat) Negara ASEAN")

# Menampilkan nama anggota kelompok menggunakan st.write
st.write("""Kelompok 2:
1. Jesica Octavia Simamora (021002414002)
2. Muhammad Hary Prasetyo Wahyu Jatmiko (021002414004)
3. Alma Dewi Ananda (021002414005)
4. Chika Ristysuatantri (021002201016)
    """)

# Subjudul bagian pendahuluan
st.subheader("Pendahuluan")

# Menampilkan paragraf panjang dengan HTML agar justify bisa digunakan
st.markdown("""
    <div style="text-align: justify;">
    <p>Investasi Asing Langsung (FDI) memainkan peran yang sangat penting dalam perekonomian negara berkembang, khususnya di kawasan Asia Tenggara. FDI tidak hanya memberikan kontribusi terhadap pembentukan modal tetap dan penciptaan lapangan pekerjaan, tetapi juga berperan dalam transfer teknologi, peningkatan keterampilan tenaga kerja, serta integrasi ekonomi global. Negara-negara ASEAN, termasuk Indonesia, Malaysia, Thailand, dan Vietnam, telah menjadi tujuan utama bagi investor asing karena potensi pasar yang besar, biaya tenaga kerja yang relatif lebih rendah, dan posisi geografis yang strategis di kawasan Asia. Namun, meskipun kawasan ini menawarkan berbagai peluang investasi, aliran FDI tetap dipengaruhi oleh berbagai faktor makroekonomi dan non-ekonomi.
    
    <p>Beberapa faktor yang diketahui dapat memengaruhi FDI antara lain: Produk Domestik Bruto (GDP) per kapita, kurs mata uang lokal terhadap Dolar AS, inflasi, suku bunga deposito, ekspor, kestabilan politik, serta pengendalian korupsi. Faktor-faktor ini mencerminkan kondisi ekonomi, sosial, dan politik yang dapat meningkatkan atau menurunkan daya tarik suatu negara bagi investor asing. Oleh karena itu, penting untuk mengeksplorasi bagaimana faktor-faktor tersebut mempengaruhi aliran FDI di negara-negara ASEAN, khususnya Indonesia, Malaysia, Thailand, dan Vietnam pada periode 2004-2023. Penelitian ini bertujuan untuk memberikan gambaran yang lebih komprehensif tentang bagaimana berbagai faktor ini mempengaruhi FDI dan, pada gilirannya, pertumbuhan ekonomi di negara-negara tersebut.
    
    <p>Berbagai studi teoritis dan empiris telah membahas pengaruh berbagai faktor terhadap aliran FDI, dan masing-masing variabel independen memiliki kontribusi yang berbeda dalam mempengaruhi keputusan investasi asing. GDP per kapita dianggap sebagai indikator utama daya beli dan ukuran pasar suatu negara. Teori ekonomi klasik menyatakan bahwa negara yang memiliki GDP per kapita yang besar mempunyai daya tarik lebih besar bagi investor asing karena pasar yang lebih besar dan potensi konsumsi yang lebih tinggi (Harrison & McMillan, 2019). Dalam banyak studi empiris, ditemukan bahwa pada suatu negara yang meiliki GDP per kapita yang besar lebih mampu menarik FDI karena stabilitas ekonomi dan daya beli yang lebih besar, yang berpotensi meningkatkan pengembalian investasi (Borensztein et al., 2020). Teori ekonomi internasional juga menunjukkan bahwa nilai tukar mata uang dapat memengaruhi aliran FDI. Nilai tukar yang stabil dan kompetitif dapat meningkatkan daya tarik investasi asing karena mengurangi ketidakpastian yang dihadapi investor. Teori ini didukung oleh temuan empiris yang menunjukkan bahwa negara dengan nilai tukar yang stabil lebih cenderung menarik FDI karena mengurangi risiko fluktuasi (Eicher & Karras, 2017). Nguyen et al. (2020) meneliti bahwa nilai tukar stabil mendorong keputusan investasi karena memperkirakan pengembalian yang lebih konsisten. Dalam teori ekonomi, inflasi moderat sering dianggap sebagai indikator pertumbuhan ekonomi yang sehat dan dapat menarik investasi asing. Inflasi yang stabil dan terkendali menciptakan lingkungan ekonomi yang dapat diprediksi, yang penting bagi keputusan investasi (Aizenman et al., 2017). Beberapa studi empiris menunjukkan bahwa inflasi yang rendah atau moderat cenderung meningkatkan aliran FDI, sementara inflasi yang tinggi dapat mengurangi kepercayaan investor (Arslan & Zhang, 2015). Suku bunga deposito yang tinggi dapat memengaruhi keputusan investor, karena suku bunga yang lebih tinggi memberikan alternatif investasi domestik yang lebih menguntungkan daripada investasi asing. Oleh karena itu, suku bunga deposito yang tinggi dapat menurunkan daya tarik FDI. Penelitian oleh Alfaro et al. (2015) menemukan bahwa suku bunga yang tinggi dapat mendorong investor untuk memilih investasi di pasar domestik karena tingkat pengembalian yang lebih menarik. Teori perdagangan internasional menunjukkan bahwa negara dengan volume ekspor yang tinggi cenderung menarik lebih banyak FDI. Ekspor yang tinggi mencerminkan daya saing ekonomi dan integrasi ekonomi global, yang membuat negara tersebut lebih menarik bagi investor asing. Studi oleh Cavallo & Fernández-Arias (2015) menunjukkan bahwa negara-negara dengan performa ekspor yang baik sering kali memiliki sektor yang lebih maju dan menarik lebih banyak investasi asing.  Ketidakstabilan politik justru dapat mendorong masuknya FDI, terutama di sektor-sektor berisiko tinggi seperti pertambangan atau pasar frontier. Investor asing dapat memanfaatkan lemahnya institusi atau tawaran insentif tinggi dari pemerintah negara yang tidak stabil sebagai peluang untuk memperoleh keuntungan besar (Bailey, 2018; Khanna & Palepu, 2010). Studi Le dan Zak (2006) serta Busse dan Hefeker (2007) mendukung pandangan ini dengan menunjukkan bahwa investor tetap bersedia menanamkan modal di negara tidak stabil jika potensi return investasi cukup tinggi. Negara dengan tingkat pengendalian korupsi yang baik cenderung menarik lebih banyak FDI. Hal ini terkait dengan teori yang menyatakan bahwa negara dengan tingkat transparansi dan akuntabilitas yang tinggi memberikan kepercayaan lebih kepada investor asing. Studi oleh Blonigen (2016) menunjukkan bahwa pengendalian korupsi yang baik dapat menciptakan lingkungan yang kondusif bagi investasi asing karena mengurangi biaya transaksi dan meningkatkan kepastian hukum bagi investor.
    
    <p>Studi tentang pengaruh faktor-faktor makroekonomi dan non-ekonomi terhadap FDI telah banyak dilakukan, namun hasil penelitian yang ada sering kali menunjukkan temuan yang beragam, baik yang sejalan maupun yang bertolak belakang dengan teori yang ada. Sebagai contoh, beberapa studi menunjukkan bahwa GDP per kapita yang lebih tinggi menarik lebih banyak FDI karena mencerminkan pasar yang lebih besar dan stabilitas ekonomi (Binh, 2016; Nguyen et al., 2019), sementara studi lain menunjukkan bahwa faktor-faktor politik dan sosial, seperti kestabilan politik dan pengendalian korupsi, lebih berpengaruh terhadap keputusan investasi asing (Alfaro et al., 2015). Tujuan penelitian ini adalah untuk mengatasi kesenjangan tersebut dengan memberikan penilaian yang lebih komprehensif mengenai pengaruh berbagai faktor ekonomi dan politik terhadap FDI, serta untuk menguji interaksi antara variabel-variabel tersebut di negara-negara ASEAN, khususnya Indonesia, Malaysia, Thailand, dan Vietnam.
    
    <p>Penelitian ini menawarkan kontribusi baru dengan mengkaji pengaruh faktor-faktor makroekonomi dan non-ekonomi terhadap FDI di empat negara ASEAN pada periode 2004-2023. Penelitian ini mengintegrasikan variabel-variabel yang jarang disatukan dalam studi-studi sebelumnya, seperti kestabilan politik, kekerasan/terorisme, serta pengendalian korupsi yang dapat memberikan pemahaman yang lebih komprehensif tentang dinamika FDI di kawasan ASEAN. Selain itu, penelitian ini akan menguji keterkaitan antara kondisi sosial, politik, dan ekonomi yang berbeda di setiap negara dan bagaimana hal ini mempengaruhi daya tarik masing-masing negara bagi investor asing.
    
    <p>Tujuan dari penelitian ini adalah untuk menganalisis pengaruh GDP per kapita, nilai tukar mata uang lokal terhadap Dollar AS, inflasi, suku bunga deposito, ekspor, kestabilan politik, dan pengendalian korupsi terhadap FDI di empat negara ASEAN (Indonesia, Malaysia, Thailand, dan Vietnam) pada periode 2004-2023. Penelitian ini bertujuan untuk memberikan wawasan yang lebih mendalam tentang faktor-faktor yang mempengaruhi aliran FDI di negara-negara tersebut serta kontribusinya terhadap pertumbuhan ekonomi regional. Hasil penelitian ini diharapkan dapat memberikan rekomendasi bagi pembuat kebijakan untuk merumuskan strategi yang lebih efektif dalam menarik FDI dan mendukung pertumbuhan ekonomi yang berkelanjutan.
    </div>
    """,
    unsafe_allow_html=True
)

# Subjudul Metode Penelitian
st.subheader("Metode Penelitian")

# Penjelasan mengenai pendekatan penelitian secara justify paragraf
st.markdown("""
    <div style="text-align: justify;">
    <p>Penelitian ini menggunakan pendekatan kuantitatif dengan desain penelitian Klausal-komparatif. Kausal-komparatif digunakan untuk menjelaskan hubungan sebab-akibat antar variabel, meskipun tanpa manipulasi variabel secara langsung (non-eksperimen). Penelitian ini berupaya melihat apakah perubahan pada variabel-variabel seperti GDP atau suku bunga menyebabkan perubahan pada FDI. Penelitian ini bertujuan untuk menguji pengaruh beberapa variabel makroekonomi dan politik terhadap Investasi Asing Langsung (FDI) di empat negara ASEAN (Indonesia, Malaysia, Thailand, dan Vietnam) pada periode 2004-2023. Penelitian ini menggunakan metode regresi data panel, yang memungkinkan untuk menganalisis data yang mempunyai dimensi waktu (time series) serta dimensi antar negara (cross-section) secara bersamaan.
   </div>
    """,
    unsafe_allow_html=True
)   

# Penjelasan lanjutan terkait variabel dependen & independen
st.markdown("""
    <div style="text-align: justify;">    
    <p>Penelitian ini menggunakan satu variabel dependen dan tujuh variabel independen, yang dijelaskan sebagai berikut:
     </div>
    """,
    unsafe_allow_html=True
)  

# Daftar variabel penelitian ditulis dengan markdown HTML
st.markdown("""
    <div style="text-align: justify;">
    
1.	Variabel Dependen
FDI (Foreign Direct Investment) yaitu pengukur aliran investasi asing langsung yang masuk ke negara. Data FDI yang digunakan adalah net inflows dalam satuan USD, yang diperoleh dari World Bank.

2.	Variabel Independen
GDP (Gross Domestic Product per Capita) yaitu ukuran total produksi barang dan jasa dalam suatu negara dibagi dengan jumlah penduduk. Satuan yang digunakan adalah USD. EXC (Exchange Rate) yaitu kurs mata uang lokal terhadap Dolar AS, dihitung dalam satuan LCU per USD (local currency units per US dollar). INF (Inflation) yaitu ingkat inflasi tahunan yang diukur dengan menggunakan inflasi harga konsumen dalam persentase (%). INT (Interest Rate) yaitu suku bunga deposito tahunan dalam persen (%). EKS (Exports) yaitu total ekspor barang dan jasa dalam satuan USD. POL (Political Stability) yaitu kestabilan politik dan tidak adanya kekerasan atau terorisme, diukur dengan menggunakan Political Stability and Absence of Violence/Terrorism dalam persenile rank. COC (Control of Corruption) yaitu tingkat pengendalian korupsi, diukur dengan Control of Corruption dalam persenile rank.
  
    </div>
    """,
    unsafe_allow_html=True
) 

st.markdown("""
    <div style="text-align: justify;">
    <p>Penelitian ini menggunakan data sekunder dari World Bank selama periode 2004–2023 dengan fokus pada empat negara ASEAN: Indonesia, Malaysia, Thailand, dan Vietnam. Keempat negara ini dipilih secara purposive sampling karena merupakan ekonomi terbesar di kawasan dan memiliki data yang tersedia serta relevan dengan topik penelitian. Data berbentuk panel yang menggabungkan time series dan cross-section, menghasilkan total 80 observasi (4 negara × 20 tahun). Analisis dilakukan menggunakan regresi data panel dengan pendekatan Common Effect, Fixed Effect, dan Random Effect, yang dipilih berdasarkan uji Chow, Lagrange Multiplier, dan Hausman. Selain itu, dilakukan uji Goodness of Fit dan uji t untuk mengevaluasi pengaruh variabel secara simultan dan parsial (Gujarati & Porter, 2013).

     </div>
    """,
    unsafe_allow_html=True
) 

# Paragraf penjelasan data panel World Bank
st.markdown("""
    <div style="text-align: justify;">
    <p>Dengan menggunakan Eviews sebagai alat bantu statistik, model regresi data panel dapat dianalisis untuk menguji hipotesis penelitian tentang pengaruh faktor ekonomi dan politik terhadap aliran FDI di negara-negara ASEAN.
Model regresi data panel yang digunakan dalam penelitian ini adalah sebagai berikut:
     
    """,unsafe_allow_html=True) 

# Menampilkan formula regresi panel menggunakan LaTeX
st.latex(r'''
FDI_{it} = \alpha 
+ \beta_1 GDP_{it}
+ \beta_2 EXC_{it}
+ \beta_3 INF_{it}
+ \beta_4 INT_{it}
+ \beta_5 EKS_{it}
+ \beta_6 POL_{it}
+ \beta_7 COC_{it}
+ \varepsilon
''')  # st.latex akan merender rumus matematis

# Penjelasan definisi masing-masing variabel dan notasi matematis
st.markdown("""
<div style="text-align: justify;">
Dimana:

<p>FDI 	= Investasi Asing Langsung di negara i pada waktu t.

<p>GDP 	= GDP per kapita negara i pada waktu t.

<p>EXC 	= Nilai tukar mata uang lokal terhadap Dollar AS negara i pada waktu t.

<p>INF 	= Inflasi tahunan negara i pada waktu t.

<p>INT	    = Suku bunga deposito negara i pada waktu t.

<p>EKS	    = Total ekspor negara i pada waktu t.

<p>POL	    = Kestabilan politik negara i pada waktu t.

<p>COC	    = Pengendalian korupsi negara i pada waktu t.

<p>Α		= Konstanta.

<p>β1- β7	= Koefisien regresi (hubungan antara variabel independen dengan FDI).

<p>ϵ 		= Error term.

<p>i		= Banyaknya observasi (cross section) yaitu empat Negara ASEAN

<p>t		= Banyaknya data time series (2004-2023)

    """,unsafe_allow_html=True
           )