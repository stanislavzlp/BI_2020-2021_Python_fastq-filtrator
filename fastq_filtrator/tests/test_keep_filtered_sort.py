from fastq_filtrator.keep_filtered_sort import sort_only_GC_keep_filtered
from fastq_filtrator.keep_filtered_sort import sort_only_len_keep_filtered
from fastq_filtrator.keep_filtered_sort import sort_by_len_GC_keep_filtered
import os


def test_sort_only_GC_keep_filtered():
    file_name = './test_data/test1.fastq'
    output_name_GC = 'only_GC_test'
    min_GC = 50
    max_GC = 100
    sort_only_GC_keep_filtered(min_GC=min_GC, max_GC=max_GC,
                               output_base_name=output_name_GC,
                               file_name=file_name)
    test_file_pass = open('{}_passed.fastq'.format(output_name_GC), 'r')
    check_file_pass = open('test_data/test_sort_only_GC_res_PASSED.fastq', 'r')
    test_file_fail = open('{}_failed.fastq'.format(output_name_GC), 'r')
    check_file_fail = open('test_data/test_sort_only_GC_res_FAILED.fastq', 'r')
    assert test_file_pass.read() == check_file_pass.read()
    assert test_file_fail.read() == check_file_fail.read()
    test_file_fail.close()
    test_file_pass.close()
    check_file_fail.close()
    check_file_pass.close()
    os.remove('{}_failed.fastq'.format(output_name_GC))
    os.remove('{}_passed.fastq'.format(output_name_GC))


def test_sort_only_len_keep_filtered():
    file_name = './test_data/test2.fastq'
    output_name_len = 'only_len_test'
    min_len = 5
    sort_only_len_keep_filtered(min_len=min_len,
                                output_base_name=output_name_len,
                                file_name=file_name)
    test_file_pass = open('{}_passed.fastq'.format(output_name_len), 'r')
    check_file_pass = open('test_data/test_sort_only_len_res_PASSED.fastq',
                           'r')
    test_file_fail = open('{}_failed.fastq'.format(output_name_len), 'r')
    check_file_fail = open('test_data/test_sort_only_len_res_FAILED.fastq',
                           'r')
    assert test_file_pass.read() == check_file_pass.read()
    assert test_file_fail.read() == check_file_fail.read()
    test_file_fail.close()
    test_file_pass.close()
    check_file_fail.close()
    check_file_pass.close()
    os.remove('{}_failed.fastq'.format(output_name_len))
    os.remove('{}_passed.fastq'.format(output_name_len))


def test_sort_by_len_GC_keep_filtered():
    file_name = './test_data/test3.fastq'
    output_name_GC = 'GC_len_test'
    min_len = 5
    min_GC = 50
    max_GC = 100
    sort_by_len_GC_keep_filtered(min_GC=min_GC, max_GC=max_GC,
                                 min_len=min_len,
                                 output_base_name=output_name_GC,
                                 file_name=file_name)
    test_file_pass = open('{}_passed.fastq'.format(output_name_GC), 'r')
    check_file_pass = open('test_data/test_sort_GC_len_res_PASSED.fastq', 'r')
    test_file_fail = open('{}_failed.fastq'.format(output_name_GC), 'r')
    check_file_fail = open('test_data/test_sort_GC_len_res_FAILED.fastq', 'r')
    assert test_file_pass.read() == check_file_pass.read()
    assert test_file_fail.read() == check_file_fail.read()
    test_file_fail.close()
    test_file_pass.close()
    check_file_fail.close()
    check_file_pass.close()
    os.remove('{}_failed.fastq'.format(output_name_GC))
    os.remove('{}_passed.fastq'.format(output_name_GC))
