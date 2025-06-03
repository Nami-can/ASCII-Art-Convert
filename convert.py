
import time
import cv2
from pyfiglet import figlet_format
from ascii_text import menu, image_art






###################################################################
#   3 - Преобразовать ASCII-арт в текстовый формат
###################################################################

def text_ascii_art(text, asi):
    asi = figlet_format(text)
    print(text)














#############################################################
#              1 - Создать ASCII-арт из изображения
#############################################################

def image_terminal(image_path1):

    chars = " .'`^\",:;Il!i~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZwmqpdbkhao*#MW&8%B@$"
    coef = 255 / len(chars)
    image = cv2.imread(image_path1)
    if image is None:
        raise ValueError('Не удалось загрузить изображения')
    print('\n\t---Изображения загружено---')
    print('\n\t---Конвертируем изображения в черно-белое---')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
    print('\n\t---Конвертация завершена!---')
    height, width, channels = image.shape
    for x in range(0, height - 1, 18):
        s = ''
        for y in range(0, width - 1, 9):
            s += chars[len(chars) - int(gray_image[x, y] / coef) - 1]

        print(s)
        # print('-' * 50)
        # time.sleep(0.5)

# /home//PycharmProjects/PythonProject1/Text_file/img_ASCII



def image_file(image_path, file_path):
    chars = " .'`^\",:;Il!i~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZwmqpdbkhao*#MW&8%B@$"
    coef = 255 / len(chars)
    image = cv2.imread(image_path)

    height, width, channels = image.shape
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)

    with open(file_path, 'w') as file:
        for x in range(0, height - 1, 18):
            c = ''
            for y in range(0, width - 1, 9):
                c += chars[len(chars) - int(gray_image[x, y] / coef) - 1]
            file.write(c + '\n')



########################################################
#        2 - Создать ASCII-арт из видеофайла
#######################################################



def video_cmd(video_path):
    chars = " .'`^\",:;Il!i~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZwmqpdbkhao*#MW&8%B@$"
    coef = 255 / len(chars)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print('Ошибка, не удалось открыть видеофайл')
    print('---Видеофайл загружен---')



    # Чтения файла
    while True:
        ret, frame = cap.read()
        if not ret:
            print('---Конец видео---')
            break
        gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        height, width = gray_video.shape
        ascii_frame = ''

        for x in range(0, height - 1, 8):
            line = ''
            for y in range(0, width - 1, 4):
                pixel_valye = int(gray_video[x, y])
                index = min(int(pixel_valye / coef), len(chars) - 1)
                line += chars[index]
            ascii_frame += line + '\n'

        print('\n' * 100)

        print(ascii_frame)

        # time.sleep(0.01)
        # kass = cv2.waitKey(30) & 0xFF
        # if kass == ord('q'):
        #     print('\n---Выход по запросу---')
        #     break
        # elif kass == 'p':
        #     paused = not paused
        #     print('\n---Пауза---' if paused else '\n---Возобновлено---')
        time.sleep(0.01)

    cap.release()


#################################################
#                    МЕНЮ
#################################################

def main_menu():
    while True:
        print(menu)
        key = input('\tВведите действия (1-4): ').strip()
        if key == '1':
            while True:
                print(image_art)
                im = input('Введите действия: ').strip()
                print('\n\t---(b - вернуться назад)---')
                if im.lower() == 'b':
                    break

                if im == '1':
                    print('\n\t---Вы выбрали ASCII-арт в текстовый формат---')
                    while True:
                        image_path = input('Введите путь к изображению: ').strip()
                        if image_path.lower() == 'b':
                            break
                        file_path = input('Введите путь к txt файлу: ').strip()
                        if file_path.lower() == 'b':
                            continue

                        try:
                            image_file(image_path, file_path)
                            print('\n\t---Файл успешно сохранен---')
                            break
                        except Exception as e:
                            print(f'Ошибка: {e}')
                            continue

                elif im == '2':
                    print('\n\t---Вы выбрали  ASCII-арт из изображения в терминал---')
                    while True:
                        image_path1 = input('\n\n\tВведите путь к изображению: ').strip()
                        if image_path1 == 'b':
                            break
                        try:
                            image_terminal(image_path1)
                            print('---Изображения готово---')
                            break
                        except Exception as e:
                            print(f'Ошибка: {e}')
                            continue

        elif key == '2':
            while True:
                print('\n\t--Вы выбрали ASCII-арт из видеофайла-- ')
                print('\n\t---(b - вернуться назад)---')
                video_path = input('Введите путь к видео-файлу: ').strip()
                if video_path == 'b':
                    break
                try:
                    video_cmd(video_path)
                    print('---Видеофайл готов---')
                    break
                except Exception as e:
                            print(f'Ошибка: {e}')
                            continue

        elif key == '3':
            while True:
                print('\n\t---Вы выбрали ASCII-арт в текстовый формат---')
                print('\n\t---(b - вернуться назад)---')
                text = input('Введите текс: ').strip()
                asi = figlet_format(text)
                print(asi)
                if text.lower() == 'b':
                    break
                try:
                    text_ascii_art(text,asi)
                    print('---ASCII txt завершен---')

                except Exception as e:
                            print(f'Ошибка: {e}')
                            continue

        elif key == '4':
            print('\n\t---Выход из программы---')
            break


        else:
            print('\n\t---Неверный ввод, попробуй еще раз---')





main_menu()


