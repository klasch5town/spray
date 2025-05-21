Parameter handling
==================

Pre-Conditions
--------------

What we need to handle:

- yaml-file
- spreadsheet file
- command to handle
  - convert
    - yaml to spreadsheet (excel)
    - spreadsheet (Excel) to yaml
- add a dataset (table-row)
- insert item to the dataset (add column)
- data to work at (task-context)
  - dataset in JSON notation? (JSON fits better on command-line as YAML)
  - name of YAML file to tread as data

Command line
------------

```text
positional arguments:
  task  the task to be processed:
    - yaml2xls
    - xls2yaml
    - new
    - add
    - insert
    - remove
    - delete
    - list
    - info

options:
-c  context: may be data in JSON format or yaml file with data or information which
             item to add, remove or delete
-d  show debug output
-v  show verbose output
```