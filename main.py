__author__ = 'jubin'

import jtk.report.report_generator as report

if __name__ == '__main__':
    report.report_path = '/home/jubin/projects/PyReport/report/fixing'

    columnHeaders = ['Column1', 'Column2', 'Column3']

    table = [["value1", "value2", "value3"], ["value1", "value2", "value3"], ["value1", "value2", "value3"]]

    report.get_report('/home/jubin/projects/PyReport/template/report.jinja', "EOD report generation",
                      "Daily report generated for EOD",
                      "List of Ids that failed the EOD activity", "Fixing", columnHeaders, table)
