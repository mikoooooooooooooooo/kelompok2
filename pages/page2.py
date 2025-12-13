import streamlit as st
import pandas as pd

st.title("Isi Pembahasan")

st.markdown(
""
## HASIL DAN PEMBAHASAN

Pemilihan model terbaik dalam analisis regresi data panel dilakukan dengan menggunakan **Uji Chow, Uji Hausman, dan Uji Lagrange Multiplier (LM)**. Ketiga uji tersebut digunakan untuk menentukan model yang paling sesuai di antara **Common Effect Model (CEM)**, **Fixed Effect Model (FEM)**, dan **Random Effect Model (REM)**.

Berdasarkan hasil **Uji Chow**, diperoleh nilai probabilitas sebesar **0.0000**, yang lebih kecil dari tingkat signifikansi 5% (alpha = 0.05). Dengan demikian, dapat disimpulkan bahwa model **Fixed Effect Model (FEM)** lebih tepat digunakan dibandingkan dengan **Common Effect Model (CEM)**.  
Selanjutnya, hasil **Uji Lagrange Multiplier (LM)** menunjukkan nilai probabilitas sebesar **0.0015 < 0.05**, yang mengindikasikan bahwa model **Random Effect Model (REM)** lebih sesuai dibandingkan CEM.

Untuk menentukan model terbaik antara FEM dan REM, dilakukan **Uji Hausman**. Hasil pengujian menunjukkan nilai probabilitas sebesar **1.0000 > 0.05**, sehingga tidak terdapat perbedaan signifikan antara FEM dan REM. Oleh karena itu, model **Random Effect** dinilai lebih tepat untuk digunakan. Dengan demikian, **model Random Effect dipilih sebagai model terbaik** untuk mengestimasi pengaruh variabel independen terhadap **Foreign Direct Investment (FDI)** di negara-negara ASEAN, dan seluruh pengujian hipotesis serta analisis selanjutnya didasarkan pada model ini.

---

### Uji Goodness of Fit dan Uji Parsial

Setelah ditetapkan bahwa model regresi yang digunakan adalah **Random Effect Model (REM)**, analisis dilanjutkan dengan melakukan **uji individual (uji t)** dan **uji goodness of fit**, yang terdiri dari **uji F** serta penghitungan **koefisien determinasi (Adjusted R-squared)**.

Uji t digunakan untuk menilai pengaruh masing-masing variabel independen secara parsial terhadap variabel dependen, yaitu **Foreign Direct Investment (FDI)**. Sementara itu, uji F bertujuan untuk menguji pengaruh seluruh variabel independen secara simultan terhadap FDI. Nilai Adjusted R-squared digunakan untuk mengetahui seberapa besar proporsi variasi FDI yang dapat dijelaskan oleh variabel independen yang digunakan dalam model.

Nilai **Adjusted R-squared (Adj R^2)** sebesar **0.390916** menunjukkan bahwa sekitar **39.09%** variasi FDI dapat dijelaskan oleh variabel independen dalam model, yaitu **GDP per kapita, nilai tukar, inflasi, suku bunga deposito, ekspor, kestabilan politik, dan pengendalian korupsi**. Sisanya sebesar **60.91%** dipengaruhi oleh faktor lain di luar model, seperti kebijakan domestik, dinamika geopolitik, serta kebijakan perdagangan global.  
Temuan ini sejalan dengan teori internalisasi yang dikemukakan oleh **Dunning (1988)**, yang menyatakan bahwa keputusan investasi asing tidak hanya ditentukan oleh indikator ekonomi makro, tetapi juga oleh faktor non-ekonomi.

---

### Uji Simultan (Uji F)

Hasil **Uji F** menunjukkan nilai **F-statistic sebesar 8.151590** dengan **p-value mendekati 0.0000**, yang berada jauh di bawah tingkat signifikansi 5%. Hal ini menunjukkan bahwa model regresi secara keseluruhan **signifikan**, sehingga dapat disimpulkan bahwa variabel independen secara simultan berpengaruh terhadap **Foreign Direct Investment (FDI)** di negara-negara ASEAN.  
Hasil ini mendukung **OLI Paradigm (Dunning, 1988)** yang menekankan pentingnya kondisi ekonomi makro dan kualitas tata kelola institusional dalam menarik investasi asing.

---

### Interpretasi Koefisien Regresi

Nilai **konstanta (C)** sebesar **USD 1,843,361,056.20** menunjukkan bahwa ketika seluruh variabel independen bernilai nol, FDI tetap berada pada tingkat tersebut. Meskipun kondisi ini secara empiris jarang terjadi, nilai konstanta mencerminkan daya tarik dasar negara-negara ASEAN dalam menarik investasi asing.

- **GDP per kapita** memiliki koefisien **1,081,684.56** dengan p-value **0.0275**, yang menunjukkan pengaruh positif dan signifikan terhadap FDI.
- **Nilai tukar (EXC)** memiliki koefisien **786,225.09** dengan p-value **0.0038**, yang menunjukkan pengaruh positif dan signifikan terhadap FDI.
- **Inflasi (INF)** memiliki koefisien **564,779,664.76** dengan p-value **0.0172**, yang menunjukkan pengaruh positif dan signifikan.
- **Suku bunga deposito (INT)** memiliki koefisien **-953,322,243.40** dengan p-value **0.0470**, yang menunjukkan pengaruh negatif dan signifikan terhadap FDI.
- **Ekspor (EKS)** memiliki p-value **0.4366**, sehingga tidak berpengaruh signifikan secara statistik.
- **Kestabilan politik (POL)** memiliki p-value **0.1705**, sehingga tidak signifikan.
- **Pengendalian korupsi (COC)** memiliki koefisien positif, namun tidak signifikan secara statistik dengan p-value **0.0844**.

Dengan demikian, meskipun beberapa variabel institusional belum menunjukkan tingkat signifikansi statistik yang kuat, secara keseluruhan **model Random Effect** dinilai cukup mampu menjelaskan dinamika **Foreign Direct Investment (FDI)** di negara-negara ASEAN.
""
)
  an 
 .

