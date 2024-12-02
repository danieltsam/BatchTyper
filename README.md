# BatchTyper

BatchTyper is a lightweight Python tool designed to streamline manual data entry. It automates the process of sequentially entering data into systems that only accept one item at a time. Whether you're inputting barcodes, usernames, or any other type of data, BatchTyper simplifies the workflow by letting you process batches with a single keypress.

## Features
- Automates sequential data entry for repetitive tasks.
- Configurable to process data in batches of any size.
- Pauses between batches, allowing you to trigger the next batch with a keypress.
- Works with any type of data requiring individual input.

## Use Cases
- Inputting barcodes into library or inventory systems.
- Manually entering data into legacy systems.
- Automating repetitive data entry tasks.

## Installation
>Install the required Python version (no additional libraries are needed).
1. Clone the repository:
   ```bash
   git clone https://github.com/danieltsam/batchtyper.git
2. Navigate to the directory:
    ```bash
    cd batchtyper
    

## Usage
Add all your data into the .py file into the string `import_data` delimited by a space e.g. `item1 item2 item3`. Alternatively, prepare your data in a text file, with each item delimited by a space and direct the import_data string to your text file.

Run the script:
```bash
python batchtyper.py
```

The script will input the first batch of data. Proceed to press Enter to process each batch sequentially. By default, there is a delay of **5 seconds** before the script begins inputting the items in a batch and a delay of 0.3 seconds between inputs of individual items to allow systems time to process the inputs.

### Example Input
Your input file should look like this:

`
item1 item2 item3 item4
`

### Example Console Output
```
Press Enter to start batch 1...
Batch 1 completed!
Press Enter to start batch 2...
Batch 2 completed!
Press Enter to start batch 3...
```
#### Customization
You can modify the script to:

- Change the batch size.
- Change the input delay.
- Adjust the input format.
