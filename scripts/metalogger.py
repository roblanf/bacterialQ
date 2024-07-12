import json
import os
from threading import Lock

class MetaLogger:
    _instance = None
    _lock = Lock()

    def __new__(cls, file_path):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(MetaLogger, cls).__new__(cls)
                cls._instance._initialize(file_path)
        return cls._instance

    def _initialize(self, file_path):
        self.file_path = file_path
        self.parameters = {}
        if os.path.exists(self.file_path):
            self._read_parameters()

    def log_parameter(self, para_name, para_value):
        """Log a single parameter."""
        self.parameters[para_name] = para_value
        self._write_parameters()

    def log_parameters(self, params_dict):
        """Log a dictionary of parameters."""
        self.parameters.update(params_dict)
        self._write_parameters()

    def _write_parameters(self):
        """Write the parameters to the file, updating existing ones."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                existing_parameters = json.load(file)
            existing_parameters.update(self.parameters)
        else:
            existing_parameters = self.parameters

        with open(self.file_path, 'w') as file:
            json.dump(existing_parameters, file, indent=4)

    def _read_parameters(self):
        """Read the parameters from the file."""
        with open(self.file_path, 'r') as file:
            self.parameters = json.load(file)

    @classmethod
    def get_instance(cls, file_path):
        """Get the singleton instance of MetaLogger."""
        return cls(file_path)