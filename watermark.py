from PIL import Image, ImageDraw, ImageFont, ImageFilter

import math
import os

def add_watermark(
        image_path: str,
        text: str,
        text_opacity: int = 200,  # Прозрачность текста (0-255)
        stroke_opacity: int = 100  # Прозрачность обводки (0-255)
):
    """
    Добавляет диагональный водяной знак на изображение
    :param image_path: Путь к изображению
    :param text: Текст водяного знака
    :param text_opacity: Прозрачность текста (0 - полностью прозрачный, 255 - непрозрачный)
    :param stroke_opacity: Прозрачность обводки (0 - полностью прозрачный, 255 - непрозрачный)
    """
    # Проверка корректности параметров прозрачности
    if not 0 <= text_opacity <= 255:
        raise ValueError("text_opacity должен быть в диапазоне 0-255")
    if not 0 <= stroke_opacity <= 255:
        raise ValueError("stroke_opacity должен быть в диапазоне 0-255")
    # Проверяем существование файла
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    # Открываем изображение
    try:
        original_image = Image.open(image_path).convert("RGBA")
    except Exception as e:
        raise ValueError(f"Could not open image file: {e}")
    width, height = original_image.size
    # Создаем прозрачный слой для водяного знака
    watermark = Image.new("RGBA", original_image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(watermark)
    # Рассчитываем базовый размер шрифта
    base_size = min(width, height)
    base_font_size = int(base_size / 12)
    stroke_width = max(2, base_font_size // 15)
    # Пробуем разные варианты шрифтов
    font = None
    font_paths = [
        "../ZTTalk-Medium.ttf", "ZTTalk-Medium.ttf"
    ]
    for font_path in font_paths:
        try:
            font = ImageFont.truetype(font_path, base_font_size)
            break
        except:
            continue
    if font is None:
        font = ImageFont.load_default()
        base_font_size = font.size
    # Рассчитываем отступы (20%)
    margin_x = int(width * 0.20)
    margin_y = int(height * 0.20)
    # Точки диагонали
    start_point = (margin_x, height - margin_y)
    end_point = (width - margin_x, margin_y)
    # Рассчитываем угол наклона
    dx = end_point[0] - start_point[0]
    dy = end_point[1] - start_point[1]
    angle = math.degrees(math.atan2(dy, dx))
    # Подбираем размер шрифта
    diagonal_length = math.sqrt(dx ** 2 + dy ** 2)
    required_text_width = diagonal_length * 0.9
    while True:
        test_font = ImageFont.truetype(font.path, base_font_size) if hasattr(font, 'path') else font
        text_bbox = draw.textbbox((0, 0), text, font=test_font)
        text_width = text_bbox[2] - text_bbox[0]
        if text_width < required_text_width or base_font_size <= 10:
            font = test_font
            break
        base_font_size -= 1
        if hasattr(font, 'path'):
            try:
                font = ImageFont.truetype(font.path, base_font_size)
            except:
                break
    # Создаем временное изображение для текста
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_image = Image.new("RGBA", (int(text_width * 1.5), int(text_height * 2)), (0, 0, 0, 0))
    text_draw = ImageDraw.Draw(text_image)
    # Рисуем текст с заданной прозрачностью
    text_position = (text_image.width // 4, text_image.height // 4)
    text_draw.text(
        text_position,
        text,
        font=font,
        fill=(255, 255, 255, text_opacity),  # Используем переданную прозрачность текста
        stroke_width=stroke_width,
        stroke_fill=(0, 0, 0, stroke_opacity)  # Используем переданную прозрачность обводки
    )
    # Поворачиваем текст
    rotated_text = text_image.rotate(-angle, expand=True, resample=Image.BICUBIC, fillcolor=(0, 0, 0, 0))
    # Позиционируем текст
    text_center_x = (start_point[0] + end_point[0]) // 2
    text_center_y = (start_point[1] + end_point[1]) // 2
    paste_position = (
        text_center_x - rotated_text.width // 2,
        text_center_y - rotated_text.height // 2
    )
    # Накладываем текст
    watermark.paste(rotated_text, paste_position, rotated_text)
    # Размытие
    watermark = watermark.filter(ImageFilter.GaussianBlur(radius=1.5))
    # Наложение водяного знака
    watermarked = Image.alpha_composite(original_image, watermark)
    # Сохраняем результат
    try:
        watermarked.convert("RGB").save(image_path, quality=95)
    except Exception as e:
        print(f"Произошла ошибка при добавлении водяной марки к изображению: {image_path}")