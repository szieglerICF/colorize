import re
import sys


class Colorizer:
    def colorize(self, line: str):
        new_line = self._update_numbers(line)
        new_line = self._update_quotes(new_line)
        new_line = self._update_punc(new_line)
        new_line = self._update_keywords(new_line)
        return f"<span style='font-family: courier; font-size: small'>{new_line}</span><br/>"

    def _update_numbers(self, line: str):
        return re.sub(r"(\b[0-9]+\b)", r"<span style='color: gold'>\1</span>", line)

    def _update_quotes(self, line: str):
        return re.sub(r"(\"[^\"]+\")", r"<span style='color: darkred'>\1</span>", line)

    def _update_punc(self, line: str):
        return re.sub(r"([{}+-])", r"<span style='color: blue'>\1</span>", line)

    def _update_keywords(self, line: str):
        return re.sub(
            r"(\bERROR\b)", r"<span style='color: red'>\1</span>", line, re.IGNORECASE
        )


def main(line: str):
    colorizer = Colorizer()
    print(colorizer.colorize(line))


if __name__ == "__main__":
    line = sys.argv[1]
    main(line)
