import pkg_resources
import importlib

# prevent entrypoints from appearing in the top-level namespace.
# If we want fine grained control, we can add __all__.append(entry_point.ane) to the for loop below.
__all__ = []

for entry_point in pkg_resources.iter_entry_points('dwave.samplers'):
    module = importlib.import_module('{}'.format(entry_point.module_name))
    locals()[entry_point.name] = getattr(module, entry_point.name)
