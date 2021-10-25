import argparse
import pandas as pd

def create_csv(excel_file_path: str, country_name: str) -> str:

    excel_data = pd.read_excel(excel_file_path, sheet_name="Data", na_values=[".."])

    series_names    = excel_data["Series Name"].unique() 
    columns_to_drop = ["Series Name", "Series Code", "Country Name", "Country Code"]

    country_data  = excel_data[excel_data["Country Name"] == country_name]
    required_data = {"Years" : [year for year in range(1990, 2021)]}

    for series_name in series_names:
        try:
            required_data[series_name] = country_data[
                country_data["Series Name"] == series_name
            ].drop(columns_to_drop, axis=1).to_numpy().tolist()[0]
        except:
            pass 

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
