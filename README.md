# Software-engineering

[![Build Status](https://dev.azure.com/3AONA/Software%20engineering/_apis/build/status/timmermansjoy.Software-engineering?branchName=refs%2Fpull%2F5%2Fmerge)](https://dev.azure.com/3AONA/Software%20engineering/_build/latest?definitionId=1&branchName=refs%2Fpull%2F5%2Fmerge)
![Run all tests](https://github.com/timmermansjoy/Software-engineering/actions/workflows/run_tests.yml/badge.svg)
[![DeepSource](https://deepsource.io/gh/timmermansjoy/Software-engineering.svg/?label=active+issues&show_trend=true&token=fNqmvRX-yr1W5fMA9Ic-rBOa)](https://deepsource.io/gh/timmermansjoy/Software-engineering/?ref=repository-badge)
![Run all tests](https://github.com/timmermansjoy/Software-engineering/actions/workflows/main_3tina.yml/badge.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

<p align="center">
  <img width="500px" src="https://images.unsplash.com/photo-1538474705339-e87de81450e8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80">
</p>

## About

This project is created for the course Software Engineering at PXL, with the purpose of creating a csv parser that can be used to create groups of students.

## Requirements

To use this project it is required to install the dependencies with

```bash
pip install -e . --use-feature=in-tree-build
```

For develoment it is required to run.

```bash
pip install -e ".[development]" --use-feature=in-tree-build
```

If that doesnt work use `pip3` this is because you also have python 2 installed

## FLASK-application

To run the FLASK-application, start with installing flask

```bash
pip install flask
```

Once flask is installed, navigate to the src-folder. Once there, run the following:

```bash
set FLASK_ENV=development
python -m flask run
```

The last command will give you the adress to navigate towards to use the app.
