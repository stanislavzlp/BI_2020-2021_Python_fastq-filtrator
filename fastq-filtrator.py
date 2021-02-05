import sys
if "--min_length" in sys.argv:
    min_len_index = sys.argv.index("--min_length")
    min_len = int(sys.argv[min_len_index + 1])
    print("Минимальная длина прочтений:", min_len)
else:
    min_len = 0

if "--keep_filtered" in sys.argv:
    keep_filtered = True
    print("Отфильтрованные значения будут сохранены в отдельный файл")
else:
    keep_filtered = False
    print("Отфильтрованные значения не будут сохранены в отдельный файл")

if "--gc_bounds" in sys.argv:
    GC_bounds_index = sys.argv.index("--gc_bounds")
    min_GC = int(sys.argv[GC_bounds_index + 1])
    print("Нижний порог процентного соотношения GC:", min_GC)
    try:
        max_GC = int(sys.argv[GC_bounds_index + 2])
        print("Верхний порог процентного соотношения GC:", max_GC)
    except ValueError or IndexError:
        max_GC = 100
        print("Верхний порог процентного соотношения GC:", max_GC)
else:
    min_GC = 0
    max_GC = 100

if "--output_base_name" in sys.argv:
    output_base_name_index = sys.argv.index("--output_base_name")
    output_base_name = sys.argv[output_base_name_index + 1]
    print("Файлы будут сохранены под следующим именем:", output_base_name)
else:
    output_base_name = "base_name"
    print("Файлы будут сохранены под следующим именем:", output_base_name)

if ".fastq" in sys.argv[len(sys.argv) - 1]:
    file_name = sys.argv[len(sys.argv) - 1]
    print("Начинается обработка вашего файла:", file_name)
else:
    print(
        "\t\t\t\t<<<!!!ОШИБКА!!!>>>\nНе обнаружен файл формата .fastq. Работа приложения прекращена. "
        "Для адекватной работы скрипта укажите файл формата .fastq в качестве последнего аргумента")
    sys.exit()

Passed = 0
Failed = 0

passed_file = open("{}_passed.fastq".format(output_base_name), "w")
if keep_filtered:
    failed_file = open("{}_failed.fastq".format(output_base_name), "w")
print("\t\t\t\t!ПРЕДУПРЕЖДЕНИЕ!\nЕсли вы указали в качестве output_base_name имя уже существующего файла, он будет перезаписан!")

def sort_by_GC(read_GC, min_GC_sort=0, max_GC_sort=100):
    global Passed
    global Failed
    number_GC = 0
    for i in read_GC[1]:
        if i == "C" or i == "G":
            number_GC += 1
    percent = number_GC / len(read_GC[1])
    if max_GC_sort / 100 > percent > min_GC_sort / 100:
        Passed += 1
        for i in range(len(read_GC)):
            passed_file.write(read_GC[i])
            passed_file.write("\n")
    else:
        Failed += 1
        if keep_filtered:
            for i in range(len(read_GC)):
                failed_file.write(read_GC[i])
                failed_file.write("\n")

def sort_by_length(read):
    global Failed
    if len(read[1]) >= min_len:
        sort_by_GC(read, min_GC, max_GC)
    else:
        Failed += 1
try:
    with open(file_name, "r") as file:
        lines = []
        n = 0
        for line in file:
            lines.append(line.strip())
            n += 1
            if n == 4:
                sort_by_length(lines)
                lines = []
                n = 0
except FileNotFoundError:
    print(
        "\t\t\t\t<<<!!!ОШИБКА!!!>>>"
        "\nУказанный вами файл не обнаружен. Проверьте его наличие или правильность написания названия файла.")
    sys.exit()

print("Passed:", Passed)
print("Failed:", Failed)
passed_file.close()
if keep_filtered:
    failed_file.close()