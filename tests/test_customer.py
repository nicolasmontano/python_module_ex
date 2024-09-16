import pytest

from .conftest import dummy_customer


def test_customer_id_generation(dummy_customer):
    assert dummy_customer.id == "0001"


