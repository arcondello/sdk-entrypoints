import pkg_resources

for entry_point in pkg_resources.iter_entry_points('dwave.samplers'):
        exec('from {} import {}'.format(entry_point.module_name, entry_point.name))
