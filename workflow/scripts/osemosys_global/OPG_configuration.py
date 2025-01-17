'''Functionality to interface with configuration files. '''

from pathlib import Path
import yaml

class ConfigFile:
    '''Class to hold yaml configuration file data
    
    Args: 
        config_file_name = yaml file name in the config/ folder 
        
    Example: 
        config = ConfigFile('settings')
        config.get('geographic_scope')
        -> ['IND','NPL']
    '''
    def __init__ (self, config_file_name): 
        self.file_path = Path(Path(__file__).resolve().parent, 
            '../../../config', f'{config_file_name}.yaml')

    def get(self, name):
        with open(self.file_path, encoding='utf-8') as yaml_file:
            parsed_yaml_file = yaml.load(yaml_file, Loader = yaml.FullLoader).get(name)
        return parsed_yaml_file

class ConfigPaths:
    '''Class to hold relative paths from file called from. '''    

    # Hard coded file structure 
    input_dir_name = 'resources'
    output_dir_name = 'results'
    py_file_dir = Path(__file__).resolve().parent # folder of this module 
    
    def __init__(self):
        # USER CALLABLE PATHS
        self.input_dir = Path(self.py_file_dir, '../../../', self.input_dir_name)
        self.input_data_dir = Path(self.input_dir, 'data')

        self.output_dir = Path(self.py_file_dir, '../../../', self.output_dir_name)
        self.output_data_dir = Path(self.output_dir, 'data')

        #self.scenario_name = self.get_scenario_name(self)
        self.scenario_dir = Path(self.output_dir, self.get_scenario_name())
        self.scenario_data_dir = Path(self.scenario_dir, 'data')
        self.scenario_figs_dir = Path(self.scenario_dir, 'figures')
        self.scenario_results_dir = Path(self.scenario_dir, 'results')

        self.simplicity = Path(self.input_dir, 'simplicity')
        self.simplicity_data = Path(self.input_dir, 'simplicity/data')

    def get_scenario_name(self):
        config = ConfigFile('config')
        return config.get('scenario') 