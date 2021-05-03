from args import read_input
import sys


def main():
    min_len, keep_filtered, min_GC, max_GC, output_base_name, file_name = read_input()
    Passed = 0
    Failed = 0

    def sort_by_GC(read_GC, min_GC_sort=0, max_GC_sort=100):
        nonlocal Passed
        nonlocal Failed
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
        nonlocal Failed
        if len(read[1]) >= min_len:
            sort_by_GC(read, min_GC, max_GC)
        else:
            Failed += 1
            if keep_filtered:
                for i in range(len(read)):
                    failed_file.write(read[i])
                    failed_file.write("\n")

    passed_file = open("{}_passed.fastq".format(output_base_name), "w")
    if keep_filtered:
        failed_file = open("{}_failed.fastq".format(output_base_name), "w")
    print(
         "\t\t\t\t!ПРЕДУПРЕЖДЕНИЕ!\nЕсли вы указали в качестве output_base_name\
 имя уже существующего файла, он будет перезаписан!")

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
            "\nУказанный вами файл не обнаружен.\
 Проверьте его наличие или правильность написания названия файла.")
        sys.exit()

    print("Passed:", Passed)
    print("Failed:", Failed)
    passed_file.close()
    if keep_filtered:
        failed_file.close()


if __name__ == '__main__':
    main()
