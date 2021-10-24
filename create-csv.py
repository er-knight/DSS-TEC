import argparse
import pandas as pd

def create_csv(excel_file_path: str, country_name: str) -> str:

    required_series_names = [
        "Population growth (annual %)",
        "CO2 emissions (metric tons per capita)",
        "GDP growth (annual %)",  
        "Inflation, GDP deflator (annual %)",  
        "Industry (including construction), value added (% of GDP)",  
        "Exports of goods and services (% of GDP)",  
        "Imports of goods and services (% of GDP)",  
        "Gross capital formation (% of GDP)",  
        "Inflation, consumer prices (annual %)"
    ]

    columns_to_drop = ["Series Name", "Series Code", "Country Name", "Country Code"]

    excel_data    = pd.read_excel(excel_file_path, sheet_name="Data", na_values=[".."])
    country_data  = excel_data[excel_data["Country Name"] == country_name]
    required_data = {"Years" : [year for year in range(1990, 2021)]}

    for series_name in required_series_names:
        required_data[series_name] = country_data[
            country_data["Series Name"] == series_name
        ].drop(columns_to_drop, axis=1).to_numpy().tolist()[0]

    country_name = "-".join([name.lower() for name in country_name.split()])

    pd.DataFrame(required_data).to_csv(f"popular-indicators-{country_name}.csv", index=False)

    print(f"saved to popular-indicators-{country_name}.csv")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("excel_file_path", type=str)
    parser.add_argument("country_name", type=str)

    args = parser.parse_args()

    excel_file_path = args.excel_file_path
    country_name    = " ".join([name.title() for name in args.country_name.split()])

    create_csv(excel_file_path, country_name)

# python3 create-csv.py <path-of-excel-file> <name-of-the-country>
