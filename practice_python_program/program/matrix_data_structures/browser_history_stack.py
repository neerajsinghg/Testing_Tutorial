"""
Browser Back/Forward Navigation Simulation using Stacks
Senior SDET Context: Uses two stacks (`back_stack` and `forward_stack`) to simulate browser URL navigation history.
"""

class BrowserHistory:
    def __init__(self, homepage: str):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = homepage
        print(f"[History] Initialized homepage: {self.current_page}")

    def visit(self, url: str) -> None:
        self.back_stack.append(self.current_page)
        self.current_page = url
        self.forward_stack.clear()
        print(f"[Visit] Navigated to: {self.current_page}")

    def back(self, steps: int = 1) -> str:
        while steps > 0 and self.back_stack:
            self.forward_stack.append(self.current_page)
            self.current_page = self.back_stack.pop()
            steps -= 1
        print(f"[Back] Now at: {self.current_page}")
        return self.current_page

    def forward(self, steps: int = 1) -> str:
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.current_page)
            self.current_page = self.forward_stack.pop()
            steps -= 1
        print(f"[Forward] Now at: {self.current_page}")
        return self.current_page

if __name__ == "__main__":
    browser = BrowserHistory("google.com")
    browser.visit("github.com")
    browser.visit("leetcode.com")
    browser.back(1)
    browser.back(1)
    browser.forward(1)
