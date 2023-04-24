from kpis.temporalityFilter import get_period_filter

def test_period_filter() -> None:
    period_types = ["today", "month", "trimester", "year"]

    for period_type in period_types:
        try:
            start_date, end_date = get_period_filter(period_type)
            print(f"Period: {period_type}\nStart date: {start_date}\nEnd date: {end_date}\n")
        except ValueError as error:
            print(f"Invalid period type: {error}\n")

from kpis.temporalityFilter import load_csv, check_csv_has_created_at_column, get_period_filter, filter_csv_with_period

if __name__ == "__main__":
    # Test load_csv function
    data = load_csv("./data/orders.csv")
    print(f"Number of rows in original data: {len(data)}")

    # Test check_csv_has_created_at_column function
    has_created_at = check_csv_has_created_at_column(data)
    print(has_created_at)

    # Test get_period_filter function
    period_type = "trimester"
    date_range = get_period_filter(period_type)
    print(date_range)

    # Test filter_csv_with_period function
    filtered_data = filter_csv_with_period(data, date_range)
    print(f"Number of rows in filtered data: {len(filtered_data)}")
