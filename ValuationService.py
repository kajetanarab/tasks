import pandas as panda
import config


# getting top products by total price limited by top priced count
def get_top_products(merged, matchings):
    result = panda.DataFrame()
    for row in range(len(matchings)):
        # get matching id and top priced count from matchings.csv
        matching_id = matchings.values[row][0]
        top_priced_count = matchings.values[row][1]
        # temp DF with data from merged DF sorted by total price
        temp = merged[merged['matching_id'] == matching_id].sort_values(by='total_price', ascending=False)
        # calculate ignored products count
        temp['ignored_products_count'] = (temp.shape[0]) - top_priced_count
        temp = temp.head(top_priced_count)
        result = result.append(temp)
    return result


def aggregate_products(result, matchings):
    aggregated = panda.DataFrame()
    # for every matching id
    for row in range(len(matchings)):
        matching_id = (matchings.values[row][0])
        #selct all rows for matching id
        temp = result.loc[result['matching_id'] == matching_id]
        # calculate sum of prices and quantity get total price and average
        list_prices = temp['total_price'].to_list()
        list_quantity = temp['quantity']
        prices_sum = sum(list_prices)
        quantity_sum = sum(list_quantity)
        # insert calculated values to DataFrame
        temp["total_price"] = temp.apply(lambda row: prices_sum, axis=1)
        temp["avg_price"] = temp.apply(lambda row: (prices_sum / quantity_sum), axis=1)
        # get only firs row and remove unnecessary duplications
        temp = temp.iloc[0]
        aggregated = aggregated.append(temp)
    return aggregated


# preparing final form of data frame
def prepare_final(aggregated):
    final = panda.DataFrame()
    # inserting columns to new DataFrame
    final.insert(0, "matching_id", aggregated['matching_id'])
    final.insert(1, "total_price", aggregated['total_price'])
    final.insert(2, "avg_price", aggregated['avg_price'])
    final.insert(3, "currency", aggregated['currency'])
    final.insert(4, "ignored_products_count", aggregated['ignored_products_count'])
    return final


def save_to_file(final):
    final.to_csv(config.PATH_FOR_SAVING, index=False)


def load_data():
    return panda.read_csv(config.PATH_DATA_FILE)


def load_currencies():
    return panda.read_csv(config.PATH_CURRENCIES_FILE)


def load_matchings():
    return panda.read_csv(config.PATH_MATCHINGS_FILE)


def main():
    # load files as pandas DataFrames
    data = load_data()
    currencies = load_currencies()
    matchings = load_matchings()

    # merge currencies and data for calculations
    merged = panda.merge(data, currencies)

    # calculate total_price in pln and add to data frame
    merged["total_price"] = merged.apply(lambda row: float(row.price * row.quantity * row.ratio), axis=1)
    # switching currency to PLN as it is already calculated to PLN
    merged["currency"] = merged.apply(lambda row: 'PLN', axis=1)
    top_products = get_top_products(merged, matchings)
    aggregated = aggregate_products(top_products, matchings)
    final = prepare_final(aggregated)
    save_to_file(final)


if __name__ == "__main__":
    main()
