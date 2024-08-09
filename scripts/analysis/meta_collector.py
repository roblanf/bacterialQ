import os
import json

class MetaInfoReader:
    def __init__(self, file_path):
        self.file_path = os.path.abspath(file_path)
        self.name = None
        self.properties = self._read_properties()

    def _read_properties(self):
        # Read the JSON file and load it as a dictionary
        with open(self.file_path, 'r') as file:
            properties = json.load(file)
        return properties

    def set_name(self, rule):
        try:
            self.name = rule.format(**self.properties)
        except KeyError as e:
            print(f"Error: Missing property {e} for naming rule.")

    def get_property(self, property_name):
        return self.properties.get(property_name)

    def __repr__(self):
        return f"MetaInfoReader(name={self.name}, path={self.file_path})"

class MetaInfoManager:
    def __init__(self):
        self.meta_files = []

    def add_meta_file(self, meta_info_reader):
        self.meta_files.append(meta_info_reader)

    def add_meta_files(self, meta_info_readers):
        self.meta_files.extend(meta_info_readers)

    def get_property_dict(self, property_name):
        property_dict = {}
        for meta_file in self.meta_files:
            property_dict[meta_file.name] = meta_file.get_property(property_name)
        return property_dict

    def get_property_table(self, property_names):
        table = {}
        for meta_file in self.meta_files:
            row = {prop: meta_file.get_property(prop) for prop in property_names}
            table[meta_file.name] = row
        return table

    def rejoin_meta_files(self, force=False, record_path=False):
        merged_properties = {}
        for meta_file in self.meta_files:
            for key, value in meta_file.properties.items():
                if key not in merged_properties:
                    merged_properties[key] = {}
                merged_properties[key][meta_file.name] = value
    
        # Set missing properties to None if force=True
        if force:
            all_keys = set(merged_properties.keys())
            for meta_file in self.meta_files:
                for key in all_keys:
                    if key not in meta_file.properties:
                        merged_properties[key][meta_file.name] = None
    
        if record_path:
            merged_properties['path'] = {}
            for meta_file in self.meta_files:
                merged_properties['path'][meta_file.name] = meta_file.file_path


        return merged_properties
