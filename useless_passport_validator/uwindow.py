#!/usr/bin/python3.4
import ulibrary
from gi.repository import Gtk


class UWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Useless passport validator")

        grid = Gtk.Grid()
        self.add(grid)

        """Passport column"""
        passport_country_label = Gtk.Label("Country")
        passport_name_label = Gtk.Label("Name")
        passport_gender_label = Gtk.Label("Gender")
        passport_isscity_label = Gtk.Label("Iss. City")
        passport_expdate_label = Gtk.Label("Exp. Date")
        passport_serial_label = Gtk.Label("Serial")

        no_passport = Gtk.CheckButton("No Passport")
        no_passport.set_active(False)

        passport_country_combo = Gtk.ComboBoxText()
        passport_country_combo.set_entry_text_column(0)
        for country in ulibrary.countries:
            passport_country_combo.append_text(country)

        passport_gender_combo = Gtk.ComboBoxText()
        passport_gender_combo.set_entry_text_column(0)
        for gender in ulibrary.genders:
            passport_gender_combo.append_text(gender)

        passport_name_entry = Gtk.Entry()
        passport_isscity_entry = Gtk.Entry()
        passport_expdate_entry = Gtk.Entry()
        passport_serial_entry = Gtk.Entry()

        grid.attach(no_passport, 0, 0, 2, 1)
        grid.attach(passport_country_label, 0, 1, 1, 1)
        grid.attach_next_to(passport_name_label, passport_country_label, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(passport_gender_label, passport_name_label, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(passport_isscity_label, passport_gender_label, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(passport_expdate_label, passport_isscity_label, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(passport_serial_label, passport_expdate_label, Gtk.PositionType.BOTTOM, 1, 1)

        grid.attach_next_to(passport_country_combo, passport_country_label, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(passport_name_entry, passport_name_label, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(passport_gender_combo, passport_gender_label, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(passport_isscity_entry, passport_isscity_label, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(passport_expdate_entry, passport_expdate_label, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(passport_serial_entry, passport_serial_label, Gtk.PositionType.RIGHT, 1, 1)

        """Pass column"""
        pass_name_label = Gtk.Label("Name")
        pass_gender_label = Gtk.Label("Gender")
        pass_purpose_label = Gtk.Label("Purpose")
        pass_duration_label = Gtk.Label("Duration")
        pass_serial_label = Gtk.Label("Serial")
        pass_expires_label = Gtk.Label("Expires")

        no_pass = Gtk.CheckButton("No entry pass")
        no_pass.set_active(False)

        pass_gender_combo = Gtk.ComboBoxText()
        pass_gender_combo.set_entry_text_column(0)
        for gender in ulibrary.genders:
            pass_gender_combo.append_text(gender)

        pass_purpose_combo = Gtk.ComboBoxText()
        pass_purpose_combo = Gtk.ComboBoxText()
        for purpose in ulibrary.purposes:
            pass_purpose_combo.append_text(purpose)

        pass_name_entry = Gtk.Entry()
        pass_duration_entry = Gtk.Entry()
        pass_serial_entry = Gtk.Entry()
        pass_expires_entry = Gtk.Entry()

        grid.attach_next_to(no_pass, no_passport, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(pass_name_label, passport_country_combo, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(pass_gender_label, passport_name_entry, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(pass_purpose_label, passport_gender_combo, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(pass_duration_label, passport_isscity_entry, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(pass_serial_label, passport_expdate_entry, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(pass_expires_label, passport_serial_entry, Gtk.PositionType.RIGHT, 1, 1)

        grid.attach_next_to(pass_name_entry, pass_name_label, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(pass_gender_combo, pass_gender_label, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(pass_purpose_combo, pass_purpose_label, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(pass_duration_entry, pass_duration_label, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(pass_serial_entry, pass_serial_label, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(pass_expires_entry, pass_expires_label, Gtk.PositionType.RIGHT, 1, 1)
