# Kaim3 Stock Price and Financial News Analysis

## Project Overview
This project analyzes correlations between financial news sentiment and stock price movements for major companies like Apple and Amazon. The system combines exploratory stock data analysis with NLP-based news sentiment evaluation.

## Repository Structure
```bash
kaim3-stock-price-analysis
├── datasets
├── LICENSE
├── notebook
│   ├── amazon_stock-EDA.ipynb
│   ├── apple_stock-EDA.ipynb
│   ├── __init__.py
│   └── news_sentiment.ipynb
├── README.md
├── requirements.txt
├── scripts
│   ├── __init__.py
│   ├── load_data.py
│   ├── sentiment_score.py
│   ├── stock_data_analysis.py
│   ├── visualize_stock_data.py
│   └── word_analyer.py
└── tests
    └── __init__.py
```

## Installation
```bash
git clone https://github.com/your-username/kaim3-stock-price-analysis.git
cd kaim3-stock-price-analysis

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt