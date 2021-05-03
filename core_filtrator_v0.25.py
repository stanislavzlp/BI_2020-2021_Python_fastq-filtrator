from argument_reader import read_input
from shutil import copyfile
from keep_filtered_sort import sort_by_len_GC_keep_filtered
from keep_filtered_sort import sort_only_len_keep_filtered
from keep_filtered_sort import sort_only_GC_keep_filtered
from trash_filtered_sort import sort_by_len_GC_trash_filtered
from trash_filtered_sort import sort_only_GC_trash_filtered
from trash_filtered_sort import sort_only_len_trash_filtered

OVERWRITE_WARNING = "\t\t\t\t!WARNING!\nЕсли вы указали в качестве output_base_name\
имя уже существующего файла, он будет перезаписан!"


def main_sorter(min_len, keep_filtered, min_GC,
                max_GC, output_base_name, file_name):

    print("Минимальная длина прочтений:", min_len)
    print("Нижний порог процентного соотношения GC:", min_GC)
    print("Верхний порог процентного соотношения GC:", max_GC)
    print("Файлы будут сохранены под следующим именем:", output_base_name)

    if keep_filtered:
        print("Отфильтрованные значения будут сохранены в отдельный файл")
        sort_and_keep_filtered(min_len, min_GC,
                               max_GC, output_base_name, file_name)
    elif not keep_filtered:
        print("Отфильтрованные значения не будут сохранены в отдельный файл")
        sort_and_trash_filtered(min_len, min_GC,
                                max_GC, output_base_name, file_name)


def sort_and_keep_filtered(min_len, min_GC, max_GC,
                           output_base_name, file_name):

    print(OVERWRITE_WARNING)

    if min_len == 0 and min_GC == 0 and max_GC == 0:
        copy_fastq(output_base_name, file_name)
    elif min_len == 0:
        sort_only_GC_keep_filtered(min_GC, max_GC,
                                   output_base_name, file_name)
    elif min_len > 0:
        if min_GC == 0 and max_GC == 100:
            sort_only_len_keep_filtered(min_len,
                                        output_base_name, file_name)
        else:
            sort_by_len_GC_keep_filtered(min_len, min_GC, max_GC,
                                         output_base_name, file_name)


def sort_and_trash_filtered(min_len, min_GC, max_GC,
                            output_base_name, file_name):

    print(OVERWRITE_WARNING)

    if min_len == 0 and min_GC == 0 and max_GC == 0:
        copy_fastq(output_base_name, file_name)
    elif min_len == 0:
        sort_only_GC_trash_filtered(min_GC, max_GC,
                                    output_base_name, file_name)
    elif min_len > 0:
        if min_GC == 0 and max_GC == 100:
            sort_only_len_trash_filtered(min_len,
                                         output_base_name, file_name)
        else:
            sort_by_len_GC_trash_filtered(min_len, min_GC, max_GC,
                                          output_base_name, file_name)


def copy_fastq(output_base_name, file_name):
    print('Filtration arguments not found. Output file is equal to\
 non filtrated file')
    original = file_name
    target = '{}_output.fastq'.format(output_base_name)
    copyfile(original, target)


if __name__ == '__main__':
    (min_len, keep_filtered, min_GC,
     max_GC, output_base_name, file_name) = read_input()

    main_sorter(min_len, keep_filtered, min_GC,
                max_GC, output_base_name, file_name)
