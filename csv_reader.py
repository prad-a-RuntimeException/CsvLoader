import codecs

from collections import Counter

"""
 Generic CSV reader, Possible introspection to infer the delimiter
"""

default_encoding = 'ISO-8859-1'


def read_file(csv_file_name, delimiter=None):
    """
    :param csv_file_name:
    :param delimiter: Optional, code will try to infer, but provide when available.
    :return:
    """
    if delimiter is None:
        with codecs.open(csv_file_name, 'r', default_encoding) as csv_file:
            first_line = next(csv_file)
            delimiter = __get_delimiter(first_line)
    file = codecs.open(csv_file_name, 'r', default_encoding)
    elements = (line.split(delimiter) for line in file)
    return elements


def __get_delimiter(first_line):
    val = [nc for nc in first_line if not (nc.isalpha() or nc.isnumeric())]
    most_common, num_most_common = Counter(val).most_common(1)[0]
    return most_common
