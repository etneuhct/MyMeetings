import random
import string
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible
from django.core import validators


def create_random_password():
    selected_digits = random.choices(string.digits, k=3)
    selected_upper = random.choices(string.ascii_uppercase, k=3)
    selected_lower = random.choices(string.ascii_lowercase, k=3)
    letter = list(selected_digits + selected_upper + selected_lower)
    random.shuffle(letter)
    return ''.join(letter)

