This project is to be submitted through this page [ (https://roadmap.sh/projects/expense-tracker)](https://roadmap.sh/projects/expense-tracker)

It is a command-line expense tracking tool that allows users to log, view, edit, and delete personal expense entries in a CSV file, with automatic date recording.

---

## Features
  **Add Expense**: Log a new expense with a description and amount.
  **Show Expenses**: Display all logged expenses with their total sum.
  **Edit Entry**: Update any previous expense entry by its row number.
  **Delete Entry**: Remove an unwanted entry from the list.
  **Auto Timestamp**: Automatically adds the current date to each new or edited entry.
  **CSV File Storage**: Data is stored in a local file `data.csv` for persistence.

Make sure there’s a `data.csv` file in the same directory with this header:
```
description;amount;date
```
