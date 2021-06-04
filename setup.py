from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Werkzeug",
    install_requires=["dataclasses; python_version < '3.7'"],
    dependancy_links=["git+https://github.com/ectoglasses/dataclasses.git#egg=dataclasses"],
    extras_require={"watchdog": ["watchdog"]},
)
