import pkg_resources

for entry_point in pkg_resources.iter_entry_points('dwave.samplers'):
    module = __import__('{}'.format(entry_point.module_name))
    locals()[entry_point.name] = getattr(module, entry_point.name)
