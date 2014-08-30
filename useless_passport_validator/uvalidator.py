#!/usr/bin/python3.4
import ulibrary
from ulibrary import UPassport
from ulibrary import UPass
from ulibrary import UWorkVisa
from ulibrary import URecord
from datetime import date
from datetime import datetime


class UserInput(object):

    def __init__(self):
        pass

    def add_passport(self, passport):
        self.passport = UPassport(passport.country, passport.name, passport.gender,
                passport.isscity, passport.expdate, passport.serial)

    def add_pass(self, enpass):
        self.enpass = UPass(enpass.name, enpass.gender, enpass.purpose,
                enpass.duraton, enpass.serial, enpass.expires)

    def add_work_visa(self, work_visa):
        self.work_visa = UWorkVisa(work_visa.name, work_visa.proff,
                work_visa.duration, work_visa.expires)

    def add_record(self, record):
        self.record = URecord(record.purpose, record.duration)


class UValidator(object):

    def __init__(self):
        self.error_list = []
        self.current_date = date.today()

    def validate_documents(self, user_input):
        self.__validate_passport(user_input.passport)
        self.__validate_pass(user_input.enpass)
        self.__validate_work_visa(user_input.work_visa)
        return self.error_list

    def __validate_passport(self, passport_values):
        if not passport_values:
            self.error_list.append("[Discrepancy] You must have passport!")

        if self.current_date > datetime.strptime(passport_values.expdate, '%d %m %Y %I:%M%p').date():
            self.error_list.append("[Discrepancy] Your can't use expired passport!")

        if ulibrary.cities[passport_values.country].find(passport_values.isscity) < 0:
            self.error_list.append("[Discrepancy] Issue city does not exist!")

    def __validate_pass(self, pass_values):
        if not pass_values:
            self.error_list.append("[Discrepancy] You must have pass!")

        if self.current_date > datetime.strptime(pass_values.expires, '%d %m %Y %I:%M%p').date():
            self.error_list.append("[Discrepancy] Your can't use expired pass!")

    def __validate_work_visa(self, work_visa_values):
        if not work_visa_values:
            return

        if self.current_date > datetime.strptime(work_visa_values.expires, '%d %m %Y %I:%M%p').date():
            self.error_list.append("[Discrepancy] Your can't use expired work visa!")
