import pytest
from task1 import OpenFile


# I'll use "fixtures can request other fixtures"
# Some nice theory: in this code, test_data “requests” check and when pytest sees this, it will execute
# the check fixture function and pass the object it returns into test_data as the check argument.
@pytest.fixture
def replace_file_obj():
    return "new_test.txt"


@pytest.fixture
def data_to_check(replace_file_obj):
    with OpenFile(replace_file_obj, 'r') as opened_file:
        data = opened_file.read()
        return data[:10]


def test_data(data_to_check):
    assert data_to_check == "this is al"

# code output:
# task3.py::test_data PASSED                                               [100%]
#
# ============================== 1 passed in 0.01s ===============================

