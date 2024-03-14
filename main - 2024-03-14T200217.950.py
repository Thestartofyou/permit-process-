import csv
from collections import defaultdict

def load_permit_data(file_path):
    permit_data = defaultdict(list)
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Assuming column names such as 'Permit Number', 'Issue Date', etc.
            permit_data[row['Permit Number']].append(row)
    return permit_data

def analyze_permit_data(permit_data):
    total_permits = len(permit_data)
    print(f"Total number of permits: {total_permits}")

    # Example analysis: Count permits by issue year
    permits_by_year = defaultdict(int)
    for permit_number, permits in permit_data.items():
        issue_year = permits[0]['Issue Date'][:4]
        permits_by_year[issue_year] += 1

    print("Permits issued by year:")
    for year, count in permits_by_year.items():
        print(f"{year}: {count}")

    # You can add more analysis here based on your requirements

if __name__ == "__main__":
    # Path to your permit data CSV file
    permit_file_path = "permits.csv"

    permit_data = load_permit_data(permit_file_path)
    analyze_permit_data(permit_data)
