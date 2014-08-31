#!/usr/bin/python3.4
from collections import namedtuple


def init():
    """Document constants"""
    global countries
    countries = ["Mordor", "Gondor", "Lorien", "Shire"]
    global genders
    genders = ["Male", "Female"]
    global cities
    cities = {
        'Mordor': 'Minas Morgul,Barad Dur',
        'Gondor': 'Minas Tirith,Isengard,Osgiliath',
        'Lorien': 'Lorien',
        'Shire': 'Hobbiton,Waymeet,Frogmorton,Tuckborough'
    }
    global purpose
    purpose = ["Visit", "Transit", "Work", "Immigrate"]

    """Store user input here"""
    global UPassport
    UPassport = namedtuple("UPassport", "country name gender isscity expdate serial")
    global UPass
    UPass = namedtuple("UPass", "name gender purpose duration serial expires")
    global UWorkVisa
    UWorkVisa = namedtuple("UWorkVisa", "name proff duration expires")
    global URecord
    URecord = namedtuple("URecord", "purpose duration")
