#!/bin/bash
mkdir -p build
env/bin/mypy --junit-xml=build/python-mypy.xml --ignore-missing-imports experiments ||:
env/bin/pylint --reports=n --rcfile=config/pylint.rc --output-format=parseable experiments/*.py experiments/tests > build/python-lint.txt ||:
env/bin/python runtests.py experiments --with-xunit --xunit-file=build/python-tests.xml --cover-xml --cover-xml-file=build/python-coverage.xml ||:
