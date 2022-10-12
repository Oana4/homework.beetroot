import unittest
import homework_09.task2 as program


class PhonebookTestCase(unittest.TestCase):

    # not working!!
    def test_search_by(self):
        new_phonebook = program.phonebook
        self.assertEqual(new_phonebook.search_by("First name", "john"), "The phonebook doesn't have any records!")


if __name__ == "__main__":
    unittest.main()
