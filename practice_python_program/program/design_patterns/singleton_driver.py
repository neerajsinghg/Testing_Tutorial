"""
Singleton Design Pattern for Driver / Database Connection Manager
Senior SDET Context: Ensures only a single instance of WebDriver or DB connection is active across tests.
"""

class DriverSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, browser_name: str = "chrome"):
        if self._initialized:
            return
        self.browser_name = browser_name
        self.session_id = f"session_{id(self)}"
        self._initialized = True
        print(f"[Singleton] Created new {self.browser_name} driver session: {self.session_id}")

    def get_session(self) -> str:
        return self.session_id

if __name__ == "__main__":
    driver1 = DriverSingleton("chrome")
    driver2 = DriverSingleton("chrome")
    
    print("Driver 1 Session:", driver1.get_session())
    print("Driver 2 Session:", driver2.get_session())
    print("Are driver1 and driver2 identical instances?", driver1 is driver2)
