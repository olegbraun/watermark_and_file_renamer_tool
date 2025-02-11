import os
from glob import glob
import random

from watermark import add_watermark

from config import WORK_FOLDER, TEXT_TO_FILES, TEXT_TO_IMAGES, EXTENSIONS


# Рекурсивно ищем все .jpg файлы
jpg_files = glob(os.path.join(WORK_FOLDER, "*.jpg"), recursive=True)

# Обрабатываем каждый файл
for jpg_file in jpg_files:
    try:
        add_watermark(image_path=jpg_file, text=TEXT_TO_IMAGES)
        print(f"Added watermark in: {jpg_file}")
    except Exception as e:
        print(f"Error added watermark {jpg_file}: {str(e)}")


# Рекурсивно ищем все файлы с нужными расширениями
for ext in EXTENSIONS:
    files = glob(os.path.join(WORK_FOLDER, "*" + ext), recursive=True)
    # Переименовываем каждый файл
    for file_path in files:
        try:
            # Получаем директорию и имя файла
            dir_name, file_name = os.path.split(file_path)
            # Разделяем имя файла и его расширение
            name_without_extension, extension = os.path.splitext(file_name)         
            # Генерация уникального числа из 6 цифр
            unique_number = str(random.randint(100000, 999999))
            # Новое имя файла
            new_name = f"{TEXT_TO_FILES}_{unique_number}{extension}"
            new_path = os.path.join(dir_name, new_name)
            # Переименовываем файл
            os.rename(file_path, new_path)
            print(f"Rename: {file_path} -> {new_path}")
        except Exception as e:
            print(f"Error rename {file_path}: {str(e)}")