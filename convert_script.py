#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pandas
from lib.reader import Reader


def write_records_to_excel(excel_writer, dic_data, sheet_name):
    data_frame = pandas.DataFrame(dic_data)
    data_frame.to_excel(excel_writer, sheet_name=sheet_name)


def get_excel_data_from_records(record_iterator):
    # Step 1, init data
    basic_data = {'  url': [], ' name':[], 'company':[]}
    skill_data = {' url': []}
    for i in range(30):   # most record 30 skills
        skill_data['skills_%02i' % i] = []
    education_data = {' url': []}
    for i in range(10):   # most record 10 skills
        education_data['educations_%02i' % i] = []
    work_data = {' url': []}
    for i in range(15):   # most record 10 skills
        work_data['works_%02i' % i] = []

    # Step 2, convert data from records
    for record in record_iterator:
        basic_data['  url'].append(record.url)
        basic_data[' name'].append(record.name)
        basic_data['company'].append(record.company)
        for i in range(30):
            skill_data['skills_%02i' % i].append('' if i >= len(record.skills) else record.skills[i])
        for i in range(10):
            education_data['educations_%02i' % i].append('' if i >= len(record.educations) else record.educations[i])
        for i in range(15):
            work_data['works_%02i' % i].append('' if i >= len(record.works) else record.works[i])
    skill_data[' url'].extend(basic_data['  url'])
    education_data[' url'].extend(basic_data['  url'])
    work_data[' url'].extend(basic_data['  url'])

    # Step 3, return data
    return basic_data, skill_data, education_data, work_data


if __name__ == '__main__':
    # step 1, init parameters
    excel_file_path = os.path.join(os.getcwd(), 'resource', '01.xls')
    out_put_excel = os.path.join(os.getcwd(), 'output', 'result.xls')

    # step 2, read data from origin excel and convert to data
    records = Reader(excel_file_path).read_records()
    basic, skill, education, work = get_excel_data_from_records(records)

    # step 3, write data to output excel
    writer = pandas.ExcelWriter(out_put_excel, engine='xlsxwriter')
    write_records_to_excel(writer, basic, "basic")
    write_records_to_excel(writer, skill, "skills")
    write_records_to_excel(writer, education, 'educations')
    write_records_to_excel(writer, work, 'works')
    writer.close()





