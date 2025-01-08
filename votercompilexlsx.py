import pandas as pd
from tkinter import Tk, filedialog
import os

# Function to extract column D and split Voter's Name into Surname and First Name
def process_voter_names(dataframe):
    try:
        # Ensure column D exists (index 3)
        if len(dataframe.columns) > 3:
            # Extract column D
            dataframe = dataframe.iloc[:, [3]].copy()
            dataframe.columns = ["Voter's Name"]

            # Ensure the "Voter's Name" column is of string type
            dataframe["Voter's Name"] = dataframe["Voter's Name"].astype(str)

            # Split into Surname and First Name
            split_names = dataframe["Voter's Name"].str.split(',', n=1, expand=True)
            dataframe['Surname'] = split_names[0]
            dataframe['First Name'] = split_names[1]

            # Drop the original "Voter's Name" column
            dataframe.drop(columns=["Voter's Name"], inplace=True)
        else:
            print("Warning: Column D not found. Skipping this file.")
    except Exception as e:
        print(f"Error processing 'Voter's Name': {e}")
    return dataframe

# Function to compile selected files into one Excel file
def compile_excel_files():
    # Open a file dialog to select multiple files
    Tk().withdraw()  # Hide the root window
    file_paths = filedialog.askopenfilenames(title="Select Excel Files to Compile", filetypes=[("Excel files", "*.xlsx")])

    # Check if files were selected
    if not file_paths:
        print("No files selected. Exiting.")
        return

    # Prompt for output file location
    output_filename = filedialog.asksaveasfilename(
        title="Save Compiled File As",
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")]
    )

    if not output_filename:
        print("No output file selected. Exiting.")
        return

    # Create a Pandas Excel writer
    with pd.ExcelWriter(output_filename, engine='xlsxwriter') as writer:
        for file_path in file_paths:
            # Extract the file name without extension for the sheet name
            sheet_name = os.path.basename(file_path).replace('.xlsx', '')

            try:
                # Read the first sheet of the current file
                excel_data = pd.ExcelFile(file_path)
                sheet_data = excel_data.parse(excel_data.sheet_names[0])

                # Process Voter's Name in column D
                processed_data = process_voter_names(sheet_data)

                # Write data to the corresponding sheet in the output file
                processed_data.to_excel(writer, sheet_name=sheet_name, index=False)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

    print(f"Compilation complete. Data saved to {output_filename}")

# Main execution
if __name__ == "__main__":
    compile_excel_files()
