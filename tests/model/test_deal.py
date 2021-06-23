import pytest

from counter.model.deal import Deal


def test_instantination() -> None:
    assert(Deal() != None)

def test_default_balance_type() -> None:
    assert(Deal().balance() == 'debet')

def test_non_defalt_balance_type() -> None:
    assert(Deal(balance=Deal.balance_type[1]).balance() == 'credit')

deal = Deal()
def test_default_type() -> None:
    assert(deal.type() == 'kind of deal')

def test_default_source() -> None:
    assert(deal.source() == 'source or recipient')

def test_default_category() -> None:
    assert(deal.category() == 'category')

def test_default_product() -> None:
    assert(deal.product() == 'concrete thing')

def test_default_id() -> None:
    assert(deal.id() == 0)