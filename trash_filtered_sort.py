import sys

NO_FILE_ERROR = "\t\t\t\t<<<!!!ERROR!!!>>>\nУказанный вами файл не обнаружен.\
 Проверьте его наличие или правильность написания названия файла."


def sort_only_GC_trash_filtered(min_GC, max_GC, output_base_name, file_name):
    passed_file = open("{}_passed.fastq".format(output_base_name), "w")

    try:
        with open(file_name, "r") as file:
            lines = []
            n = 0
            for line in file:
                lines.append(line.strip())
                n += 1
                if n == 4:
                    number_GC = lines[1].count('C') + lines[1].count('G')
                    percent = number_GC / len(lines[1])
                    if max_GC / 100 > percent > min_GC / 100:
                        for i in range(len(lines)):
                            passed_file.write(lines[i])
                            passed_file.write("\n")
                    lines = []
                    n = 0
    except FileNotFoundError:
        print(NO_FILE_ERROR)
        sys.exit()

    passed_file.close()


def sort_only_len_trash_filtered(min_len, output_base_name, file_name):
    passed_file = open("{}_passed.fastq".format(output_base_name), "w")

    try:
        with open(file_name, "r") as file:
            lines = []
            n = 0
            for line in file:
                lines.append(line.strip())
                n += 1
                if n == 4:
                    if len(lines[1]) > min_len:
                        for i in range(len(lines)):
                            passed_file.write(lines[i])
                            passed_file.write("\n")
                lines = []
                n = 0
    except FileNotFoundError:
        print(NO_FILE_ERROR)
        sys.exit()

    passed_file.close()


def sort_by_len_GC_trash_filtered(min_len, min_GC, max_GC,
                                  output_base_name, file_name):

    passed_file = open("{}_passed.fastq".format(output_base_name), "w")

    try:
        with open(file_name, "r") as file:
            lines = []
            n = 0
            for line in file:
                lines.append(line.strip())
                n += 1
                if n == 4:
                    if len(lines[1]) > min_len:
                        number_GC = lines[1].count('C') + lines[1].count('G')
                        percent = number_GC / len(lines[1])
                        if max_GC / 100 > percent > min_GC / 100:
                            for i in range(len(lines)):
                                passed_file.write(lines[i])
                                passed_file.write("\n")
                    lines = []
                    n = 0
    except FileNotFoundError:
        print(NO_FILE_ERROR)
        sys.exit()

    passed_file.close()
