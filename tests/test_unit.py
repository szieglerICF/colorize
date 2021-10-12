import unittest
from unittest.mock import MagicMock, Mock, PropertyMock, patch

from colorize import *


class ColorizerUnitTests(unittest.TestCase):
    def test_should_colorize_number(self):
        # Arrange
        subject = Colorizer()

        # Act
        results = subject.colorize("Here is 3983998231 that should be colorized.")
        print(f"test results: {results}")

        # Assert
        self.assertTrue(
            "Here is <span style='color: orange'>3983998231</span> that should be colorized."
            in results
        )

    def test_should_not_colorize_number_in_id(self):
        # Arrange
        subject = Colorizer()

        # Act
        results = subject.colorize("Here is 33jK55 that should be colorized.")
        print(f"test results: {results}")

        # Assert
        self.assertEqual(
            results,
            "<span style='font-family: courier; font-size: small'>Here is 33jK55 that should be colorized.</span><br/>",
        )

    def test_should_colorize_quote(self):
        # Arrange
        subject = Colorizer()

        # Act
        results = subject.colorize('Here is a "quoted" string')
        print(f"test results: {results}")

        # Assert
        self.assertEqual(
            results,
            "<span style='font-family: courier; font-size: small'>Here is a <span style='color: green'>\"quoted\"</span> string</span><br/>",
        )

    def test_should_colorize_single_quote(self):
        # Arrange
        subject = Colorizer()

        # Act
        results = subject.colorize("Here is a 'quoted' string")
        print(f"test results: {results}")

        # Assert
        self.assertEqual(
            results,
            """<span style='font-family: courier; font-size: small'>Here is a <span style='color: green'>'quoted'</span> string</span><br/>""",
        )

    def test_should_colorize_punc(self):
        # Arrange
        subject = Colorizer()

        # Act
        results = subject.colorize('{"hello" : "world"}')
        print(f"test results: {results}")

        # Assert
        self.assertEqual(
            results,
            """<span style='font-family: courier; font-size: small'><span style='color: darkblue'>{</span><span style='color: green'>"hello"</span> : <span style='color: green'>"world"</span><span style='color: darkblue'>}</span></span><br/>""",
        )

    def test_should_colorize_keywords(self):
        # Arrange
        subject = Colorizer()

        # Act
        results = subject.colorize("started yesterday")
        print(f"test results: {results}")

        # Assert
        self.assertEqual(
            results,
            """<span style='font-family: courier; font-size: small'><span style='color: blue'>started</span> yesterday</span><br/>""",
        )

    def test_should_colorize_error(self):
        # Arrange
        subject = Colorizer()

        # Act
        results = subject.colorize("[ERROR] on first line")
        print(f"test results: {results}")

        # Assert
        self.assertEqual(
            results,
            """<span style='font-family: courier; font-size: small'>[<span style='color: red'>ERROR</span>] on first line</span><br/>""",
        )


if __name__ == "__main__":
    unittest.main()
