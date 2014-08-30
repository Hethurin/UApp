#!/usr/bin/python3.4
import ulibrary


class UserInput(object):

    def __init__(self):
        pass

    def add_passport(self, passport):
        self.passport = ulibrary.UPassport(passport.country, passport.name, passport.gender,
                passport.isscity, passport.expdate, passport.serial)

    def add_pass(self, enpass):
        self.enpass = ulibrary.UPass(enpass.name, enpass.gender, enpass.purpose,
                enpass.duraton, enpass.serial, enpass.expires)

    def add_work_visa(self, work_visa):
        self.work_visa = ulibrary.UWorkVisa(work_visa.name, work_visa.proff,
                work_visa.duration, work_visa.expires)

    def add_record(self, record):
        self.record = ulibrary.URecord(record.purpose, record.duration)
