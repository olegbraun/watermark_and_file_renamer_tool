from PIL import Image, ImageDraw, ImageFont, ImageFilter

def add_watermark(image_path: str, text: str):
    # Открываем изображение
    original_image = Image.open(image_path).convert("RGBA")
    width, height = original_image.size
    
    # Создаем прозрачный слой для водяного знака
    watermark = Image.new("RGBA", original_image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(watermark)
    
    # Параметры шрифта
    try:
        font = ImageFont.truetype("ZTTalk-Medium.ttf", int(height / 20))
    except:
        font = ImageFont.load_default()

    # Рассчитываем размер текста и позицию
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    margin = 20  # Отступ от краев
    x = width - text_width - margin
    y = height - text_height - margin

    # Добавляем тень
    shadow = Image.new("RGBA", original_image.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    for i in range(3):
        shadow_draw.text((x + i, y + i), text, font=font, fill=(0, 0, 0, 100))
    shadow = shadow.filter(ImageFilter.BLUR)

    # Основной текст
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 180))
    
    # Комбинируем все элементы
    watermarked = Image.alpha_composite(original_image, shadow)
    watermarked = Image.alpha_composite(watermarked, watermark)
    
    # Сохраняем изображение уже с водяной маркой 
    watermarked.convert("RGB").save(image_path, quality=95)