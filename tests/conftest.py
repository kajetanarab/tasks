import pytest
import pandas as panda
import config


@pytest.fixture(scope='module')
def currencies():
    return panda.read_csv("../" + config.PATH_CURRENCIES_FILE)


@pytest.fixture(scope='module')
def matchings():
    return panda.read_csv("../" + config.PATH_MATCHINGS_FILE)


@pytest.fixture(scope='module')
def data():
    return panda.read_csv("../" + config.PATH_DATA_FILE)


@pytest.fixture(scope='module')
def test_data_merged():
    data_merged = {'matching_id': [3, 3, 1], 'total_price': [999, 1, 1]}
    merged_df = panda.DataFrame(data_merged)
    return merged_df


@pytest.fixture(scope='module')
def test_data_matchings():
    data_match = {'matching_id': [3], 'top_priced_count': [1]}
    matchings_df = panda.DataFrame(data_match)
    return matchings_df


@pytest.fixture(scope='module')
def test_data_expected():
    data_expected = {'matching_id': [3], 'total_price': [999], 'ignored_products_count': [1]}
    expected_top_df = panda.DataFrame(data_expected)
    return expected_top_df


@pytest.fixture(scope='module')
def test_data_final():
    data_final = {'total_price':[99], 'matching_id':[1], 'avg_price':[10], 'currency':['USD'], 'ignored_products_count':[0]}
    data_final = panda.DataFrame(data_final)
    return data_final


@pytest.fixture(scope='module')
def test_data_expected_final():
    data_expected = {'matching_id':[1], 'total_price':[99], 'avg_price':[10], 'currency':['USD'], 'ignored_products_count':[0]}
    data_expected_final = panda.DataFrame(data_expected)
    return data_expected_final


@pytest.fixture(scope='module')
def test_data_aggregate_matchings():
    fake_matchings = {'matching_id':[2]}
    fake_matchings_df = panda.DataFrame(fake_matchings)
    return fake_matchings_df


@pytest.fixture(scope='module')
def test_data_aggregate():
    data_aggregate = {'matching_id': [2, 2, 1], 'total_price': [6, 4, 100], 'quantity': [2, 2, 100]}
    data_aggregate_df = panda.DataFrame(data_aggregate)
    return data_aggregate_df


@pytest.fixture(scope='module')
def test_data_expected_aggregate():
    expected_aggregated = {'matching_id':[2], 'total_price':[10], 'quantity':[4], 'avg_price':[2.5]}
    expected_aggregated_df = panda.DataFrame(expected_aggregated)
    return expected_aggregated_df