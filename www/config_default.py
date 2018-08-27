#!/usr/bin/env/ python
# _*_ coding:utf-8 _*_

'''
Default configurations.
'''

__author__ = 'Jim Yang'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '1234',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}