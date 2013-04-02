import pandas as pd
from mrbob.rendering import parse_variables
from encode.mouse.csvreader import parse


def pre_render(self):
    self.variables = parse_variables(self.variables)
    frame = get_frame()
    url_template = self.variables['url_template']
    number = 0
    for dimension_id in self.variables['dimensions'].split():
        dimension = self.variables['dimension'][dimension_id]
        dimension['url'] = url_template % dimension['encode_id']
        unique_values = list(frame[dimension['id']].unique())
        dimension['unique_values'] = unique_values
        dimension['number'] = number
        if dimension_id == self.variables['colour']:
            dimension['colour_mapping'] = {}
            for index, value in enumerate(unique_values):
                dimension['colour_mapping'][value] = dimension['colours'][index]
        number = number + 1
