# Анализ и визуализация данных об акциях

## Ссылка на проект

[Ссылка на проект](https://github.com/lubyantsev/061220241613)

## Общий обзор

Этот проект предназначен для загрузки и визуализации исторических данных об акциях, используя библиотеку yfinance для
получения данных и matplotlib для создания графиков. Пользователи могут выбирать различные тикеры и временные периоды
для анализа, а также просматривать движение цен и скользящие средние на графике. Проект помогает не только в
визуализации данных, но и в их анализе, предоставляя возможность отслеживания колебаний цен.

## Структура и модули проекта

1. **data_download.py**:
    - Ответственный за загрузку данных об акциях.
    - Содержит функции для извлечения данных из интернета и вычисления скользящего среднего.

2. **main.py**:
    - Точка входа в программу.
    - Запрашивает у пользователя тикер акции и временной период, загружает и обрабатывает данные, а затем визуализирует
      результаты.

3. **data_plotting.py**:
    - Отвечает за визуализацию данных.
    - Содержит функции для создания и сохранения графиков цен закрытия и скользящих средних.

4. **data_analysis.py**:
    - Содержит функции для анализа данных.
    - Позволяет рассчитывать среднюю цену закрытия и уведомляет о сильных колебаниях цен.
    - Включает функцию export_data_to_csv для экспорта данных о ценах акций в CSV файл.

## Описание функций

### 1. data_download.py:

- **fetch_stock_data(ticker, period='1mo')**:
  Получает исторические данные об акциях для указанного тикера и временного периода.

- **add_moving_average(data, window_size=5)**:
  Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.

### 2. main.py:

- **main()**:
  Основная функция, управляющая процессом загрузки, обработки данных и их визуализации, запрашивая у пользователя ввод
  данных и вызывая соответствующие функции.

### 3. data_plotting.py:

- **create_and_save_plot(data, ticker, period, filename=None)**:
  Создаёт график, отображающий цены закрытия и скользящие средние, с возможностью сохранения графика в файл.

### 4. data_analysis.py:

- **calculate_and_display_average_price(data)**:
  Рассчитывает и отображает среднюю цену закрытия за указанный период.

- **notify_if_strong_fluctuations(data, threshold)**:
  Уведомляет, если цены акций колебались более чем на заданный процент.

- **export_data_to_csv(data, filename)**:
  Экспортирует данные о ценах акций в CSV файл в папку csv_files.

## Пошаговое использование

Этот проект предоставляет пользователю возможность анализировать и визуализировать исторические данные акций. Следуйте
этим шагам, чтобы начать работу с проектом:

### Шаг 1: Установка необходимых библиотек

Убедитесь, что у вас установлены необходимые библиотеки. Вы можете установить их с помощью pip:

```bash
pip install yfinance matplotlib pandas
```

### Шаг 2: Запуск программы

1. Откройте файл `main.py` в вашем IDE (например, PyCharm).
2. Запустите файл с помощью команды:

```bash
python main.py
```

### Шаг 3: Ввод данных

После запуска программы вы увидите приветственное сообщение с инструкциями:

- Введите тикер акции, который вы хотите проанализировать (например, AAPL для акций Apple).
- Введите период для получения данных (например, 1mo для данных за один месяц).
- Введите порог для уведомления о колебаниях в процентах (например, 5 для 5%).
- Если вы хотите экспортировать полученные данные в CSV файл, введите имя файла, например, `stock_data.csv`. Если
  экспорт не нужен, просто нажмите Enter.

### Шаг 4: Просмотр результатов

После ввода данных программа выполнит следующие действия:

1. Загрузит данные о выбранной акции за указанный период.
2. Рассчитает скользящее среднее и добавит его в набор данных.
3. Создаст график, на котором будут отображены цены закрытия и скользящие средние, и сохранит его в папке `charts`.
4. Рассчитает и отобразит среднюю цену закрытия за указанный период.
5. Уведомит вас о сильных колебаниях цен, если они превышают заданный вами порог.
6. Экспортирует данные о ценах акций в CSV файл.

### Шаг 5: Просмотр графика

После завершения работы программы вы можете найти график в папке `charts` в вашем проекте. Имя файла будет сгенерировано
автоматически, основываясь на тикере и периоде.

### Шаг 6: Анализ данных

Используйте полученные результаты для анализа поведения цен акций. Вы можете повторять процесс с разными тикерами и
периодами, чтобы исследовать различные тренды и колебания на рынке.

### Примечания

- Убедитесь, что вы используете актуальные тикеры акций, так как устаревшие или неверные тикеры могут привести к ошибкам
  при загрузке данных.
- Проверяйте консоль на наличие сообщений об ошибках, если данные не загружаются или возникают другие проблемы.
- Для более глубокого анализа вы можете модифицировать функции в `data_analysis.py` или добавлять новые функции в
  зависимости от ваших потребностей.