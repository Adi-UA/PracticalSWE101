# Homework Assignment 3

## Objective

Now that you've learned about modules, import statements, JSON handling, web requests, and HTTP status codes, let's put that knowledge into practice by writing a Python program that retrieves UniProt entry data using the UniProt REST API. Once again, this is also your mini assignment, so don't read the code section unless you want spoilers!

UniProt is a comprehensive resource for protein sequence and annotation data. The UniProt REST API allows users to retrieve UniProt entry data in various formats, including JSON. The API endpoint for retrieving UniProt entry data is `https://rest.uniprot.org/uniprotkb/{entry_id}`. You can specify the format of the data using the `format` query parameter.

You don't need to understand what the UniProt REST API does or how it works. You only need to know that you can retrieve UniProt entry data in JSON format by sending an HTTP GET request to the API endpoint with the UniProt entry ID and the desired format. You can read more about what UniProt is here: [UniProt](https://en.wikipedia.org/wiki/UniProt).

### Task

You are required to write a Python program that accomplishes the following tasks:

1. Create a function `get_uniprot_entry(entry_id)` that takes a UniProt entry ID as input and returns the UniProt entry data in JSON format. The function should handle HTTP requests using the `requests` module.

2. Define a function `main()` that performs the following steps:

   - Change the working directory to the directory of the script using the `os` module. Or use the absolute path to accomplish the same thing!
   - Read a list of UniProt entry IDs from a file named `input_ids.txt`. Ensure the file is properly read and each entry ID is stripped of leading/trailing whitespace.
   - For each entry ID in the list, call the `get_uniprot_entry()` function to retrieve the entry data.
   - If the data is successfully retrieved, save it to a JSON file named after the entry ID using the `json` module's `dump()` function with proper formatting (lookup what the `indent` argument to this function does!). One file should be created for each entry ID.
   - Print appropriate messages indicating whether the data retrieval and saving were successful.

3. Remember to call the `main()` function at the end of your script to execute the program. Otherwise `python your_script.py` will not run the code in the `main()` function.
