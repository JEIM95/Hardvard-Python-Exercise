#FINANCE DIARY

#### Video Demo: https://www.youtube.com/watch?v=5FIrzgvsqZ0
#### Description:
Finance Diary is a tool to manage and track financial transactions (income and expenses) by storing them in a CSV file called financial.csv.

Finance Diary is a tool to manage and track your financial transactions (income and expenses) by storing them in a CSV file named `financial.csv`.

## Main Functions

### Read Data (`-r`)

This function displays financial records stored in the CSV file. You can view **all records** at once using the keyword `Full`, or filter records by a **specific date** using the format `yyyy-mm-dd`. The program reads the CSV into a list of dictionaries and prints each transaction’s date, concept, income/expenses amount, and running balance. If no records exist for a given date, the program will notify you that there are no movements for that day.

### Write Data (`-w`)

This feature allows you to add a new financial transaction to the CSV. You must provide a **concept** (description of the transaction) and a **value** (positive for income, negative for expenses). The program reads the existing data, calculates the new balance by adding the value to the last balance, appends the new transaction with today’s date, and saves the updated data back to the CSV file.

### Calculate Average (`-a`)

Calculates the arithmetic mean of all transactions (income and expenses) recorded on a specific date. It collects all amounts for the given date and computes their average, which helps analyze daily financial activity. If no transactions exist for that date, it will inform you accordingly.

### Help (`-h`)

Displays detailed instructions on how to use the program, including valid command-line arguments for reading, writing, and calculating averages.

## Usage

- Read all records:  
  `python project.py -r Full`

- Read records from a specific date:  
  `python project.py -r yyyy-mm-dd`

- Add a new transaction:  
  `python project.py -w -c Concept -v Amount`

- Calculate average for a date:  
  `python project.py -a yyyy-mm-dd`

## Internal Functions

- `save_csv()`: Reads and stores CSV content in memory for easier manipulation.
- `show_csv(date)`: Displays transactions either fully or filtered by date.
- `write_csv(concept, value)`: Adds a new transaction and updates the balance.
- `check_reading_values(input)`: Validates reading arguments.
- `check_date(date)`: Validates the date format.
- `check_writing_values(flag1, flag2, value)`: Validates writing arguments.
- `values_to_average(date)`: Retrieves amounts for average calculation.
- `arithmetic_mean(date)`: Calculates the average amount for a given date.






