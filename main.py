import streamlit as st
import yfinance as yf
import pandas as pd

# Judul aplikasi
st.title("📈 AI Stock Assistant")

# Input kode saham
ticker = st.text_input("Masukkan kode saham (contoh: AAPL, TSLA, BBCA.JK)", "AAPL")

if ticker:
    # Ambil data saham dari Yahoo Finance
    data = yf.download(ticker, period="1mo", interval="1d")

    if not data.empty:
        st.subheader(f"📊 Harga Penutupan {ticker}")
        st.line_chart(data["Close"])

        st.subheader("📄 Data Terbaru")
        st.write(data.tail())
    else:
        st.warning("⚠️ Data saham tidak ditemukan, coba kode lain.")
