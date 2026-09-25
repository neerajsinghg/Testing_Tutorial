"""
HTML / Web Table Scraper & Parser
Senior SDET Context: Converts raw HTML table structure or Selenium `<tr>`/`<td>` row elements into a structured list of dictionaries.
"""

import re

def parse_html_table(html_content: str) -> list[dict[str, str]]:
    headers = re.findall(r"<th>(.*?)</th>", html_content, re.IGNORECASE)
    row_matches = re.findall(r"<tr>(.*?)</tr>", html_content, re.IGNORECASE | re.DOTALL)
    table_data = []

    for row in row_matches:
        cells = re.findall(r"<td>(.*?)</td>", row, re.IGNORECASE)
        if cells and len(cells) == len(headers):
            row_dict = {headers[i].strip(): cells[i].strip() for i in range(len(headers))}
            table_data.append(row_dict)

    return table_data

if __name__ == "__main__":
    raw_html = """
    <table>
        <tr><th>User ID</th><th>Name</th><th>Role</th></tr>
        <tr><td>101</td><td>Neeraj</td><td>SDET Lead</td></tr>
        <tr><td>102</td><td>Rahul</td><td>Dev Lead</td></tr>
    </table>
    """
    structured_table = parse_html_table(raw_html)
    print("Parsed Web Table Data:")
    for row in structured_table:
        print(row)
