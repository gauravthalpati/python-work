# This is the test code for pytest
# Run this as pytest <folder>\test_code4sum.py -v
# Since sleep does not return anything, retrun value as None is used
# Since we mock the data, actual function does not get called for 120 seconds

from mycode.code4sum import sleep_awhile

def test_sleep_awhile(mocker):
    m=mocker.patch("mycode.code4sum.time.sleep", return_values=None)
    sleep_awhile(120)
    #m.assert_called()
    #assert_not_called()
    m.assert_called_once_with(120)