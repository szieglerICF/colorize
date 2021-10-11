import re
import sys


class Colorizer:
    def colorize(self, line: str):
        new_line = self._update_numbers(line)
        return new_line

    def _update_numbers(self, line: str):
        return re.sub(r"([0-9]+)", r"<span style='color: red'>\1</span>", line)
