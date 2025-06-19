
import streamlit as st
import pandas as pd
from utils import load_data, add_indicators, predict_signal

st.set_page_config(page_title="BO予測AIツール", layout="wide")

st.title("📊 バイナリーオプション予測AIツール")
uploaded_file = st.file_uploader("📁 CSVファイルをアップロード（例：OHLC）", type="csv")

if uploaded_file is not None:
    df = load_data(uploaded_file)
    df = add_indicators(df)
    df['予測シグナル'] = predict_signal(df)
    st.dataframe(df.tail(100))

    st.line_chart(df[['Close', 'ボリンジャー_上限', 'ボリンジャー_下限']].tail(100))
    st.success("✅ 最新データと予測を表示しました")
else:
    st.info("デモ用データを使用中")
    df = load_data("data/sample_data.csv")
    df = add_indicators(df)
    df['予測シグナル'] = predict_signal(df)
    st.dataframe(df.tail(100))
    st.line_chart(df[['Close', 'ボリンジャー_上限', 'ボリンジャー_下限']].tail(100))
