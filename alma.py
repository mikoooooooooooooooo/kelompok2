import streamlit as st
import pandas as pd

st.tittle("Metode Penelitian")

st.markdown("
Penelitian ini menggunakan pendekatan kuantitatif dengan desain penelitian Klausal-komparatif. Kausal-komparatif digunakan untuk menjelaskan hubungan sebab-akibat antar variabel, meskipun tanpa manipulasi variabel secara langsung (non-eksperimen). Penelitian ini berupaya melihat apakah perubahan pada variabel-variabel seperti GDP atau suku bunga menyebabkan perubahan pada FDI. Penelitian ini bertujuan untuk menguji pengaruh beberapa variabel makroekonomi dan politik terhadap Investasi Asing Langsung (FDI) di empat negara ASEAN (Indonesia, Malaysia, Thailand, dan Vietnam) pada periode 2004-2023. Penelitian ini menggunakan metode regresi data panel, yang memungkinkan untuk menganalisis data yang mempunyai dimensi waktu (time series) serta dimensi antar negara (cross-section) secara bersamaan.
Penelitian ini menggunakan satu variabel dependen dan tujuh variabel independen, yang dijelaskan sebagai berikut:
1.	Variabel Dependen:
FDI (Foreign Direct Investment) yaitu pengukur aliran investasi asing langsung yang masuk ke negara. Data FDI yang digunakan adalah net inflows dalam satuan USD, yang diperoleh dari World Bank.
2.	Variabel Independen:
GDP (Gross Domestic Product per Capita) yaitu ukuran total produksi barang dan jasa dalam suatu negara dibagi dengan jumlah penduduk. Satuan yang digunakan adalah USD. EXC (Exchange Rate) yaitu kurs mata uang lokal terhadap Dolar AS, dihitung dalam satuan LCU per USD (local currency units per US dollar). INF (Inflation) yaitu ingkat inflasi tahunan yang diukur dengan menggunakan inflasi harga konsumen dalam persentase (%). INT (Interest Rate) yaitu suku bunga deposito tahunan dalam persen (%). EKS (Exports) yaitu total ekspor barang dan jasa dalam satuan USD. POL (Political Stability) yaitu kestabilan politik dan tidak adanya kekerasan atau terorisme, diukur dengan menggunakan Political Stability and Absence of Violence/Terrorism dalam persenile rank. COC (Control of Corruption) yaitu tingkat pengendalian korupsi, diukur dengan Control of Corruption dalam persenile rank.
Penelitian ini menggunakan data sekunder dari World Bank selama periode 2004–2023 dengan fokus pada empat negara ASEAN: Indonesia, Malaysia, Thailand, dan Vietnam. Keempat negara ini dipilih secara purposive sampling karena merupakan ekonomi terbesar di kawasan dan memiliki data yang tersedia serta relevan dengan topik penelitian. Data berbentuk panel yang menggabungkan time series dan cross-section, menghasilkan total 80 observasi (4 negara × 20 tahun). Analisis dilakukan menggunakan regresi data panel dengan pendekatan Common Effect, Fixed Effect, dan Random Effect, yang dipilih berdasarkan uji Chow, Lagrange Multiplier, dan Hausman. Selain itu, dilakukan uji Goodness of Fit dan uji t untuk mengevaluasi pengaruh variabel secara simultan dan parsial (Gujarati & Porter, 2013).
Dengan menggunakan Eviews sebagai alat bantu statistik, model regresi data panel dapat dianalisis untuk menguji hipotesis penelitian tentang pengaruh faktor ekonomi dan politik terhadap aliran FDI di negara-negara ASEAN.
Model regresi data panel yang digunakan dalam penelitian ini adalah sebagai berikut:
FDIit = α + β1GDPit + β2EXCit + β3INFit + β4INTit + β5EKSit + β6POLit + β7COCit + ϵ 
Dimana:
FDI 	= Investasi Asing Langsung di negara i pada waktu t.
GDP 	= GDP per kapita negara i pada waktu t.
EXC 	= Nilai tukar mata uang lokal terhadap Dollar AS negara i pada waktu t.
INF 	= Inflasi tahunan negara i pada waktu t.
INT	    = Suku bunga deposito negara i pada waktu t.
EKS	    = Total ekspor negara i pada waktu t.
POL	    = Kestabilan politik negara i pada waktu t.
COC	    = Pengendalian korupsi negara i pada waktu t.
Α		= Konstanta.
β1- β7	= Koefisien regresi (hubungan antara variabel independen dengan FDI).
ϵ 		= Error term.
i		= Banyaknya observasi (cross section) yaitu empat Negara ASEAN
t		= Banyaknya data time series (2004-2023)

    ")
