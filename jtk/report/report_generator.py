__author__ = 'jubin'

import jinja2
import datetime

report_template = None

report_path = None


def __get_template(file_path):
    """
    :rtype : template object fron jinja2
    """
    global report_template

    if file_path is None:
        raise Exception('No Template specified')

    report_template = file_path

    template_loader = jinja2.FileSystemLoader(searchpath='/')

    template_env = jinja2.Environment(loader=template_loader)

    return template_env.get_template(report_template)


def get_report(template_path, title, desc, table_desc, table_caption, column_headers=[], rows=[[]]):
    template = __get_template(template_path)

    template_vars = {'title': title, 'description': desc, 'tableDescription': table_desc, 'tableCaption': table_caption,
                     'columnHeaders': column_headers, 'rows': rows}

    if report_path is None:

        return template.render(template_vars)

    else:
        today = datetime.date.today().strftime("%Y%m%d")

        global report_path

        report_path = report_path + '_' + str(today) + '.html'

        with open(report_path, "w") as fh:

            fh.write(template.render(template_vars))
