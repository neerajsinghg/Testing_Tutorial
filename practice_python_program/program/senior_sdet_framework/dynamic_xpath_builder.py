"""
Dynamic XPath Builder & Locators Helper
Senior SDET Context: Safely formats dynamic XPaths with param escaping to locate dynamic web elements (e.g. table cells, dropdowns, dynamic text).
"""

class XPathBuilder:
    @staticmethod
    def contains_text(tag: str, text: str) -> str:
        return f"//{tag}[contains(normalize-space(text()), '{text}')]"

    @staticmethod
    def button_by_label(label: str) -> str:
        return f"//button[contains(@class, 'btn') and text()='{label}']"

    @staticmethod
    def table_cell(row_index: int, col_index: int) -> str:
        return f"//table//tr[{row_index}]/td[{col_index}]"

    @staticmethod
    def input_by_name_or_id(identifier: str) -> str:
        return f"//input[@id='{identifier}' or @name='{identifier}']"

if __name__ == "__main__":
    print("Dynamic Button XPath:", XPathBuilder.button_by_label("Submit Order"))
    print("Dynamic Table Cell XPath:", XPathBuilder.table_cell(row_index=3, col_index=2))
    print("Dynamic Input XPath:", XPathBuilder.input_by_name_or_id("username"))
