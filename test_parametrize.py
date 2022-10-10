from dataclasses import dataclass

import pytest


@pytest.mark.parametrize(["browser", "test_user"],
                         [("Chrome", 100), ("Firefox", 200)],
                         ids=["Chrome with business account", "Firefox with personal account"],
                         )
def test_with_param(browser, test_user):
    pass


@pytest.mark.parametrize("browser", ["Chrome", "Firefox"])
@pytest.mark.parametrize("test_user", [100, 200], ids=["business account", "personal account"])
def test_with_param2(browser, test_user):
    pass


@pytest.mark.parametrize("browser", [pytest.param("Firefox", marks=[pytest.mark.skip("Firefox tests broken")]),
                                     pytest.param("Chrome")])
@pytest.mark.parametrize("test_user", [100, 200], ids=["business account", "personal account"])
def test_with_param3(browser, test_user):
    pass


@pytest.fixture(params=["Chrome", "Firefox"])
def browser(request):
    assert request.param in ["Chrome", "Firefox"]
    return {"browser_name": request.param}


@pytest.fixture(params=[100])
def test_user(request):
    return request.param


def test_with_parametrized_fixture(browser, test_user):
    pass


@pytest.fixture(params=[])
def account(request):
    pass


@pytest.mark.parametrize("browser", ["Chrome"], indirect=True)
def test_with_indirect_parametrization(browser):
    assert browser == "Chrome"


personal = pytest.mark.parametrize("account", ["personal"], indirect=True)


@personal
def test_with_account(account):
    pass




@dataclass
class User:
    id: int
    name: str
    age: int
    description: str

    # def __repr__(self):
    #     return f"{self.name} ({self.id})"


user1 = User(id=1, name="Mario", age=32, description="something " * 10)
user2 = User(id=2, name="Wario", age=62, description="else " * 10)


def show_user(user):
    return f"{user.name} ({user.id})"


@pytest.mark.parametrize("user", [user1, user2], ids=show_user)
def test_users(user):
    print()
