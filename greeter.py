class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self, style="friendly"):
        if style == "friendly":
            return self._friendly_greet()
        elif style == "formal":
            return self._formal_greet()

        return "Hello!"

    def _friendly_greet(self):
        return f"Hey there, {self.name}!"

    def _formal_greet(self):
        return f"Good day, {self.name}."
