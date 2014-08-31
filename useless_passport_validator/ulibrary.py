#!/usr/bin/python3.4
from collections import namedtuple


"""Document constants"""
countries = ["Mordor", "Gondor", "Lorien", "Shire"]
genders = ["Male", "Female"]
cities = {
    'Mordor': 'Minas Morgul,Barad Dur',
    'Gondor': 'Minas Tirith,Isengard,Osgiliath',
    'Lorien': 'Lorien',
    'Shire': 'Hobbiton,Waymeet,Frogmorton,Tuckborough'
    }
purpose = ["Visit", "Transit", "Work", "Immigrate"]

"""Store user input here"""
UPassport = namedtuple("UPassport", "country name gender isscity expdate serial")
UPass = namedtuple("UPass", "name gender purpose duration serial expires")
UWorkVisa = namedtuple("UWorkVisa", "name proff duration expires")
URecord = namedtuple("URecord", "purpose duration")
