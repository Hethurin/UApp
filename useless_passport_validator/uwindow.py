#!/usr/bin/python3.4
import ulibrary
from gi.repository import Gtk


class UWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Useless passport validator")

        grid = Gtk.Grid()
        self.add(grid)

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
        passport_gender_combo.set_entry.text_column(0)
        for gender in ulibrary.genders:
            passport_gender_combo.append_text(gender)

        passport_name_entry = Gtk.Entry()
        passport_isscity_entry = Gtk.Entry()
        passport_expdate_entry = Gtk.Entry()
        passport_serial_entry = Gtk.Entry()

        grid.attach(no_passport, 0, 0, 2, 1)
        grid.attach(passport_country_label(0, 1, 1, 1)
        grid.attach_next_to(passport_name_label, passport_country_label, Gtk.Position.BOTTOM, 1, 1)
        grid.attach_next_to(passport_gender_label, passport_name_label, Gtk.Position.BOTTOM, 1, 1)
        grid.attach_next_to(passport_isscity_label, passport_gender_label, Gtk.Position.BOTTOM, 1, 1)
        grid.attach_next_to(passport_expdate_label, passport_isscity_label, Gtk.Position.BOTTOM, 1, 1)
        grid.attach_next_to(passport_serial_label, passport_expdate_label, Gtk.Position.BOTTOM, 1, 1)

        grid.attach_next_to(passport_country_combo, passport_country_label, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(passport_name_entry, passport_name_label, Gtk.Position.RIGHT, 1, 1)
        grid.attach_next_to(passport_gender_combo, passport_gender_label, Gtk.Position.RIGHT, 1, 1)
        grid.attach_next_to(passport_isscity_entry, passport_isscity_label, Gtk.Position.RIGHT, 1, 1)
        grid.attach_next_to(passport_expdate_entry, passport_expdate_label, Gtk.Position.RIGHT, 1, 1)
        grid.attach_next_to(passport_serial_entry, passport_serial_lavel, Gtk.Position.RIGHT, 1, 1)
