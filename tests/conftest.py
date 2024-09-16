from pytest import  fixture
from ecommerce.ecommerce import  Customer


@fixture()
def dummy_customer():
    return Customer('nicolas','montano')
