import pandas as pd
from mrbob.rendering import parse_variables
from encode.mouse.csvreader import parse


def pre_render(self):
    self.variables = parse_variables(self.variables)
    if len(self.variables['frame']) == 0:
        return ""
