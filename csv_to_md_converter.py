import os
import pandas as pd
from pathlib import Path

def convert_csv_to_md(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Get the output filename (same name but .md extension)
    output_file = Path(csv_file).with_suffix('.md')
    
    # Open the output file for writing
    with open(output_file, 'w', encoding='utf-8') as f:
        # Process each row
        for _, row in df.iterrows():
            # Write the section header (first column)
            f.write(f"## {row[0]}\n\n")
            
            # Create a table with the remaining columns
            f.write("| Name | Code | Category Code | Category Name |\n")
            f.write("|------|------|---------------|---------------|\n")
            
            # Write the data row
            f.write(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |\n\n")

def main():
    # Directory containing the CSV files
    csv_dir = "dpm_regulatory_views"
    
    # Process each CSV file in the directory
    for file in os.listdir(csv_dir):
        if file.endswith('.csv'):
            csv_path = os.path.join(csv_dir, file)
            print(f"Converting {file} to markdown...")
            convert_csv_to_md(csv_path)
            print(f"Successfully converted {file}")

if __name__ == "__main__":
    main() 