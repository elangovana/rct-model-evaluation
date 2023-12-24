import os.path
from unittest import TestCase

from preprocess_rct_imdb import PreprocessRCTIMDB


class TestPreprocessRCTIMDB(TestCase):
    def test_process(self):
        # Arrange
        control_file = os.path.join(os.path.dirname(__file__), "sample_data", "imdb_contrast.tsv")
        original_file = os.path.join(os.path.dirname(__file__), "sample_data", "imdb_original.tsv")
        sut = PreprocessRCTIMDB()
        expected_columns = sorted(["case_label", "case_text", "control_text", "control_label"])

        # Act
        actual = sut.process(control_file, original_file)

        # Assert
        self.assertEqual(2, len(actual), "Expect exactly 2 rows")
        self.assertSequenceEqual(expected_columns, sorted(actual.columns))
