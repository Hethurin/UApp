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

        if not self.error_list:
            self.__validate_documents_correspondence(user_input)

        return self.error_list

    def __validate_passport(self, passport):
        if not passport:
            self.error_list.append("[Discrepancy] You must have passport!")

        if self.current_date > datetime.strptime(passport.expdate, '%d %m %Y %I:%M%p').date():
            self.error_list.append("[Discrepancy] Your can't use expired passport!")

        if ulibrary.cities[passport.country].find(passport.isscity) < 0:
            self.error_list.append("[Discrepancy] Issue city does not exist!")

    def __validate_pass(self, enpass):
        if not enpass:
            self.error_list.append("[Discrepancy] You must have pass!")

        if self.current_date > datetime.strptime(enpass.expires, '%d %m %Y %I:%M%p').date():
            self.error_list.append("[Discrepancy] Your can't use expired pass!")

    def __validate_work_visa(self, work_visa):
        if not work_visa:
            return

        if self.current_date > datetime.strptime(work_visa.expires, '%d %m %Y %I:%M%p').date():
            self.error_list.append("[Discrepancy] Your can't use expired work visa!")

    def __validate_documents_correspondence(self, user_input):
        self.__validate_passport_vs_pass(user_input.passport, user_input.enpass)
        self.__validate_pass_vs_work_visa(user_input.enpass, user_input.work_visa)
        self.__validate_pass_vs_record(user_input.enpass, user_input.record)
        self.__validate_work_visa_vs_record(user_input.work_visa, user_input.record)

    def __validate_passport_vs_pass(self, passport, enpass):
        if not passport.name == enpass.name:
            self.error_list.append("[Discrepancy] Passport and pass names do not match!")

        if not passport.gender == enpass.gender:
            self.error_list.append("[Discrepancy] Gender in passport and gender in pass do not match!")

        if not passport.serial == enpass.serial:
            self.error_list.append("Discrepancy] Passport serial # doesnt' match serial on pass!")

    def __validate_pass_vs_work_visa(self, enpass, work_visa):
        if not enpass.name == work_visa.name:
            self.error_list.append("[Discrepancy] Pass and work visa names do not match!")

        if not enpass.duration == work_visa.duration:
            self.error_list.append("[Discrepancy] Pass duration doesn't match work visa duration!")

    def __validate_pass_vs_record(self, enpass, record):
        if not enpass.duration == record.duration:
            self.error_list.append("[Discrepancy] Pass duration doesn't match what you've said!")

        if not enpass.purpose == record.purpose:
            self.error_list.append("[Discrepancy] Pass purpose doesn't match what you've said!")

    def __validate_work_visa_vs_record(self, work_visa, record):
        if (record.purpose == "Work") and (not work_visa):
            self.error_list.append("[Discrepancy] You can't work without work visa!")

        if not work_visa.duration == record.duration:
            self.error_list.append("[Discrepancy] Work visa duration doesn't match what you've said!")
