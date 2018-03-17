import pkg_resources
import importlib

for entry_point in pkg_resources.iter_entry_points('dwave.samplers'):
    module = importlib.import_module('{}'.format(entry_point.module_name))
    locals()[entry_point.name] = getattr(module, entry_point.name)
