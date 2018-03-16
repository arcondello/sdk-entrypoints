from __future__ import absolute_import

from setuptools import setup

package_name = 'dwave_a'

# These should be minimal requiments for the package to work, and avoid pinning dependencies unless required. See
# https://packaging.python.org/discussions/install-requires-vs-requirements/
install_requires = []

# Any extra requirements, to be used by pip install PACKAGENAME['keyname']
extras_require = {}

# The packages in this repo that are to be installed. Either list these explictly, or use setuptools.find_packages. If
# the latter, take care to filter unwanted packages (e.g. tests)
packages = ['dwave_a']

setup(
    name=package_name,
    version='0.1',
    packages=packages,
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points={'dwave.samplers': ['a_name = dwave_a:ASampler'],
                  'dwave.composites': ['AComposite = dwave_a:AComposite'],
                  'dwave.utilities': ['a_function = dwave_a:a_function']}
)
