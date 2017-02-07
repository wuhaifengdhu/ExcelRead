#!/usr/bin/python
# -*- coding: utf-8 -*-
import pickle
import os
from lib.reader import Reader


def store_data(data, store_file):
    file_handler = open(store_file, 'wb')
    pickle.dump(data, file_handler)
    file_handler.close()


def load_data(store_file):
    file_handler = open(store_file, 'rb')
    data = pickle.load(file_handler)
    file_handler.close()
    return data


def convert_and_store(file_name, store_file):
    reader = Reader(file_name)
    store = []
    for record in reader.read_records():
        store.append(record)
    print "Stored %i records into %s" % (len(store), store_file)
    store_data(store, store_file)


if __name__ == '__main__':
    excel_file_path = os.path.join(os.getcwd(), 'resource', '01.xls')
    store_file_path = os.path.join(os.getcwd(), 'output', 'excel.dat')
    # Test convert excel and store object
    convert_and_store(excel_file_path, store_file_path)

    # Test read data from store file
    data = load_data(store_file_path)
    print data[0]
