import codecs
from pkg_resources import get_provider


def pre_render(self):
    provider = get_provider('encode.mouse')

