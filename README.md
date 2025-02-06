# Spacewalks

## Overview
Spacewalks is a Python analysis tool for researchers to generate visualisations
and statistical summaries of NASA's extravehicular activity datasets. The contents
are based on coursework about FAIR code development, so their actual usefulness is
mainly didactic and information may be incomplete or incorrect.

## Features
Key features of Spacewalks:

- Generates a CSV table of summary statistics of extravehicular activity crew sizes
- Generates a line plot to show the cumulative duration of space walks over time

## Pre-requisites

Spacewalks was developed using Python version 3.12

To install and run Spacewalks you will need have Python >=3.10
installed. Further libraries are listed in the `requirements.txt`.

## Installation

Clone the Spacewalks repository to your local machine using Git.
If you don't have Git installed, you can download it from the official Git website.

It is recommended to create a virtual environment, from the project directory:

```
python3 -m venv venv_spacewalks
```
Then, activate the environment:
(On Linux or Mac):
```
source venv_spacewalks/bin/activate
```
(On Windows):
```
source venv_spacewalks/Scripts/activate
```
And finally install the libraries in `requirements.txt`:
```
python3 -m pip install -r requirements.txt
```

To ensure everything is working correctly, run the tests using pytest, from within the src directory.
```
python3 -m pytest
```

## Usage Example

```
python3 eva_data_analysis.py eva-data.json eva-data.csv
```
The first argument is path to the JSON data file (and example data file is stored under the `data` directory).
The second argument is the path the CSV output file.
