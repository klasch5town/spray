spray
=====

Motivation
----------

Excel respectively spreadsheets are a cancer in office realm.
Reasons are:

- have you ever tried to compare excel-files?
- using spreadsheets in version control systems brings no advantage like diffing, in-place-review,...

The spray project tries to reduce the need for using Excel.

The name is simple constructed from 'SPReadsheet And Yaml'.

Description
-----------

The content of a given YAML file is treaded like a table.
The first block-entry in the YAML file represents the header of the table.
Each following block is treaded like a table row.
Each entry of a YAML-block represents a column in the table

Setup
-----

Make sure you have python installed:

```shell
python --version
```

should show the python version. It should be 3.10 or 3.11.

Next step is to check if pdm is intalled:

```shell
pdm --version
# or if pdm 'is not in the path'
python -m pdm --version
```

If it is not installed, install it by calling:

```shell
pip install pdm
```

Finally let pdm create your virtual environment and install the needed python modules:

```shell
pdm install
```

usage
-----

```help
usage: spray.py [-h] [-d] [-v] [-t TASK] [-y YAML_FILE] input

positional arguments:
  input                 input to handle with the given task

options:
  -h, --help            show this help message and exit
  -d, --debug           show debug output at console
  -v, --verbose         show more console output
  -t, --task TASK       the task to do, like:
                        - create
                        - yaml2xls
                        - xls2yaml
  -y, --yaml_file YAML_FILE
                        YAML based input file.
```

example
-------

```shell
python spray -y example.yml -t create id,name,description
```

will create a yaml file like

```yaml
- id: id
  name: name
  description: description
```

Roadmap
-------

- [x] create a row with given header
- [x] convert spreadsheet (Excel) into YAML file
- [ ] rework parameter structure and handling
- [ ] add a row/entry with data
  - [ ] one-shot via command line
  - [ ] interactive: asking for each column via command line
- [ ] delete a row/entry
- [ ] add a column (new item in dataset of a row)
- [x] export YAML content to spreadsheet file (Excel)
- [ ] store yaml-file path to yaml2xls.yml config-file located at home subfolder .yaml2xls (~/.yaml2xls/yaml2xls.yml) such that there is no need to provide it via command line all the time.
- [ ] provide an show option to view the table in the browser (e.g. via flask)

Links
-----

- YAML at Wikipedia => https://en.wikipedia.org/wiki/YAML
- Home of YAML => https://yaml.org/
- YAML specification 1.2.2 => https://yaml.org/spec/1.2.2/
- pyyaml home => https://pyyaml.org/
- openpyxl project => https://openpyxl.readthedocs.io/en/stable/
- working with openpyxl => https://www.geeksforgeeks.org/creating-the-workbook-and-worksheet-using-openpyxl-in-python/

License
-------

Distributed under the Unlicense License. See LICENSE file for more information.
