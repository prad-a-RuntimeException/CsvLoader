from unittest import TestCase
from csv_reader import read_file, __get_delimiter as get_delimiter
from tests.test_utils import get_path


class CSVReaderTests(TestCase):
    def test_infer_delimiter(self):
        delimiter = get_delimiter("~203~^~g~^~PROCNT~^~Protein~^~2~^~600~ ")
        self.assertEqual(delimiter, "~")

    def test_read_csv_file_with_provided_delimiter(self):
        content = read_file(get_path("usda/data-files/NUTR_DEF.txt"), '^')
        self.assertEqual(sum(1 for _ in content), 150)
