"""Signals from the django_bouncy app"""
# pylint: disable=invalid-name
from django.dispatch import Signal

# Any notification received
# providing_args = ["notification", "request"]
notification = Signal()

# New SubscriptionConfirmation received
# providing_args = ["result", "notification"]
subscription = Signal()

# New bounce or complaint received
# providing_args = ["instance", "message", "notification"]
feedback = Signal()
