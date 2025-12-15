import os
import io
import pandas as pd
import streamlit as st
import plotly.express as px

# ------------------------------------------------------------
# Konfigurasi halaman (judul & layout)
# ------------------------------------------------------------
st.set_page_config(page_title="Data World Bank", layout="wide")
st.title("Visualisasi Data")

# ------------------------------------------------------------
# Daftar indikator yang tersedia di sistem
# ------------------------------------------------------------
INDICATORS = ["FDI", "GDP", "EXC", "INF", "EKS", "INT", "POL", "COC"]

# ------------------------------------------------------------
# Mapping nama negara -> kode ISO3 untuk Plotly choropleth
# ------------------------------------------------------------
ISO3_MAP = {
    "Indonesia": "IDN",
    "Malaysia": "MYS",
    "Viet Nam": "VNM",
    "Vietnam": "VNM",
    "Thailand": "THA",
}

# ------------------------------------------------------------
# Fungsi baca CSV + bersihkan tipe data (cache agar lebih cepat)
# ------------------------------------------------------------
@st.cache_data
def load_data(csv_path: str) -> pd.DataFrame:
    # Baca data CSV
    df = pd.read_csv(csv_path)

    # Validasi kolom wajib
    required_cols = {"Negara", "Tahun"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Kolom wajib tidak ada: {missing}")

    # Konversi Tahun ke angka, buang baris yang invalid
    df["Tahun"] = pd.to_numeric(df["Tahun"], errors="coerce")
    df = df.dropna(subset=["Negara", "Tahun"])
    df["Tahun"] = df["Tahun"].astype(int)

    # Bersihkan angka: "1,234.56" -> 1234.56 (hilangkan koma ribuan)
    for col in INDICATORS:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col].astype(str).str.replace(",", "", regex=False),
                errors="coerce"
            )

    return df


# ------------------------------------------------------------
# Menentukan path data/data.csv dari file pages/page4.py
# pages/page4.py -> naik 1 level (root) -> masuk data -> data.csv
# ------------------------------------------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CSV_PATH = os.path.join(ROOT_DIR, "data", "data.csv")

# Jika file tidak ketemu, stop agar jelas errornya
if not os.path.exists(CSV_PATH):
    st.error(f"File tidak ditemukan: {CSV_PATH}\nPastikan ada `data/data.csv` di project kamu.")
    st.stop()

# Load data
df = load_data(CSV_PATH)
if df.empty:
    st.warning("Data kosong.")
    st.stop()

# ------------------------------------------------------------
# UI FILTER (negara, tahun, indikator)
# ------------------------------------------------------------
st.subheader("Filter")

# Ambil list negara dan range tahun dari data
negara_all = sorted(df["Negara"].dropna().unique().tolist())
tahun_min, tahun_max = int(df["Tahun"].min()), int(df["Tahun"].max())

# Buat 3 kolom agar filter rapi
col1, col2, col3 = st.columns([2, 2, 3])

with col1:
    # Multiselect negara (boleh lebih dari satu)
    negara_pick = st.multiselect(
        "Pilih Negara",
        options=negara_all,
        default=negara_all[:1] if negara_all else []
    )

with col2:
    # Slider rentang tahun (min..max)
    year_range = st.slider(
        "Rentang Tahun",
        min_value=tahun_min,
        max_value=tahun_max,
        value=(tahun_min, tahun_max),
        step=1
    )

with col3:
    # Multiselect indikator (hanya yang benar-benar ada di kolom CSV)
    indikator_pick = st.multiselect(
        "Pilih Indikator",
        options=[c for c in INDICATORS if c in df.columns],
        default=["GDP"] if "GDP" in df.columns else []
    )

# ------------------------------------------------------------
# Jika indikator kosong: chart line & peta harus tidak tampil
# (tapi tab tabel data tetap boleh tampil)
# ------------------------------------------------------------
indikator_kosong = (len(indikator_pick) == 0)

# Jika negara kosong, data tidak bisa divisualisasikan, tapi tabel tetap bisa (opsional)
negara_kosong = (len(negara_pick) == 0)

# ------------------------------------------------------------
# Terapkan filter ke data untuk dipakai semua tab
# ------------------------------------------------------------
df_filtered = df[
    (df["Tahun"] >= year_range[0]) &
    (df["Tahun"] <= year_range[1])
].copy()

if not negara_kosong:
    df_filtered = df_filtered[df_filtered["Negara"].isin(negara_pick)].copy()

# ============================================================
# 3 TAB
# ============================================================
tab_line, tab_map, tab_table = st.tabs(["📈 Chart Line", "🌍 Peta Dunia", "📋 Tabel Data & Download"])

# ============================================================
# TAB 1 — CHART LINE
# ============================================================
with tab_line:
    st.subheader("Chart Line per Indikator")

    # Kondisi hide: indikator kosong atau negara belum dipilih
    if indikator_kosong or negara_kosong:
        st.info("Chart Line disembunyikan: pilih minimal 1 negara dan 1 indikator.")
    else:
        if df_filtered.empty:
            st.warning("Data kosong setelah filter. Coba ubah negara / tahun.")
        else:
            # Plot satu per satu indikator agar jelas per slide presentasi
            for ind in indikator_pick:
                # Ambil kolom yang diperlukan, drop NaN supaya chart bersih
                plot_df = df_filtered[["Negara", "Tahun", ind]].dropna()

                # Jika indikator ini tidak ada datanya, tampilkan info saja
                if plot_df.empty:
                    st.info(f"Tidak ada data untuk indikator {ind} setelah filter.")
                    continue

                # Buat line chart: x=Tahun, y=indikator, warna=Negara
                fig = px.line(
                    plot_df,
                    x="Tahun",
                    y=ind,
                    color="Negara",
                    markers=True,
                    title=f"{ind} vs Tahun"
                )

                # Tinggi chart agar enak dibaca
                fig.update_layout(height=420, legend_title_text="Negara")

                # Render chart di Streamlit
                st.plotly_chart(fig, use_container_width=True)

# ============================================================
# TAB 2 — PETA ASEAN (bukan dunia)
# ============================================================
with tab_map:
    st.subheader("Peta ASEAN per Indikator (Highlight Negara Terpilih)")

    # Kondisi hide: indikator kosong atau negara belum dipilih
    if indikator_kosong or negara_kosong:
        st.info("Peta disembunyikan: pilih minimal 1 negara dan 1 indikator.")
    else:
        # ------------------------------------------------------------
        # (OPSIONAL) Lengkapi ISO3 untuk negara ASEAN lain
        # Agar aman kalau dataset kamu nambah negara
        # ------------------------------------------------------------
        ISO3_MAP.update({
            "Singapore": "SGP",
            "Brunei": "BRN",
            "Brunei Darussalam": "BRN",
            "Philippines": "PHL",
            "Cambodia": "KHM",
            "Lao PDR": "LAO",
            "Laos": "LAO",
            "Myanmar": "MMR",
            "Timor-Leste": "TLS",
            "East Timor": "TLS",
        })

        # Ambil tahun terakhir dari rentang filter
        map_year = year_range[1]
        map_base = df[df["Tahun"] == map_year].copy()

        # Ambil hanya negara yang dipilih
        map_sel = map_base[map_base["Negara"].isin(negara_pick)].copy()

        # Tambahkan kolom iso3 hasil mapping
        map_sel["iso3"] = map_sel["Negara"].map(ISO3_MAP)

        # Buang baris yang iso3-nya tidak ada (tidak bisa dimapping)
        map_sel = map_sel.dropna(subset=["iso3"])

        if map_sel.empty:
            st.warning(
                "Tidak ada negara yang bisa ditampilkan di peta.\n"
                "Pastikan nama negara di CSV cocok dengan ISO3_MAP."
            )
        else:
            # ------------------------------------------------------------
            # Batas wilayah ASEAN (perkiraan aman)
            # lon: 92 s/d 142, lat: -15 s/d 25
            # Ini meng-cover: Indonesia, Malaysia, Thailand, Vietnam, dll.
            # ------------------------------------------------------------
            ASEAN_LON_RANGE = [92, 142]
            ASEAN_LAT_RANGE = [-15, 25]

            # Buat peta per indikator
            for ind in indikator_pick:
                z_df = map_sel[["Negara", "iso3", ind]].dropna()

                if z_df.empty:
                    st.info(f"Tidak ada data peta untuk {ind} pada tahun {map_year}.")
                    continue

                fig_map = px.choropleth(
                    z_df,
                    locations="iso3",
                    color=ind,
                    hover_name="Negara",
                    color_continuous_scale="Viridis",
                    title=f"Peta ASEAN — {ind} (Tahun {map_year})"
                )

                # ------------------------------------------------------------
                # Kunci viewport agar fokus ASEAN (bukan world)
                # ------------------------------------------------------------
                fig_map.update_geos(
                    projection_type="mercator",
                    showframe=False,
                    showcoastlines=True,
                    lonaxis_range=ASEAN_LON_RANGE,
                    lataxis_range=ASEAN_LAT_RANGE,
                    fitbounds=False  # jangan auto-fit ke dunia
                )

                fig_map.update_layout(
                    height=520,
                    margin=dict(l=10, r=10, t=60, b=10)
                )

                st.plotly_chart(fig_map, use_container_width=True)


# ============================================================
# TAB 3 — TABEL DATA + DOWNLOAD
# ============================================================
with tab_table:
    st.subheader("Tabel Data (sesuai filter)")

    if df_filtered.empty:
        st.warning("Data kosong setelah filter.")
    else:
        # Pilih kolom yang akan ditampilkan:
        # - selalu tampilkan Negara & Tahun
        # - indikator: tampilkan semua indikator yang dipilih (kalau kosong, tampilkan semua indikator yang ada)
        cols_to_show = ["Negara", "Tahun"]
        if not indikator_kosong:
            cols_to_show += indikator_pick
        else:
            # kalau indikator tidak dipilih, tetap tampilkan seluruh indikator yang ada di file
            cols_to_show += [c for c in INDICATORS if c in df_filtered.columns]

        # Data final untuk tabel
        table_df = df_filtered[cols_to_show].copy()

        # Tampilkan tabel interaktif
        st.dataframe(table_df, use_container_width=True)

        st.divider()
        st.subheader("Download Data")

        # ---------- Download CSV ----------
        # Convert dataframe -> CSV bytes agar bisa di-download
        csv_bytes = table_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="⬇️ Download CSV",
            data=csv_bytes,
            file_name="data_terfilter.csv",
            mime="text/csv",
        )

        # ---------- Download Excel ----------
        # Convert dataframe -> Excel di memory (BytesIO) agar bisa di-download
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            table_df.to_excel(writer, index=False, sheet_name="FilteredData")
        excel_bytes = output.getvalue()

        st.download_button(
            label="⬇️ Download Excel",
            data=excel_bytes,
            file_name="data_terfilter.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

st.divider()
st.caption("Sumber data: World Bank")
