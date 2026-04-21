
# CODING EXERCISES
#
# Q5. Write the exact Python import statement required to use a standard mock and the patch decorator.
#
# Q6. Complete the code to make a mock return a specific dictionary:
#
# my_mock = MagicMock()
# # Assign {"status": 200} to be returned
#
# Q7. Debug this mocking code:
#
# @patch('requests.get')
# def test_api(mock_get):
#     mock_get.return_value = {"data": "success"}
#     result = requests.get("url").json()
#
# Why does result throw an AttributeError, and how do you fix the mock setup?
#
# Q8. Write an assertion to mathematically prove that an AsyncMock named my_mock was awaited exactly 5 times.
#
# Q9. Write a side_effect configuration that simulates an HTTPError crashing the my_mock function.
#
# Q10. Extend the ShopEase project by writing a test using @patch to intercept a fictional core.db.save_cart function, ensuring it is called with cart_id=99 without actually writing to a live database.
# SOLUTIONS FOR CHAPTER 17



# Q5:
from unittest.mock import MagicMock, patch

# Q6:
my_mock.return_value = {"status": 200}

# Q7: requests.get() returns a Response object, not dict. Fix:
mock_get.return_value.json.return_value = {"data": "success"}

# Q8:
assert my_mock.await_count == 5

# Q9:
my_mock.side_effect = Exception("HTTPError: 500 Server Error")

# Q10:
@patch('core.db.save_cart')
def test_save_cart(mock_save):
    # call function that saves cart with id=99
    mock_save.assert_called_once_with(cart_id=99)