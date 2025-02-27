import data_download as dd
import data_plotting as dplt
from data_analysis import calculate_and_display_average_price, notify_if_strong_fluctuations, \
    export_data_to_csv  # Импортируем обе функции


def main():
    """
    Основная функция, управляющая процессом загрузки, обработки и визуализации данных о биржевых акциях.

    Функция выполняет следующие действия:
    1. Приветствует пользователя и предоставляет информацию о доступных тикерах и периодах.
    2. Запрашивает ввод тикера акции и периода для получения данных.
    3. Запрашивает порог для уведомления о колебаниях цен.
    4. Загружает данные о выбранной акции за указанный период.
    5. Добавляет скользящее среднее к загруженным данным.
    6. Строит и сохраняет график цен закрытия и скользящих средних.
    7. Рассчитывает и отображает среднюю цену закрытия.
    8. Уведомляет пользователя о сильных колебаниях цен, если они превышают заданный порог.
    """

    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5л, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # Запрос порога колебаний
    threshold = float(input("Введите порог для уведомления о колебаниях (в процентах): "))

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Calculate additional indicators
    stock_data = dd.calculate_rsi(stock_data)
    stock_data = dd.calculate_macd(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period, filename_prefix=ticker)

    # Calculate and display the average price
    calculate_and_display_average_price(stock_data)

    # Notify if there are strong fluctuations
    notify_if_strong_fluctuations(stock_data, threshold)  # Вызов новой функции

    # Export data to CSV
    export_filename = input("Введите имя файла для экспорта данных (например, 'stock_data.csv'): ")
    export_data_to_csv(stock_data, export_filename)


if __name__ == "__main__":
    main()
