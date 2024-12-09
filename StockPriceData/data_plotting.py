import matplotlib.pyplot as plt
import pandas as pd
import os

def create_and_save_plot(data, ticker, period, filename_prefix=None):
    """
    Создает и сохраняет графики для цен закрытия, RSI и MACD.
    """
    # Создаем папку 'charts', если она не существует
    if not os.path.exists('charts'):
        os.makedirs('charts')

    filename_prefix = filename_prefix or f"{ticker}_{period}"

    # График цен закрытия и скользящих средних
    plt.figure(figsize=(14, 6))
    if 'Date' in data.columns:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price', color='blue')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average', color='orange')
        plt.title(f'{ticker} - Close Price and Moving Average for {period}')
        plt.xlabel("Date")
    else:
        plt.plot(data['Close'], label='Close Price', color='blue')
        plt.plot(data['Moving_Average'], label='Moving Average', color='orange')
        plt.title(f'{ticker} - Close Price and Moving Average for {period}')

    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join('charts', f"{filename_prefix}_Close_MA.png"))
    plt.close()

    # График RSI
    plt.figure(figsize=(14, 6))
    plt.plot(data['RSI'], label='RSI', color='purple')
    plt.axhline(70, linestyle='--', alpha=0.5, color='red', label='Overbought')
    plt.axhline(30, linestyle='--', alpha=0.5, color='green', label='Oversold')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join('charts', f"{filename_prefix}_RSI.png"))
    plt.close()

    # График MACD
    plt.figure(figsize=(14, 6))
    plt.plot(data['MACD'], label='MACD', color='blue')
    plt.plot(data['Signal_Line'], label='Signal Line', color='orange')
    plt.title('MACD')
    plt.xlabel("Date")
    plt.ylabel("MACD")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join('charts', f"{filename_prefix}_MACD.png"))
    plt.close()

    print(f"Графики сохранены в папке 'charts' с префиксом {filename_prefix}.")