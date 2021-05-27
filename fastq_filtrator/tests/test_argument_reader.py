from fastq_filtrator.argument_reader import read_input


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
    import sys
    sys.argv = ['--gc_bounds', '45', 'test.fastq']
    (min_len, keep_filtered, min_GC, max_GC,
     output_base_name, file_name) = read_input()
    assert min_GC == 45

    sys.argv = ['--gc_bounds', '55', 'test.fastq']
    (min_len, keep_filtered, min_GC, max_GC,
     output_base_name, file_name) = read_input()
    assert min_GC == 55

    sys.argv = ['--gc_bounds', '10', 'test.fastq']
    (min_len, keep_filtered, min_GC, max_GC,
     output_base_name, file_name) = read_input()
    assert min_GC == 10


def test_max_GC_read_input():
    import sys
    sys.argv = ['--gc_bounds', '0', '75', 'test.fastq']
    (min_len, keep_filtered, min_GC, max_GC,
     output_base_name, file_name) = read_input()
    assert max_GC == 75

    sys.argv = ['--gc_bounds', '0', '15', 'test.fastq']
    (min_len, keep_filtered, min_GC, max_GC,
     output_base_name, file_name) = read_input()
    assert max_GC == 15

    sys.argv = ['--gc_bounds', '0', '95', 'test.fastq']
    (min_len, keep_filtered, min_GC, max_GC,
     output_base_name, file_name) = read_input()
    assert max_GC == 95


def test_GC_bounds_read_input():
    import sys
    sys.argv = ['--gc_bounds', '10', '75', 'test.fastq']
    (min_len, keep_filtered, min_GC, max_GC,
     output_base_name, file_name) = read_input()
    assert max_GC == 75
    assert min_GC == 10


def test_output_base_name_read_input():
    import sys
    sys.argv = ['--gc_bounds', '10', '75', '--output_base_name', 'name_test',
                'test.fastq']
    (min_len, keep_filtered, min_GC, max_GC,
     output_base_name, file_name) = read_input()
    assert max_GC == 75
    assert min_GC == 10
    assert output_base_name == 'name_test'


def test_min_len_read_input():
    import sys
    sys.argv = ['--min_length', '50',  'test.fastq']
    (min_len, keep_filtered, min_GC, max_GC,
     output_base_name, file_name) = read_input()
    assert min_len == 50


def test_file_name_read_input():
    import sys
    sys.argv = ['--min_length', '50',  'test.fastq']
    (min_len, keep_filtered, min_GC, max_GC,
     output_base_name, file_name) = read_input()
    assert file_name == 'test.fastq'
