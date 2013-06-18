lidar-mashup
============

LIDAR data mash-up.

## description

Takes 2 .xyz files as argument --file1 and –file2, and eliminates `stepsize` points from each of them, swapping them after each elimination `iter` iterations.

The files will be 'embedded' into each other fully if the product of `iter` and `stepsize` is roughly equal to the size of the biggest file of two. For example, if the biggest file is 1.6Gb, these params will make a full mash-up:
--stepsize=1680000
--iterations=10

If it is less, only a section of both files close to the "black hole" will be produced. Alternatively, using the same file for both `file1` and `file2` parameters will extract a certain section from this file.

Quick and dirty, written in one hour, and can currently process .xyz files only. But even in its current minimal state it gives pretty interesting results, “embedding” one image into another.

### call example:
`python lidarmash.py -i 50 -s 1500000 -a /path/to/fileA.xyz -b /path/to/fileB.xyz /path/to/result_file.xyz`

For more help, type:
`$ python lidarmash.py -h`

### credits

For SESMI program at the University of California in San Diego, CA.
Written by Denis Kolokol, belongs to anyone in the Universe.