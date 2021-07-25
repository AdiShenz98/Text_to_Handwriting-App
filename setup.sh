mkdir -p ~/.streamlit/

echo "[theme]
primaryColor = ‘#ffe3e3’
backgroundColor = ‘#262a53’
secondaryBackgroundColor = ‘#4f575a’
textColor= ‘#ffa0a0’
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml