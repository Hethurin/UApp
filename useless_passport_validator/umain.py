#!/usr/bin/python3.4
import ulibrary
import sys
from uwindow import UWindow
from gi.repository import Gtk


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main():
    ulibrary.init()

    uwindow = UWindow()
    uwindow.connect("delete-event", Gtk.main_quit)
    uwindow.show_all()
    Gtk.main()

if __name__ == "__main__":
    sys.exit(main())
