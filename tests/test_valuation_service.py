import pandas as panda
import pandas.api.types as types
import datatest
import pytest

from ValuationService import get_top_products, prepare_final, aggregate_products


def test_columns_type(currencies, matchings, data):
    datatest.validate(currencies.columns, {'currency', 'ratio'})
    datatest.validate(matchings.columns, {'matching_id', 'top_priced_count'})
    datatest.validate(data.columns, {'id', 'price', 'currency', 'quantity', 'matching_id'})


def test_currency(currencies, data):
    assert (types.is_string_dtype(currencies['currency']))
    assert (types.is_string_dtype(data['currency']))


def test_ratio(currencies):
    assert (types.is_float_dtype(currencies['ratio']))


def test_matching_id(matchings, data):
    assert (types.is_integer_dtype(matchings['matching_id']))
    assert (types.is_integer_dtype(data['matching_id']))


def test_top_priced_count(matchings):
    assert (types.is_integer_dtype(matchings['top_priced_count']))


def test_price(data):
    assert (types.is_integer_dtype(data['price']))


def test_quantity(data):
    assert (types.is_integer_dtype(data['quantity']))


def test_incorrect_paths():
    with pytest.raises(FileNotFoundError):
        currencies = panda.read_csv("../" + "wrong path to file")


def test_top_products(test_data_merged, test_data_matchings, test_data_expected):
    final = get_top_products(test_data_merged, test_data_matchings)
    assert all(final == test_data_expected)


def test_prepare_final(test_data_final, test_data_expected_final):
    final_df = prepare_final(test_data_final)
    assert all(final_df == test_data_expected_final)


def test_aggregate(test_data_aggregate, test_data_aggregate_matchings, test_data_expected_aggregate):
    matchings = test_data_aggregate_matchings
    to_be_aggregated = test_data_aggregate
    assert all(aggregate_products(to_be_aggregated, matchings) == test_data_expected_aggregate)


