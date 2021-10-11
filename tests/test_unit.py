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
            "Here is <span style='color: red'>3983998231</span> that should be colorized."
            in results
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
            "Here is <span style='color: red'>3983998231</span> that should be colorized.",
        )


if __name__ == "__main__":
    unittest.main()
