
import streamlit as st
from stock_data import get_stock_data
from news_fetcher import get_news
from ai_summary import generate_summary
from video_generator import create_video

st.title("FinVise AI - Indian Stock Intelligence")
ticker = st.text_input("Enter NSE Stock Ticker (Example: RELIANCE)")

if st.button("Analyze Stock"):
    if not ticker:
        st.warning("Please enter a ticker!")
    else:
        ticker = ticker.strip().upper()
        with st.spinner("Fetching stock data..."):
            stock = get_stock_data(ticker, "NSE")
        st.subheader("Stock Data")
        st.write(stock)
        with st.spinner("Fetching news..."):
            news = get_news(ticker)
        st.subheader("Latest News")
        for n in news:
            st.write("*", n["title"])
        with st.spinner("Generating AI script..."):
            script = generate_summary(stock, news, ticker)
        st.subheader("Generated Script")
        st.write(script)
        with st.spinner("Generating video... (takes 30-60 sec)"):
            video_path = create_video(script, ticker)
        if video_path:
            st.video(video_path)
        else:
            st.error("Video generation failed.")
