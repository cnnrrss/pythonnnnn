# Pythonnnnn

A production ready python template. Elevate your python from scripts to service.

## Linting

Flake8 and pylint.

Rules can be customised in .pylintrc

It is recommended to setup linting on save in your IDE of choice.

## Environment

This project uses Pipenv, a combination of pyenv and virtualenv which provides dynamic tooling across python and lib
versions.

To install a new dependency:

`pipenv install numpy`

To install a new dev dependency use the dev kwarg:

`pipenv install --dev coverage`

## Testing

This repo uses the _unittest_ lib for testing. All files should provide unit test coverage.

Coverage is calculated with the conveniently named lib _coverage_.

Run tests:

`coverage  run --source=. -m unittest discover`

Get coverage report:

`coverage report -m`

To generate and view the report as html

`coverage html && cd htmlcov && python3 -m http.server 8000`