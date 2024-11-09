'''

Виконав:Stetrsenko Anna

Homework_5
З використанням механізмів модульного та функціонального програмування реалізувати програмну архітектуру проекту python
у відповідності до структурної схеми завдання.
Порядок інформаційного обміну – на самостійне рішення.
Принципи внутрішньої організації модулів – на самостійне рішення.
До модулів та функцій застосувати архітектурну побудову з дотриманням вимог РЕР.
Передбачити документування складових проекту.

'''

import LessonHM5_1
import LessonHM5_2 as l
from LessonHM5_3 import FizzBuzz
import Im_PIL


if __name__ == "__main__":

    LessonHM5_1.CV_csv(name='Stetsenko Anna', education='University', skills=['Python', 'SQL'], adress='Kyiv', email='asdf@sdf')

    radius = 10
    print('Area_of_circle', l.Area_of_circle(radius=radius))

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
    print(FizzBuzz(numbers))

    file_name = "Picture.jpg"
    file_name_stop = "Picture_stop.jpg"

    processor = Im_PIL.ImageProcessor(Im_PIL.ImageRead(), Im_PIL.ImageSaver())

    gray_filter = Im_PIL.ShadesOfGrayFilter()
    processor.process(file_name, file_name_stop, gray_filter)

    serpia_filter = Im_PIL.Serpia()
    processor.process(file_name, file_name_stop, serpia_filter)





