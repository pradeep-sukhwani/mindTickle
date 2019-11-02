import os
import csv


def main():
    html_structure = ""
    with open(os.getcwd() + '/output.csv') as file_obj:
        data = csv.reader(file_obj)
        html_structure += "<table>"
        for count, row in enumerate(data):
            for row_count, i in enumerate(row):
                if row_count == 0:
                    html_structure += "<th style='border: 1px solid #ddd;'><td style='border: 1px solid #ddd; padding: 8px;'>" + i + "</td></th>"
                else:
                    if row_count == 0:
                        html_structure += "<tr>"
                    html_structure += "<td style='border: 1px solid #ddd;'>" + i + "</td>"
            html_structure += "</tr>"
        html_structure += "</table>"
        with open(os.getcwd() + '/output.html', "w") as html_file:
            html_file.write(html_structure)


if __name__ == '__main__':
    main()
