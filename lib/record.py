#!/usr/bin/python
# -*- coding: utf-8 -*-
import unicodedata


class Record(object):
    def __init__(self, raw_list):
        self.url = Record._pretreatment_data(raw_list[1])
        self.name = self._build_name(raw_list[2])
        self.skills = self._build_skills(raw_list[3])
        self.company = raw_list[4]
        self.educations = self._build_educations(raw_list[5])
        self.works = self._build_works(raw_list[6])

    @staticmethod
    def _build_name(raw_name):
        # Remove ph.d, M.A. etc for most case, in little case would remove good things
        return raw_name.split(',')[0]

    @staticmethod
    def _build_skills(raw_skills):
        raw_skills = Record._pretreatment_data(raw_skills)
        return raw_skills.split('///')

    @staticmethod
    def _build_educations(raw_educations):
        raw_educations = Record._pretreatment_data(raw_educations)
        educations = []
        for education in raw_educations.split('///'):
            if '|' not in education:
                continue
            columns = education.split('|')
            if ',' in columns[1]:
                columns.insert(1, columns[1].split(',')[0])
                columns[2] = ''.join(columns[2].split(',')[1:]).strip()
            else:
                columns.insert(1, '')
            educations.append(columns)
        return educations

    @staticmethod
    def _build_works(raw_works):
        raw_works = Record._pretreatment_data(raw_works)
        return [work.split('|') for work in raw_works.split('///')]

    @staticmethod
    def _pretreatment_data(raw):
        try:
            # Fixed problem happened when raw is a float type data
            data = str(raw).strip()
        except UnicodeEncodeError:
            # Deal with condition which raw have unicode characters
            data = raw.strip().replace(u'\u2013', '-')  # translate unicode characters
            data = unicodedata.normalize('NFKD', data).encode('ascii','ignore')
        return data

    def __repr__(self):
        return " url = %s\n name = %s\n skills = %s \n company = %s\n education = %s\n " \
               "works= %s" % (self.url, self.name, self.skills, self.company, self.educations, self.works)








