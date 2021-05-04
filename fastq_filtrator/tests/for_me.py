from fastq_filtrator.keep_filtered_sort import sort_only_GC_keep_filtered


file_name = './test_data/test1.fastq'
output_name = 'only_GC_test'
min_GC = 50
max_GC = 100
sort_only_GC_keep_filtered(min_GC=min_GC, max_GC=max_GC,
                           output_base_name=output_name,
                           file_name=file_name)
