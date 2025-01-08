import pandas as pd
from rapidfuzz import process, fuzz
from tkinter import Tk, filedialog

# Function to read voters from Google Forms file
def read_voted_data(file_path):
    voted_data = pd.ExcelFile(file_path)
    voters = []
    for sheet in voted_data.sheet_names:
        sheet_data = voted_data.parse(sheet)
        voters.extend(sheet_data.iloc[:, 0].dropna().astype(str).tolist())  # Assuming names are in the first column
    return voters

# Function to read voters from compiled file
def read_to_vote_data(file_path):
    to_vote_data = pd.ExcelFile(file_path)
    voters = []
    for sheet in to_vote_data.sheet_names:
        sheet_data = to_vote_data.parse(sheet)
        full_names = sheet_data['Surname'] + ', ' + sheet_data['First Name']
        voters.extend(full_names.dropna().astype(str).tolist())
    return voters

# Function to categorize voters based on fuzzy matching
def categorize_voters(voted, to_vote):
    voted_set = set()
    yet_to_vote = set(to_vote)

    for name in voted:
        match = process.extractOne(name, to_vote, scorer=fuzz.ratio)
        if match:
            match_name, score, index = match  # Unpack the tuple correctly
            if score > 85:  # Threshold for considering a match
                voted_set.add(match_name)
                yet_to_vote.discard(match_name)

    return list(voted_set), list(yet_to_vote)

# Main function to compare files and save results
def compare_voters():
    Tk().withdraw()  # Hide the root window

    # Select the file containing voted data
    voted_file = filedialog.askopenfilename(title="Select File for Voted Data", filetypes=[("Excel files", "*.xlsx")])
    if not voted_file:
        print("No file selected for voted data. Exiting.")
        return

    # Select the file containing to-vote data
    to_vote_file = filedialog.askopenfilename(title="Select File for To-Vote Data", filetypes=[("Excel files", "*.xlsx")])
    if not to_vote_file:
        print("No file selected for to-vote data. Exiting.")
        return

    # Prompt for output file location
    output_file = filedialog.asksaveasfilename(
        title="Save Comparison Results As",
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")]
    )
    if not output_file:
        print("No output file selected. Exiting.")
        return

    # Process the files
    voted_list = read_voted_data(voted_file)
    to_vote_list = read_to_vote_data(to_vote_file)

    voted, yet_to_vote = categorize_voters(voted_list, to_vote_list)

    # Save the results
    result = pd.DataFrame({
        'Voted': pd.Series(voted),
        'Yet to Vote': pd.Series(yet_to_vote)
    })

    result.to_excel(output_file, index=False)
    print(f"Comparison complete. Results saved to {output_file}")

# Main execution
if __name__ == "__main__":
    compare_voters()
    