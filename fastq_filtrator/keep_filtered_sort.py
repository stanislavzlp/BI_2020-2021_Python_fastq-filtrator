import sys

NO_FILE_ERROR = "\t\t\t\t<<<!!!ERROR!!!>>>\nУказанный вами файл не обнаружен.\
 Проверьте его наличие или правильность написания названия файла."


def sort_only_GC_keep_filtered(min_GC: int, max_GC: int,
                               output_base_name: str, file_name: str):

    passed_file = open("{}_passed.fastq".format(output_base_name), "w")
    failed_file = open("{}_failed.fastq".format(output_base_name), "w")

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
                    else:
                        for i in range(len(lines)):
                            failed_file.write(lines[i])
                            failed_file.write("\n")
                    lines = []
                    n = 0
    except FileNotFoundError:
        print(NO_FILE_ERROR)
        sys.exit()

    passed_file.close()
    failed_file.close()


def sort_only_len_keep_filtered(min_len: int, output_base_name: str,
                                file_name: str):

    passed_file = open("{}_passed.fastq".format(output_base_name), "w")
    failed_file = open("{}_failed.fastq".format(output_base_name), "w")

    try:
        with open(file_name, "r") as file:
            lines = []
            n = 0
            for line in file:
                lines.append(line.strip())
                n += 1
                if n == 4:
                    if len(lines[1]) >= min_len:
                        for i in range(len(lines)):
                            passed_file.write(lines[i])
                            passed_file.write("\n")
                    else:
                        for i in range(len(lines)):
                            failed_file.write(lines[i])
                            failed_file.write("\n")
                    lines = []
                    n = 0
    except FileNotFoundError:
        print(NO_FILE_ERROR)
        sys.exit()

    passed_file.close()
    failed_file.close()


def sort_by_len_GC_keep_filtered(min_len: int, min_GC: int, max_GC: int,
                                 output_base_name: str, file_name: str):

    passed_file = open("{}_passed.fastq".format(output_base_name), "w")
    failed_file = open("{}_failed.fastq".format(output_base_name), "w")

    try:
        with open(file_name, "r") as file:
            lines = []
            n = 0
            for line in file:
                lines.append(line.strip())
                n += 1
                if n == 4:
                    if len(lines[1]) >= min_len:
                        number_GC = lines[1].count('C') + lines[1].count('G')
                        percent = number_GC / len(lines[1])
                        if max_GC / 100 > percent > min_GC / 100:
                            for i in range(len(lines)):
                                passed_file.write(lines[i])
                                passed_file.write("\n")
                        else:
                            for i in range(len(lines)):
                                failed_file.write(lines[i])
                                failed_file.write("\n")
                    else:
                        for i in range(len(lines)):
                            failed_file.write(lines[i])
                            failed_file.write("\n")
                    lines = []
                    n = 0
    except FileNotFoundError:
        print(NO_FILE_ERROR)
        sys.exit()

    passed_file.close()
    failed_file.close()
