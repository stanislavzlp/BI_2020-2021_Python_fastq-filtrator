import sys


def read_input():

    if "--help" or 'h' or '-h' or '--h' in sys.argv:
        print('Добро пожаловать в скудный --help')
        print("--min_length - параметр минимальной длины\
 прочтения\
 \n--gc_bounds - параметр для верхней и нижней\
 границы GC состава. Пример: \"--gc_bounds 20 70\"\
 \n--output_base_name - имя для файла\
 с отфильтрованными прочтениями")
        sys.exit()

    if "--min_length" in sys.argv:
        min_len_index = sys.argv.index("--min_length")
        min_len = int(sys.argv[min_len_index + 1])
    else:
        min_len = 0

    if "--keep_filtered" in sys.argv:
        keep_filtered = True
    else:
        keep_filtered = False

    if "--gc_bounds" in sys.argv:
        GC_bounds_index = sys.argv.index("--gc_bounds")
        min_GC = int(sys.argv[GC_bounds_index + 1])
        try:
            max_GC = int(sys.argv[GC_bounds_index + 2])
        except ValueError or IndexError:
            max_GC = 100
    else:
        min_GC = 0
        max_GC = 100

    if "--output_base_name" in sys.argv:
        output_base_name_index = sys.argv.index("--output_base_name")
        output_base_name = sys.argv[output_base_name_index + 1]
    else:
        output_base_name = "base_name"

    if ".fastq" in sys.argv[len(sys.argv) - 1]:
        file_name = sys.argv[len(sys.argv) - 1]
        print("Начинается обработка вашего файла:", file_name)
    else:
        print(
            "\t\t\t\t<<<!!!ОШИБКА!!!>>>\nНе обнаружен файл формата\
             .fastq. Работа приложения прекращена. "
            "Для адекватной работы скрипта укажите файл формата\
             .fastq в качестве последнего аргумента")
        # Тут идёт просто проверка на наличие *.fastq в sys.argv.
        # Указанный файл может и не существовать. Дополнительная
        # проверка следует позже.
        sys.exit()
    return (min_len, keep_filtered, min_GC,
            max_GC, output_base_name, file_name)
