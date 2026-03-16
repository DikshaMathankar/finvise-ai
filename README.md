# FinVise AI - Indian Stock Market Intelligence Platform

## Live URL
https://dikshamathankar-finvise-ai.streamlit.app

## What it does
- Real-time NSE/BSE stock data for any ticker
- Latest news fetching from Economic Times
- AI-generated 90-second beginner-friendly video script
- Auto video generation with voiceover

## Tech Stack
- Python
- Streamlit
- yFinance (stock data)
- gTTS (text to speech)
- MoviePy (video generation)
- Groq LLaMA3 (AI summary)

## Setup Instructions

### 1. Clone the repo
git clone https://github.com/DikshaMathankar/finvise-ai.git
cd finvise-ai

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the app
streamlit run app.py

### 4. Open browser
http://localhost:8501

## Architecture
1. User enters NSE/BSE ticker
2. yFinance fetches live stock data
3. Economic Times RSS fetches latest news
4. Groq LLaMA3 generates 90-second script
5. gTTS converts script to voiceover
6. MoviePy combines audio and visuals into MP4

## Sample Tickers to Test
- RELIANCE
- TCS
- INFY
- HDFCBANK
- SBIN
