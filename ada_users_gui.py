#!/usr/bin/env python
# -*_ coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
# import "Cuentas_ada"

class Handler:
    def gtk_main_quit(self, *args):
        Gtk.main_quit(*args)

    def onButtonPressed(self, button):
        print(button, "Hello World!")

    def create_accounts(self, button):
        print("stuff")

    def open_about_dialog(self):
        window = builder.get_object("about_dialog")
        window.connect("delete-event", Gtk.main_quit)
        window.show_all()


    def on_activate(instance):
        print("Activated:", instance)

builder = Gtk.Builder()
builder.add_from_file("ada_gui.glade")
builder.connect_signals(Handler())

window = builder.get_object("main_window")
window.connect("delete-event", Gtk.main_quit)
window.show_all()

Gtk.main()
