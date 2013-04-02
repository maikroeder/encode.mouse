import codecs
from pkg_resources import get_provider


def pre_render(self):
    provider = get_provider('encode.mouse')
    file_name = provider.get_resource_filename('encode.mouse', 'tables/output/tables')
    self.variables['tables'] = codecs.open(file_name, 'r', 'utf-8').read()
    

