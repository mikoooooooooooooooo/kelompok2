import streamlit as st

st.title("Isi Pembahasan")

st.markdown(
"""
**HASIL DAN PEMBAHASAN**

Pemilihan model terbaik dari regresi data panel menggunakan Uji Chow, Uji Hausman, dan Uji LM. Pemilihan model regresi data panel dalam penelitian ini dilakukan melalui tiga tahapan uji, yaitu uji Chow, uji Lagrange Multiplier (LM), dan uji Hausman. Berdasarkan hasil uji Chow, diperoleh nilai probabilitas sebesar 0.0000 yang lebih kecil dari tingkat signifikansi 5% (α = 0.05), sehingga dapat disimpulkan bahwa model Fixed Effect Model (FEM) lebih tepat dibandingkan dengan Common Effect Model (CEM). Selanjutnya, uji LM menunjukkan nilai probabilitas sebesar 0.0015 < 0.05, yang mengindikasikan bahwa model Random Effect Model (REM) lebih sesuai dibandingkan CEM. Untuk menentukan model terbaik antara FEM dan REM, dilakukan uji Hausman, yang menghasilkan nilai probabilitas sebesar 1.0000 > 0.05. Hasil ini menunjukkan bahwa model Random Effect lebih tepat digunakan karena tidak terdapat perbedaan signifikan antara FEM dan REM. Dengan demikian, model Random Effect dipilih sebagai model paling tepat untuk mengestimasi pengaruh variabel independen terhadap Foreign Direct Investment (FDI) di negara-negara ASEAN, dan seluruh pengujian hipotesis serta analisis selanjutnya dilakukan berdasarkan model ini.

Setelah ditetapkan bahwa model regresi yang digunakan adalah Random Effect Model (REM), analisis dilanjutkan dengan melakukan uji individual (uji t) dan uji goodness of fit yang terdiri dari uji F dan penghitungan nilai koefisien determinasi (Adjusted R-squared). Uji t digunakan untuk menilai pengaruh masing-masing variabel independen secara parsial terhadap variabel dependen, yaitu Foreign Direct Investment (FDI), sedangkan uji F bertujuan untuk menguji pengaruh variabel independen secara simultan. Nilai Adjusted R-squared digunakan untuk mengetahui seberapa besar proporsi variasi dalam FDI yang dapat dijelaskan oleh variabel-variabel independen dalam model.

Nilai Adjusted R-squared (Adj R^2) yang diperoleh sebesar 0,390916 mengindikasikan bahwa sekitar 39,09% variasi dalam nilai Foreign Direct Investment (FDI) dapat dijelaskan oleh variabel-variabel independen dalam model, seperti GDP per kapita, nilai tukar, inflasi, suku bunga deposito, ekspor, kestabilan politik, dan pengendalian korupsi. Meskipun nilai tersebut belum mencapai 50%, dalam konteks studi ekonomi dengan data panel lintas negara, angka ini tetap dianggap cukup memadai untuk merepresentasikan hubungan antar variabel yang kompleks (Gujarati & Porter, 2013). Sisanya sebesar 60,91% kemungkinan disebabkan oleh variabel-variabel lain di luar model, seperti kebijakan domestik, dinamika geopolitik, atau perubahan kebijakan perdagangan global.

Hasil uji F menunjukkan nilai F-statistic sebesar 8.151590 dengan p-value mendekati 0.0000, yang berada jauh di bawah tingkat signifikansi 5%. Hal ini mengindikasikan bahwa model regresi secara keseluruhan signifikan, sehingga hipotesis nol yang menyatakan bahwa seluruh koefisien regresi variabel independen sama dengan nol dapat ditolak.

Nilai konstanta (C) dalam model regresi sebesar 1.843.361.056,20 mengindikasikan bahwa ketika seluruh variabel independen dalam model diasumsikan bernilai nol, maka nilai FDI yang diharapkan tetap sebesar USD 1.843.361.056,20.

Variabel GDP per kapita memiliki koefisien sebesar 1,081,684.56 dan p-value sebesar 0.0275 (signifikan). Variabel kurs (EXC) memiliki koefisien 786,225.09 dengan p-value 0.0038 (signifikan). Variabel inflasi (INF) memiliki koefisien 564,779,664.76 dengan p-value 0.0172 (signifikan). Variabel suku bunga deposito (INT) memiliki koefisien -953,322,243.40 dengan p-value 0.0470 (signifikan). Variabel ekspor (EKS) p-value 0.4366 (tidak signifikan). Variabel kestabilan politik (POL) p-value 0.1705 (tidak signifikan). Variabel pengendalian korupsi (COC) p-value 0.0844 (tidak signifikan pada 5%).
"""
)an 
 .

