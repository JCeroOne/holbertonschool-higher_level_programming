#!/usr/bin/python3
"""No comment."""


class SwimMixin:
    """SwimMixin."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """FlyMixin."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon."""

    def roar(self):
        print("The dragon roars!")
