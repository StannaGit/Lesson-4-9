# ------------------------  Технології Computer Vision з python -------------------------------

'''
Цифрова обробка зображень: ласичні алгоритми "сирої" обробки растрового зображення з апакетом  Pillow (PIL)
Джерела даних:
https://www.kaggle.com/datasets
https://www.sentinel-hub.com/
https://livingatlas2.arcgis.com/landsatexplorer/

Package         Version
--------------- -------
matplotlib      3.8.2
pillow          10.2.0

'''

import random
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN)
from abc import ABC, abstractmethod


# --------------------- зчитування файлу зображення ----------------------
class ImageRead:

    @staticmethod
    def image_read(file_name: str):
        image = Image.open(file_name)  # відкриття файлу зображення
        draw = ImageDraw.Draw(image)  # створення інструменту для малюванн
        return {
            "image_file": image,
            "image_draw": draw,
            "image_width": image.size[0],  # визначення ширини картинки
            "image_height": image.size[1],  # визначення висоти картинки
            "image_pix": image.load()  # отримання значень пікселей для картинки
        }


class ImageSaver:

    @staticmethod
    def show(image):
        plt.imshow(image)
        plt.show()

    @staticmethod
    def save(image, file_name: str):
        image.save(file_name, "JPEG")


class ImageFilter(ABC):

    @abstractmethod
    def apply(self, image_info: dict) -> Image:
        pass


class ShadesOfGrayFilter(ImageFilter):

    def apply(self, image_info: dict) -> Image:
        image = image_info["image_file"]
        draw = image_info["image_draw"]
        width, height = image_info["image_width"], image_info["image_height"]
        pix = image_info["image_pix"]

        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a + b + c) // 3
                draw.point((i, j), (S, S, S))

        return image

class Serpia(ImageFilter):

    def apply(self, image_info: dict) -> Image:
        image = image_info["image_file"]
        draw = image_info["image_draw"]
        width, height = image_info["image_width"], image_info["image_height"]
        pix = image_info["image_pix"]
        depth = int(input('depth:'))
        for i in range(width):
            for j in range(height):  # підрахунок середнього значення кольорової гами - перетворення з коефіціентом
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a + b + c) // 3
                a = S + depth * 2
                b = S + depth
                c = S
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))
        return image


class ImageProcessor:
    """main code"""

    def __init__(self, image_read: ImageRead, image_saver: ImageSaver):
        self.image_read = image_read
        self.image_saver = image_saver

    def process(self, file_name_start: str, file_name_stop: str, image_filter: ImageFilter):
        image_info = self.image_read.image_read(file_name_start)
        print("Original picture")
        self.image_saver.show(image_info["image_file"])
        print("Changing picture")
        processed_image = image_filter.apply(image_info)
        self.image_saver.show(processed_image)
        self.image_saver.save(processed_image, file_name_stop)


