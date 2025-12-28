# ======================================================
# IMPORT LIBRARY YANG DIBUTUHKAN
# ======================================================
import streamlit as st                     # Library utama Streamlit
import pandas as pd                       # Untuk pengolahan data tabel
import streamlit.components.v1 as components  # Untuk render HTML/CSS kompleks

# ======================================================
# JUDUL HALAMAN
# ======================================================
st.subheader("Isi Pembahasan")

# ======================================================
# PARAGRAF PEMBUKA (HASIL DAN PEMBAHASAN)
# Menggunakan HTML agar teks rata kiri-kanan (justify)
# ======================================================
st.markdown(
"""
<div style="text-align: justify; line-height: 1.6;">

<b>HASIL DAN PEMBAHASAN</b><br><br>

Pemilihan model terbaik dari regresi data panel menggunakan Uji Chow, Uji Hausman, dan Uji LM.""",
    unsafe_allow_html=True
)

# ======================================================
# DATA RINGKASAN PEMILIHAN MODEL (CHOW, LM, HAUSMAN)
# ======================================================
data = [
    ["Uji Chow", "Cross-section Chi-square", 30.6209, 0.0000, "FEM"],
    ["Uji Langrange Multiplier", "Breusch-Pagan (Both)", 10.0509, 0.0015, "REM"],
    ["Uji Hausman", "Cross-section random", 0.0000, 1.0000, "REM"],
]

# Membuat DataFrame
df = pd.DataFrame(data, columns=["Metode", "Effect", "Stat", "Prob.", "Keputusan"])

# ======================================================
# FORMAT ANGKA DESIMAL ALA INDONESIA
# (koma sebagai desimal, titik sebagai pemisah ribuan)
# ======================================================
df_show = df.copy()
for col in ["Stat", "Prob."]:
    df_show[col] = df_show[col].map(
        lambda x: f"{x:,.4f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

# ======================================================
# MEMBANGUN BARIS HTML UNTUK TABEL
# ======================================================
rows = ""
for _, r in df_show.iterrows():
    rows += f"""
    <tr>
        <td><strong>{r['Metode']}</strong></td>
        <td>{r['Effect']}</td>
        <td class="num">{r['Stat']}</td>
        <td class="num">{r['Prob.']}</td>
        <td><span class="badge">{r['Keputusan']}</span></td>
    </tr>
    """

# ======================================================
# HTML + CSS UNTUK TABEL RINGKASAN PEMILIHAN MODEL
# ======================================================
html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
/* Warna dan font */
body {{
  font-family: Arial, sans-serif;
  background: transparent;          
  color: #ffffff;
}}

/* Container tabel */
.container {{
  max-width: 900px;
  margin: auto;
  padding: 16px;
  border-radius: 12px;
  background: #00008b;          
  border: 1px solid rgba(255,255,255,0.12);
}}

/* Tabel */
table {{
  width: 100%;
  border-collapse: collapse;
}}

/* Header & sel tabel */
th, td {{
  padding: 10px 12px;
  border-bottom: 1px solid rgba(255,255,255,0.15);
  color: #ffffff;
}}

th {{
  font-weight: bold;
  text-align: left;
}}

/* Kolom numerik rata kanan */
.num {{
  text-align: right;
}}

/* Badge FEM / REM */
.badge {{
  padding: 4px 10px;
  border-radius: 999px;
  background: rgba(255,255,255,0.12);
  font-weight: bold;
}}

/* Catatan sumber */
.note {{
  margin-top: 10px;
  font-size: 12px;
  text-align: right;
  color: #ffffff;
}}
</style>
</head>

<body>
<div class="container">
  <table>
    <thead>
      <tr>
        <th>Metode</th>
        <th>Effect</th>
        <th class="num">Stat</th>
        <th class="num">Prob.</th>
        <th>Keputusan</th>
      </tr>
    </thead>
    <tbody>
      {rows}
    </tbody>
  </table>
  <div class="note">Sumber: Data diolah</div>
</div>
</body>
</html>
"""

# ======================================================
# EXPANDER UNTUK MENYEMBUNYIKAN / MENAMPILKAN TABEL
# ======================================================
with st.expander("📌 Ringkasan Pemilihan Model", expanded=False):
    components.html(html, height=275, scrolling=False)

# ======================================================
# PARAGRAF PENJELASAN PEMILIHAN MODEL
# ======================================================
st.markdown(
"""
<div style="text-align: justify; line-height: 1.6;">        Pemilihan model regresi data panel dalam penelitian ini dilakukan melalui tiga tahapan uji, yaitu uji Chow, uji Lagrange Multiplier (LM), dan uji Hausman. Berdasarkan hasil uji Chow, diperoleh nilai probabilitas sebesar 0.0000 yang lebih kecil dari tingkat signifikansi 5% (α = 0.05), sehingga dapat disimpulkan bahwa model Fixed Effect Model (FEM) lebih tepat dibandingkan dengan Common Effect Model (CEM). Selanjutnya, uji LM menunjukkan nilai probabilitas sebesar 0.0015 &lt; 0.05, yang mengindikasikan bahwa model Random Effect Model (REM) lebih sesuai dibandingkan CEM. Untuk menentukan model terbaik antara FEM dan REM, dilakukan uji Hausman, yang menghasilkan nilai probabilitas sebesar 1.0000 &gt; 0.05. Hasil ini menunjukkan bahwa model Random Effect lebih tepat digunakan karena tidak terdapat perbedaan signifikan antara FEM dan REM. Dengan demikian, model Random Effect dipilih sebagai model paling tepat untuk mengestimasi pengaruh variabel independen terhadap Foreign Direct Investment (FDI) di negara-negara ASEAN, dan seluruh pengujian hipotesis serta analisis selanjutnya dilakukan berdasarkan model ini.<br><br>

Setelah ditetapkan bahwa model regresi yang digunakan adalah Random Effect Model (REM), analisis dilanjutkan dengan melakukan uji individual (uji t) dan uji goodness of fit yang terdiri dari uji F dan penghitungan nilai koefisien determinasi (Adjusted R-squared). Uji t digunakan untuk menilai pengaruh masing-masing variabel independen secara parsial terhadap variabel dependen, yaitu Foreign Direct Investment (FDI), sedangkan uji F bertujuan untuk menguji pengaruh variabel independen secara simultan. Nilai Adjusted R-squared digunakan untuk mengetahui seberapa besar proporsi variasi dalam FDI yang dapat dijelaskan oleh variabel-variabel independen dalam model.<br><br>
</div>
""",
unsafe_allow_html=True
)

# ======================================================
# DATA HASIL REGRESI RANDOM EFFECT MODEL (REM)
# ======================================================
data = [
    ["C",   1843361056,   0.4167, 0.6816],
    ["GDP",    1081685,   2.3881, 0.0275],
    ["EXC",     786225,   3.2946, 0.0038],
    ["INF",  564779665,   2.6110, 0.0172],
    ["INT", -953322243,  -2.1247, 0.0470],
    ["EKS",  7.00e-08,    0.7947, 0.4366],
    ["POL", -123913279,  -0.0743, 0.9415],
    ["COC", 5137979989,   1.2677, 0.2202],
]

# Membuat DataFrame regresi
df = pd.DataFrame(data, columns=["Variable", "Coefficient", "t-Statistic", "Prob."])

# ======================================================
# FORMAT KOEFISIEN DAN STATISTIK
# ======================================================
df_show = df.copy()
df_show["Coefficient"] = df_show["Coefficient"].map(
    lambda x: f"{x:,.0f}".replace(",", ".") if abs(x) >= 1 else f"{x:.2E}"
)
df_show["t-Statistic"] = df_show["t-Statistic"].map(lambda x: f"{x:.4f}")
df_show["Prob."] = df_show["Prob."].map(lambda x: f"{x:.4f}")

# ======================================================
# STATISTIK MODEL (R², Adj R², F)
# ======================================================
stats_html = """
<tr>
  <td><strong>R-squared</strong></td>
  <td class="num">0.4456</td>
  <td></td>
  <td></td>
</tr>
<tr>
  <td><strong>Adjusted R-squared</strong></td>
  <td class="num">0.3909</td>
  <td></td>
  <td></td>
</tr>
<tr>
  <td><strong>F-statistic</strong></td>
  <td class="num">8.1516</td>
  <td></td>
  <td></td>
</tr>
<tr>
  <td><strong>Prob(F-statistic)</strong></td>
  <td class="num">0.0000</td>
  <td></td>
  <td></td>
</tr>
"""

# ======================================================
# MEMBANGUN BARIS HTML UNTUK TABEL
# ======================================================
rows = ""
for _, r in df_show.iterrows():
    rows += f"""
    <tr>
        <td><strong>{r['Variable']}</strong></td>
        <td class="num">{r['Coefficient']}</td>
        <td class="num">{r['t-Statistic']}</td>
        <td class="num">{r['Prob.']}</td>
    </tr>
    """

# ======================================================
# HTML + CSS UNTUK TABEL HASIL UJI REGRESI REM
# ======================================================
html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
  font-family: Arial, sans-serif;
  background: transparent;
  color: #ffffff;
}}

.container {{
  max-width: 950px;
  margin: auto;
  padding: 16px 18px;
  border-radius: 14px;
  background: #00008b;          
  border: 1px solid rgba(255,255,255,0.12);
}}

h3 {{
  text-align: center;
  margin-bottom: 14px;
  color: #ffffff;
}}

table {{
  width: 100%;
  border-collapse: collapse;
}}

th, td {{
  padding: 10px 12px;
  border-bottom: 1px solid rgba(255,255,255,0.15);
  color: #ffffff;
}}

th {{
  text-align: left;
  font-weight: bold;
}}

.num {{
  text-align: right;
  font-variant-numeric: tabular-nums;
}}

tfoot td {{
  border-top: 2px solid rgba(255,255,255,0.25);
}}

.note {{
  margin-top: 10px;
  font-size: 12px;
  text-align: right;
  color: #ffffff;
}}
</style>
</head>

<body>
<div class="container">
  <table>
    <thead>
      <tr>
        <th style="width:20%;">Variable</th>
        <th class="num">Coefficient</th>
        <th class="num">t-Statistic</th>
        <th class="num">Prob.</th>
      </tr>
    </thead>
    <tbody>
      {rows}
    </tbody>
    <tfoot>
      {stats_html}
    </tfoot>
  </table>
  <div class="note">Sumber: Data diolah</div>
</div>
</body>
</html>
"""

# ======================================================
# EXPANDER TABEL REGRESI REM
# ======================================================
with st.expander("📊 Tabel Hasil Uji Regresi Random Effect Model", expanded=False):
    components.html(html, height=610, scrolling=False)
    
# ======================================================
# PARAGRAF PENJELASAN MODEL REM
# ======================================================
st.markdown(
"""
<div style="text-align: justify; line-height: 1.6;">     
Nilai Adjusted R-squared (Adj R<sup>2</sup>) yang diperoleh sebesar 0,390916 mengindikasikan bahwa sekitar 39,09% variasi dalam nilai Foreign Direct Investment (FDI) dapat dijelaskan oleh variabel-variabel independen dalam model, seperti GDP per kapita, nilai tukar, inflasi, suku bunga deposito, ekspor, kestabilan politik, dan pengendalian korupsi. Meskipun nilai tersebut belum mencapai 50%, dalam konteks studi ekonomi dengan data panel lintas negara, angka ini tetap dianggap cukup memadai untuk merepresentasikan hubungan antar variabel yang kompleks (Gujarati & Porter, 2013). Sisanya sebesar 60,91% kemungkinan disebabkan oleh variabel-variabel lain di luar model, seperti kebijakan domestik, dinamika geopolitik, atau perubahan kebijakan perdagangan global.<br><br>

Hasil uji F menunjukkan nilai F-statistic sebesar 8.151590 dengan p-value mendekati 0.0000, yang berada jauh di bawah tingkat signifikansi 5%. Hal ini mengindikasikan bahwa model regresi secara keseluruhan signifikan, sehingga hipotesis nol yang menyatakan bahwa seluruh koefisien regresi variabel independen sama dengan nol dapat ditolak.<br><br>

Nilai konstanta (C) dalam model regresi sebesar 1.843.361.056,20 mengindikasikan bahwa ketika seluruh variabel independen dalam model diasumsikan bernilai nol, maka nilai FDI yang diharapkan tetap sebesar USD 1.843.361.056,20.<br><br>

Variabel GDP per kapita memiliki koefisien sebesar 1.081.684,56 dan p-value sebesar 0.0275 (signifikan). Variabel kurs (EXC) memiliki koefisien 786.225,09 dengan p-value 0.0038 (signifikan). Variabel inflasi (INF) memiliki koefisien 564.779.664,76 dengan p-value 0.0172 (signifikan). Variabel suku bunga deposito (INT) memiliki koefisien -953.322.243,40 dengan p-value 0.0470 (signifikan). Variabel ekspor (EKS) p-value 0.4366 (tidak signifikan). Variabel kestabilan politik (POL) p-value 0.1705 (tidak signifikan). Variabel pengendalian korupsi (COC) p-value 0.0844 (tidak signifikan pada 5%).

</div>
""",
unsafe_allow_html=True
)
