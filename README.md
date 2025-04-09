# Watermark and File Renamer Tool

Этот инструмент позволяет автоматически добавлять водяные знаки на изображения и переименовывать файлы с определёнными расширениями. Он идеально подходит для тех, кто хочет защитить свои изображения водяными знаками и организовать файлы, добавляя к их именам префикс.

## Как использовать

### 1. Установка зависимостей

Перед использованием программы необходимо установить зависимости. Для этого выполните следующие шаги:

1. Создайте виртуальное окружение (если ещё не создано):

    ```bash
    python3 -m venv venv
    ```

2. Активируйте виртуальное окружение:

    - На Windows:

        ```bash
        venv\Scripts\activate
        ```

    - На macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

### 2. Настройка конфигурации

Перед запуском программы необходимо настроить файл `config.py`. Откройте его в текстовом редакторе и заполните следующие переменные:

- `WORK_FOLDER`: Укажите путь к папке, где находятся ваши изображения и файлы. Например:

    ```python
    WORK_FOLDER = "/path/to/your/folder"
    ```

- `TEXT_TO_FILES`: Укажите текст, который будет добавлен к именам файлов. Например:

    ```python
    TEXT_TO_FILES = "Your text"
    ```

- `TEXT_TO_IMAGES`: Укажите текст, который будет использоваться в качестве водяного знака на изображениях. Например:

    ```python
    TEXT_TO_IMAGES = "Your text"
    ```

- `EXTENSIONS`: Укажите расширения файлов, которые нужно переименовать. По умолчанию:

    ```python
    EXTENSIONS = (".stl", ".zip", ".3mf", ".rar", ".webp", ".mp4", ".gif")
    ```

### 3. Запуск программы

После настройки конфигурации выполните следующие шаги:

1. Убедитесь, что виртуальное окружение активировано.

2. Запустите главный скрипт:

    ```bash
    python3 run.py
    ```

### 4. Что делает программа?

- **Добавляет водяные знаки**:

    Программа ищет все файлы с расширением `.jpg` в указанной папке и добавляет на них водяной знак с текстом, указанным в `TEXT_TO_IMAGES`.

- **Переименовывает файлы**:

    Программа ищет файлы с расширениями, указанными в `EXTENSIONS`, и добавляет к их именам префикс, указанный в `TEXT_TO_FILES`.

### 5. Пример работы

Исходная структура папки:

/path/to/your/folder/  
image1.jpg  
image2.jpg  
file1.stl  
file2.zip  

После запуска программы:

/path/to/your/folder/  
image1.jpg (с водяным знаком "Your text")  
image2.jpg (с водяным знаком "Your text")  
@your text_file1.stl  
@your text_file2.zip  

### 6. Логирование

Программа выводит результаты своей работы в консоль. Например:

Added watermark in: /path/to/your/folder/image1.jpg  
Added watermark in: /path/to/your/folder/image2.jpg  
Rename: /path/to/your/folder/file1.stl -> /path/to/your/folder/your text_file1.stl  
Rename: /path/to/your/folder/file2.zip -> /path/to/your/folder/your text_file2.zip  

Если возникнут ошибки, они также будут выведены в консоль.

### 7. Требования

- Python 3.7 или выше.
- Установленные зависимости (указаны в `requirements.txt`).

### 8. Поддержка

Если у вас есть вопросы или предложения, создайте issue в репозитории или свяжитесь со мной в tg: @olegbraun.

Теперь вы готовы использовать программу! Удачи! 😊
