import re
import sys


class Colorizer:
    def colorize(self, line: str):
        new_line = self._update_quotes(line)
        new_line = self._update_numbers(new_line)
        new_line = self._update_punc(new_line)
        new_line = self._update_keywords(new_line)
        new_line = self._update_errors(new_line)
        return f"<span style='font-family: courier; font-size: small'>{new_line}</span><br/>"

    def _update_numbers(self, line: str):
        return re.sub(r"(\b[0-9]+\b)", r"<span style='color: brown'>\1</span>", line)

    def _update_quotes(self, line: str):
        line = re.sub(r"(\'[^\']+\')", r"<span style='color: green'>\1</span>", line)
        line = re.sub(r"(\"[^\"]+\")", r"<span style='color: green'>\1</span>", line)
        return line

    def _update_punc(self, line: str):
        return re.sub(r"([{}+-])", r"<span style='color: darkblue'>\1</span>", line)

    def _update_keywords(self, line: str):
        return re.sub(
            r"(\bstart\b|\bstarted\b|\bend\b|\bended\b|\bfinish\b|\bfinished\b)",
            r"<span style='color: blue'>\1</span>",
            line,
            flags=re.IGNORECASE,
        )

    def _update_errors(self, line: str):
        return re.sub(
            r"(\berror\b)",
            r"<span style='color: red'>\1</span>",
            line,
            flags=re.IGNORECASE,
        )


def main():
    colorizer = Colorizer()
    for line in sys.stdin:
        print(colorizer.colorize(line))


if __name__ == "__main__":
    main()
