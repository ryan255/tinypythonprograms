import sys
import re
import collections


def count_space(path):
    number_counts = 0
    space_counts = 0
    number_list = []

    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            space_split_list = line.split(' ')
            space_counts += len(space_split_list) - 1
            for word in space_split_list:
                    if word.isdigit():
                        number_list.append(word)
            number_counts = len(number_list)

    return space_counts

def count_word(path):
    result = {}
    with open(path) as fileread:
        alltext = fileread.read()

        alltext = alltext.lower()

        alltext = re.sub("\"|,|\.", "", alltext)

        for word in alltext.split():
            if word not in result:
                result[word] = 0
            result[word] += 1

        return result


def sort_by_count(d):

    d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))
    return d


if __name__ == '__main__':
    try:
        filename = 'read.txt'

        dword = count_word(filename)
        dword = sort_by_count(dword)

        countspace = count_space(filename)
        print "space_counts", countspace
        count_word(filename)
        for key,value in dword.items():
            print key + ":%d" % value

    except IOError:
        print 'cannot open file %s for read' % filename
