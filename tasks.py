"""Development tasks for django-experiments."""
from invoke import task, run

PYTHON_MODULES = ['experiments']


# pylint: disable=unused-argument
@task(name='format')
def format_python(ctx):
    """Run python autoformating."""
    run('isort --line-width=100 --recursive experiments')
    run('yapf --in-place --style=config/style.yapf --recursive experiments tasks.py')


@task(name='lint')
def lint_python(ctx):
    """Run python linting."""
    run('pylint --reports=n --rcfile=config/pylint.rc tasks.py ' + ' '.join(PYTHON_MODULES))
    run('mypy --ignore-missing-imports experiments')


@task(name='test')
def test_python(ctx):
    """Run python tests."""
    run('./runtests.py experiments')
