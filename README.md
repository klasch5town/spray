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

Commands
--------

- create row: creates a row like entry to the yaml file
- add to row: adds one or more items to a row.
- delete from row: removes one or more items from a row.

The first yaml entry represents the header for the table.

Roadmap
-------

- [x] create a row with given header
- [ ] convert spreadsheet (Excel) into YAML file
- [ ] add a row/entry with data
  - [ ] one-shot via command line
  - [ ] interactive: asking for each column via command line
- [ ] delete a row/entry
- [ ] add a column (new item in dataset of a row)
- [ ] export YAML content to spreadsheet file (Excel)
- [ ] store yaml-file path to yaml2xls.yml config-file located at home subfolder .yaml2xls (~/.yaml2xls/yaml2xls.yml) such that there is no need to provide it via command line all the time.
- [ ]

Links
-----

- YAML at Wikipedia => https://en.wikipedia.org/wiki/YAML
- Home of YAML => https://yaml.org/
- YAML specification 1.2.2 => https://yaml.org/spec/1.2.2/
- openpyxl project => https://openpyxl.readthedocs.io/en/stable/
- working with openpyxl => https://www.geeksforgeeks.org/creating-the-workbook-and-worksheet-using-openpyxl-in-python/

License
-------

Distributed under the Unlicense License. See LICENSE file for more information.
