#!/usr/bin/env python3

class Coffee:
    def __init__(self, size=None, price=0.0):
        self._size = None
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        allowed = ("Small", "Medium", "Large")
        if value in allowed:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        try:
            self.price += 1
        except Exception:
            self.price = 1