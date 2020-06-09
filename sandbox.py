# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Script for research and experiments                                                                               #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


import xlrd
import xlwt
from pprint import pprint


def get_xls_data():
    res = []
    sheet = xlrd.open_workbook('input.xlsx').sheet_by_index(0)
    for row in range(sheet.nrows):
        rw = sheet.row_values(row)
        try:
            n, nm, tl, tl_d, vs, vm, vb, mob, ct, etc, idiots = int(rw[0]), rw[1].split(', род. ')[0], rw[2], rw[3], \
                                                                rw[4], rw[5], rw[6], rw[7], rw[8], rw[9], rw[10]
            try:
                date = rw[1].split(', род. ')[1]
            except IndexError:
                date = ''
            res.append([n, nm, date, tl, tl_d, vs, vm, vb, mob, ct, etc, idiots])
        except ValueError:
            res.append(rw)
    return res


if __name__ == '__main__':
    xls_data = get_xls_data()
    for data in xls_data:
        print(data)