#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas
import os
from record import Record


class Reader(object):
    def __init__(self, file_name, sheet_number=0):
        self._data_frame = pandas.read_excel(file_name, sheet_number)

    def read_records(self):
        for index, row in self._data_frame.iterrows():
            yield self._build_record(row)

    @staticmethod
    def _build_record(row):
        if len(row) == 7:
            return Record(row)
        elif len(row) > 7:
            return Record(row[:7])
        else:
            print "Format Error for row: %s" % str(row)


if __name__ == '__main__':
    parent_path = os.path.dirname(os.getcwd())
    # print parent_path
    file_path = os.path.join(parent_path, 'resource', '01.xls')
    # print file_path
    reader = Reader(file_path)
    record = reader.read_records().next()
    print record





