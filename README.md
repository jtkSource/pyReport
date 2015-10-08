========
PyReport
========

Using Jinja2  to create a simple html report that will grow table as per size of the dataset column and row wise.

Main modules are:

- `jtk.report.report_generator`

Sample Code::

    report.report_path = '/home/jubin/projects/PyReport/report/fixing'

    columnHeaders = ['Column1', 'Column2', 'Column3']

    table = [["value1", "value2", "value3"], ["value1", "value2", "value3"], ["value1", "value2", "value3"]]

    report.get_report('/home/jubin/projects/PyReport/template/report.jinja', "EOD report generation",
                      "Daily report generated for EOD",
                      "List of Ids that failed the EOD activity", "Fixing", columnHeaders, table)

- `main.py`

`report.report_path` specifies the full file name for the report. This is appended with the date in YYYYMMDD.html format

