


"""def json_to_html_table(json_data):
    table = "<table border='1' style='border-collapse: collapse; width: 100%;'>"
    table += "<thead><tr>"

    # Add table headers
    headers = json_data[0].keys()
    for header in headers:
        table += f"<th style='padding: 8px; text-align: left;'>{header}</th>"
    table += "</tr></thead><tbody>"

    # Add table rows
    for row in json_data:
        table += "<tr>"
        for cell in row.values():
            table += f"<td style='padding: 8px;'>{cell}</td>"
        table += "</tr>"

    table += "</tbody></table>"
    return table
a={1: 'Karthi',2:'keyan'}
print(json_to_html_table(a))"""
def json_to_html_table_from_dict(dictionary):
    table = "<table border='1' style='border-collapse: collapse; width: 100%;'>"
    table += "<thead><tr><th style='padding: 8px; text-align: left;'>Key</th><th style='padding: 8px; text-align: left;'>Value</th></tr></thead><tbody>"

    for key, value in dictionary.items():
        table += f"<tr><td style='padding: 8px;'>{key}</td><td style='padding: 8px;'>{value}</td></tr>"

    table += "</tbody></table>"
    return table

a = {1: "Karthi", 2: "keyan"}
html_table = json_to_html_table_from_dict(a)
print(html_table)