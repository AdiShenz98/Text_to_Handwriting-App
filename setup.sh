mkdir -p ~/.streamlit/

echo "[theme]\
primaryColor = ‘#ffe3e3’\n\
backgroundColor = ‘#262a53’\n\
secondaryBackgroundColor = ‘#4f575a’\n\
textColor= ‘#ffa0a0’\n\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
" > ~/.streamlit/config.toml
