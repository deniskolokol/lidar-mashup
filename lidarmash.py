#!/usr/bin/env python

"""
LIDAR data mashup.

Takes 2 .xyz files as argument --file1 and --file2,
and eliminates <stepsize> points from each of them,
swapping them after each elimination <iter> iterations.
"""

from optparse import OptionParser

# Constants - defaults.
DEFAULT_OPTS = {
    'iterations': 30,
    'stepsize': 1000000
    }

def main(opts, args):
    """
    Processes data, throws errors, reports on the results.
    """
    # Process options.
    try:
        result_file = args[0]
    except IndexError as e:
        print "You should specify result file!"
        return

    # Process options.
    try:
        stepsize = int(opts.stepsize)
    except:
        print "Wrong stepsize!"
        return
    try:
        iterations = int(opts.iterations)
    except:
        print "Wrong number of iterations!"
        return

    # Put filenames and fileobjects to the list.
    fnames = [opts.file1, opts.file2]
    files = []
    for fname in fnames:
        try:
            files.append(open(fname, 'rb'))
        except IOError:
            print "Cannot open file %s" % fname
            return

    # Initial values.
    step = 0
    lines = []
    fileindex = 0
    count = 0

    while count < iterations:
        try:
            lines.extend(
                files[fileindex].readline() for i in xrange(step, step+stepsize)
                )
        except Exception as e:
            print e
        else:
            step += stepsize
            fileindex = 0 if fileindex == 1 else 1

        print 'read points from %s:\tfrom %d to %d' % (
            fnames[fileindex],
            step,
            step + stepsize)

        count += 1

    print "Saving the file %s (may take few minutes depening on the amount of data)" % result_file
    fw = open(result_file, 'w')
    fw.writelines(lines)
    fw.close()
    print "Done"

if __name__ == '__main__':
    """
    Process command line options, start the process.
    """
    cmdparser = OptionParser(usage="usage: python %prog [Options] result_file.xyz")
    cmdparser.add_option('-i', '--iter',
                         action='store', dest='iterations',
                         default=DEFAULT_OPTS['iterations'],
                         help= 'Number of iterations, default %s' %\
        DEFAULT_OPTS['iterations'])
    cmdparser.add_option('-s', '--stepsize',
                         action='store', dest='stepsize',
                         default=DEFAULT_OPTS['stepsize'],
                         help='Step size, default %s' %\
        DEFAULT_OPTS['stepsize'])
    cmdparser.add_option('-a', '--file1',
                         action='store', dest='file1',
                         help='File A')
    cmdparser.add_option('-b', '--file2',
                         action='store', dest='file2',
                         help='File B')

    opts, args = cmdparser.parse_args()
    main(opts, args)
