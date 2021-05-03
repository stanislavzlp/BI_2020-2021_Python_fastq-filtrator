from args import read_input


def test_keep_filtered_read_input():
    import sys
    sys.argv = ['--keep_filtered', 'test.fastq']
    (min_len, keep_filtered, min_GC, max_GC,
     output_base_name, file_name) = read_input()
    assert keep_filtered

    sys.argv = ['test.fastq']
    (min_len, keep_filtered, min_GC, max_GC,
     output_base_name, file_name) = read_input()
    assert not keep_filtered


def test_min_GC_read_input():
    pass


def test_max_GC_read_input():
    pass


def test_GC_bounds_read_input():
    pass


def test_output_base_name_read_input():
    pass


def test_min_len_read_input():
    pass


def test_file_name_read_input():
    pass