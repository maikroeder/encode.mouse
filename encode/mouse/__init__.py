"""
This is the encode.mouse Python module.
"""
import pandas as pd
from mrbob.rendering import parse_variables
from encode.mouse.csvreader import parse

def counter():
    i = 0
    while True:
       yield i
       i += 1

def debug(arg1, arg2):
	import pdb; pdb.set_trace()

def level_1(self):
    self.variables = parse_variables(self.variables)
    self.variables['colours'] = self.variables['colours'].split()
    self.variables['dimensions'] = self.variables['dimensions'].split()
    self.variables['left_row_left'] = self.variables['left_row_left'].split()
    self.variables['left_row_right'] = self.variables['left_row_right'].split()
    self.variables['left_row'] = self.variables['left_row_left'] + self.variables['left_row_right'] 
    self.variables['left_rows'] = list(self.variables['frame'].groupby(self.variables['left_row']).ix.keys())
    self.variables['grouped'] = self.variables['frame'].groupby(self.variables['dimensions'])
    url_template = self.variables['url_template']
    number = 0
    for dimension_id in self.variables['dimensions']:
        dimension = self.variables['dimension'][dimension_id.lower()]
        dimension['url'] = url_template % dimension['encode_id']
        unique_values = list(self.variables['frame'][dimension['id']].unique())
        dimension['unique_values'] = unique_values
        dimension['number'] = number
        if dimension_id == self.variables['colour']:
            dimension['colour_mapping'] = {}
            for index, value in enumerate(unique_values):
                dimension['colour_mapping'][value] = self.variables['colours'][index]
        number = number + 1
    self.variables['counter'] = counter()
    self.variables['debug'] = debug


def level_2(self):
    self.variables = parse_variables(self.variables)
    self.variables['dimensions'] = self.variables['dimensions'].split()
    self.variables['index'] = self.variables['index'].split()
    self.variables['grouped'] = self.variables['frame'].groupby(self.variables['index'])
    self.variables['column_headers'] = sorted(self.variables['frame'][self.variables['column']].unique())
    number = 0
    for dimension_id in self.variables['dimensions']:
        dimension = self.variables['dimension'][dimension_id.lower()]
        unique_values = list(self.variables['frame'][dimension['id']].unique())
        dimension['unique_values'] = unique_values
        dimension['number'] = number
        number = number + 1
    self.variables['counter'] = counter()
    self.variables['debug'] = debug
    self.variables['render_cell'] = lambda a, b, c, d:''
    self.variables['template_folder'] = ''

def level_3(self):
    self.variables = parse_variables(self.variables)
    self.variables['dimensions'] = self.variables['dimensions'].split()
    number = 0
    for dimension_id in self.variables['dimensions']:
        dimension = self.variables['dimension'][dimension_id.lower()]
        unique_values = list(self.variables['frame'][dimension['id']].unique())
        dimension['unique_values'] = unique_values
        dimension['number'] = number
        number = number + 1

def get_frame(self):
    # Read the input file in ENCODE format
    file_path = 'encode/mouse/apache_export/mm9_RNA_dashboard_files.txt'
    frame = pd.DataFrame(parse(file_path), dtype=object)
    frame['dateunrestricted'] = frame['dateUnrestricted']
    frame['biologicalreplicate'] = frame['replicate']
    frame['readtype'] = frame['readType']
    frame['insertlength'] = frame['insertLength'].fillna('')
    frame['fileview'] = frame['view']
    frame['rnaextract'] = frame['rnaExtract']
    frame['filetype'] = frame['type']
    frame['fileurl'] = frame['File URL']
    frame['treatment'] = frame['treatment'].fillna('')
    frame['technology'] = frame['dataType'] + ' (' + frame['grant'] + ')'
    frame['compartment'] = frame['localization'].fillna('cell').map({'cell':'Whole-cell'})
    frame['labExpId'] = frame['labExpId'].map(lambda x: tuple(x.split(',')))
    frame['sampleinternalname'] = frame['labExpId'].map(lambda x: ', '.join(x))
    self.variables['frame'] = frame
