from random import randint, random

scss_files = ["purple.css"]


def get_random_background():
    random_index = randint(0, len(scss_files) - 1)
    # return "{{ url_for('static',filename='styles/backgrounds/{" + scss_files[random_index] +  "}') }}"
    return scss_files[random_index]
