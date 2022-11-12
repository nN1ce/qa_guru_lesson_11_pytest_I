import os

import pytest
import time


@pytest.fixture()
def browser():
    """Мой браузер"""
    time.sleep(1)


@pytest.mark.slow
def test_first(browser):
    time.sleep(1)


@pytest.mark.fast
def test_second():
    time.sleep(1)


@pytest.mark.fast
@pytest.mark.skip(reason="TASK-123 Тест нестабильный потому что тестовые данные приходят неверные")
def test_third():
    a = 25
    b = 150
    assert a == b


@pytest.mark.skipif("os.getenv('OS') == 'Linux'", reason="Something")
def test_skipped(browser):
    if os.getenv("OS") == "linux":
        pytest.skip("reason")
    if browser == 'Safari':
        pytest.skip("Safari doesn't supported")


@pytest.mark.xfail(reason="some reason")
def test_xfailed():
    assert False
    time.sleep(5)
    try:
        assert 1 == 5
    except AssertionError:
        pytest.xfail()


@pytest.mark.usefixtures("browser")
def test_with_browser():
    pass
