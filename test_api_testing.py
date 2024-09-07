import pytest
from playwright.sync_api import *


@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context()
    yield api_context
    api_context.dispose()


@pytest.mark.API
@pytest.mark.all
def test_api_testing(api_context: APIRequestContext):
    # Define the API endpoint
    url = ('https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users?limit=50&offset=0&sortField=u'
           '.userName&sortOrder=ASC')

    response = api_context.get(url)

    if response.status != 200:
        print(f"Expected status code 200 but got {response.status}")
    else:
        # Verify the response status code
        assert response.status == 200

        # Parse and validate the response JSON
        user_data = response.json()
        assert 'username' in user_data, "User detail missing 'username'"
        assert 'role' in user_data, "User detail missing 'role'"
        assert 'status' in user_data, "User detail missing 'status'"
