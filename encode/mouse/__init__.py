"""
This is the encode.mouse Python module.
"""
import pandas as pd
from mrbob.rendering import parse_variables
from encode.mouse.csvreader import parse


def get_dimension(self):
    self.variables = parse_variables(self.variables)
    url_template = self.variables['url_template']
    number = 0
    for dimension_id in self.variables['dimensions'].split():
        dimension = self.variables['dimension'][dimension_id]
        dimension['url'] = url_template % dimension['encode_id']
        unique_values = list(self.variables['frame'][dimension['id']].unique())
        dimension['unique_values'] = unique_values
        dimension['number'] = number
        if dimension_id == self.variables['colour']:
            dimension['colour_mapping'] = {}
            for index, value in enumerate(unique_values):
                dimension['colour_mapping'][value] = dimension['colours'][index]
        number = number + 1

def get_frame(self):
    # Read the input file in ENCODE format
    file_path = 'encode/mouse/apache_export/mm9_RNA_dashboard_files.txt'
    frame = pd.DataFrame(parse(file_path), dtype=object)
    frame['Lab'] = frame['lab']
    frame['Sample Replicate'] = frame['replicate']
    frame['Biological Replicate'] = frame['Sample Replicate']
    frame['Read Type'] = frame['readType']
    frame['Replicate Insert Length'] = frame['insertLength']
    frame['Insert Length'] = frame['Replicate Insert Length'].fillna('')
    frame['File View'] = frame['view']
    frame['File Type'] = frame['type']
    frame['Treatment'] = frame['treatment'].fillna('')
    frame['Technology'] = frame['dataType'] + ' (' + frame['grant'] + ')'
    frame['Compartment'] = frame['localization'].fillna('cell').map({'cell':'Whole-cell'})
    frame['labExpId'] = frame['labExpId'].map(lambda x: tuple(x.split(',')))
    frame['Sample Internal Name'] = frame['labExpId'].map(lambda x: ', '.join(x))
    self.variables['frame'] = frame
