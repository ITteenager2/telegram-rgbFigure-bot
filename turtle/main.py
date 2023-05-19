import os
import random
from PIL import Image, ImageDraw
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Инициализация бота и диспетчера
bot = Bot(token="5687225241:AAG3whxh3RKEeMQhvxOG2-TNKu1r02aPuX8")
dp = Dispatcher(bot)

# Создание папки для сохранения изображений
if not os.path.exists("images"):
    os.makedirs("images")


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Пиши команду вида 'фигура цвет', например 'треугольник красный'")


@dp.message_handler()
async def draw_shape(message: types.Message):
    text = message.text.lower()

    # Парсинг команды на название фигуры и цвет
    shape_name, color_name = parse_command(text)

    # Проверка названия фигуры и вызов соответствующей функции рисования
    if shape_name == 'треугольник':
        image_path = draw_triangle(color_name)
    elif shape_name == 'квадрат':
        image_path = draw_square(color_name)
    elif shape_name == 'круг':
        image_path = draw_circle(color_name)
    elif shape_name == 'лицо':
        image_path = draw_face(color_name)
    else:
        await message.reply("Я не знаю такой фигуры.")
        return

    # Отправка изображения пользователю
    with open(image_path, 'rb') as f:
        await bot.send_photo(message.chat.id, photo=f)

    # Удаление изображения после отправки
    os.remove(image_path)


def parse_command(text):
    # Разделение команды на название фигуры и цвет
    parts = text.split(' ')
    shape_name = parts[0]
    color_name = parts[1] if len(parts) > 1 else None
    return shape_name, color_name


def draw_triangle(color):
    # Создание нового изображения с белым фоном
    image = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(image)

    # Преобразование названия цвета в RGB
    color_rgb = get_rgb_from_name(color)
    if color_rgb is None:
        # Генерация случайных значений цвета для компонентов RGB, если цвет не определен
        color_rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Рисование треугольника с заданным или случайным цветом
    draw.polygon([(150, 0), (0, 300), (300, 300)], fill=color_rgb)

    # Сохранение изображения с названием "triangle.png"
    image_name = "triangle.png"
    image_path = os.path.join("images", image_name)
    image.save(image_path)

    return image_path


def draw_square(color):
    # Создание нового изображения с белым фоном
    image = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(image)

    # Преобразование названия цвета в RGB
    color_rgb = get_rgb_from_name(color)
    if color_rgb is None:
        # Генерация случайных значений цвета для компонентов RGB, если цвет не определен
        color_rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Рисование квадрата с заданным или случайным цветом
    draw.rectangle([(50, 50), (250, 250)], fill=color_rgb)

    # Сохранение изображения с названием "square.png"
    image_name = "square.png"
    image_path = os.path.join("images", image_name)
    image.save(image_path)

    return image_path


def draw_circle(color):
    # Создание нового изображения с белым фоном
    image = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(image)

    # Преобразование названия цвета в RGB
    color_rgb = get_rgb_from_name(color)
    if color_rgb is None:
        # Генерация случайных значений цвета для компонентов RGB, если цвет не определен
        color_rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Рисование круга с заданным или случайным цветом
    draw.ellipse([(50, 50), (250, 250)], fill=color_rgb)

    # Сохранение изображения с названием "circle.png"
    image_name = "circle.png"
    image_path = os.path.join("images", image_name)
    image.save(image_path)

    return image_path


def draw_face(color):
    # Создание нового изображения с белым фоном
    image = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(image)

    # Преобразование названия цвета в RGB
    color_rgb = get_rgb_from_name(color)
    if color_rgb is None:
        # Использование желтого цвета, если цвет не определен
        color_rgb = (255, 255, 0)

    # Рисование лица с заданным или желтым цветом
    draw.ellipse([(50, 50), (250, 250)], fill=color_rgb)

    # Цвет глаз (черный)
    eye_color = (0, 0, 0)
    # Рисование глаз
    draw.ellipse([(100, 100), (125, 125)], fill=eye_color)
    draw.ellipse([(175, 100), (200, 125)], fill=eye_color)

    # Цвет рта (красный)
    mouth_color = (255, 0, 0)
    # Рисование рта
    draw.arc([(100, 150), (200, 200)], start=190, end=350, fill=mouth_color, width=10)

    # Сохранение изображения с названием "face.png"
    image_name = "face.png"
    image_path = os.path.join("images", image_name)
    image.save(image_path)

    return image_path


def get_rgb_from_name(color_name):
    # Преобразование названия цвета в RGB
    colors = {
        'красный': (255, 0, 0),
        'зеленый': (0, 255, 0),
        'зелёный': (0, 255, 0),
        'синий': (0, 0, 255),
        'фиолетовый': (128,0,128),
        'Маджента': (255, 0, 255,),
        'розовый': (220,20,60),
        'золотой': (255,215,0),
        'малиновый': (220,20,60),
        'белый': (255,250,250),
        'черный': (0, 0,0),
        'сбм': (115, 81, 132),
        'крк': (204, 78, 92),

    }
    return colors.get(color_name)


if __name__ == '__main__':
    executor.start_polling(dp)

