import os
import json
import csv

class MetaInfoReader:
    def __init__(self, file_path):
        self.file_path = os.path.abspath(file_path)
        self.name = None
        self.properties = self._read_properties()

    def _read_properties(self):
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


def meta_folder_to_table(meta_folder, output_csv, property_names=None):
    """
    Converts a folder of meta.json files to a CSV table.

    Args:
        meta_folder (str): Path to the folder containing meta.json files.
        output_csv (str): Path to the output CSV file.
        property_names (list, optional): List of property names to include in the table. 
                                        If None, all properties are included.
    """
    meta_manager = MetaInfoManager()
    for filename in os.listdir(meta_folder):
        if filename.endswith(".json"):
            meta_file_path = os.path.join(meta_folder, filename)
            meta_info = MetaInfoReader(meta_file_path)
            meta_info.set_name(filename[:-5])  # Remove .json extension for name
            meta_manager.add_meta_file(meta_info)

    if property_names is None:
        # Get all property names from the first meta file
        property_names = list(meta_manager.meta_files[0].properties.keys())

    property_table = meta_manager.get_property_table(property_names)

    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        header = ["phylum"] + property_names
        writer.writerow(header)
        for phylum, row in property_table.items():
            writer.writerow([phylum] + [row[prop] for prop in property_names])


if __name__ == "__main__":
    meta_folder = "/home/tim/project/bacterialQ/Result_nova/add_phylum_collection/add_phylum_with_real_aa/meta"  # Replace with your meta folder path
    output_csv = "/home/tim/project/bacterialQ/Result_nova/add_phylum_collection/add_phylum_with_real_aa/meta_table.csv"  # Replace with your desired output CSV path
    meta_folder_to_table(meta_folder, output_csv)