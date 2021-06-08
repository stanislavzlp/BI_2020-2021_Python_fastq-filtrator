# BI_2020-2021_Python_fastq-filter

Fastq-filter project is a program for filtration of fastq files.

The current version of the filter has two main functions:

`filtration by length` - reads will be filtrated by the given length 

`filtration by GC content` - reads will be filtrated by the given GC content percent


### Arguments

`--min_length` - takes a minimal length of the sequence. Sequences with less length will be filtrated away

`--gc_bounds`  - takes two arguments: upper and lower border of GC content in sequence.  
For example: `--gc_bounds 20 70`. Sequences with GC content higher or lower
than bounds will be rejected. 

`--keep_filtered` - if this flag used rejected sequences will be also saved to the file. 

`--output_base_name` - name for output file or files. Standart output name `base_name`


### Visualization

Visualization is not available in the current version.
