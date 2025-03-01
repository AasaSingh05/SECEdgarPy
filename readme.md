# SECEdgar-Python

A simple library to interact with and retrieve information from the SEC Edgar Data.

## Dependencies:

- OS
- pandas
- requests
- bs4

## Installation

To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

## Functions

### `CIKExtractor() -> list`
Extracts the CIK for S&P 500 companies from Wikipedia.

**Usage:**
```python
from SECedgarpyExtractor import CIKExtractor
cik_list = CIKExtractor()
print(cik_list)
```

**Concepts Used:**
- Web scraping using `requests` and `BeautifulSoup`
- Error handling for HTTP requests

### `GetAllSP500CSV()`
Gets all the S&P 500 info in the form of a CSV.

**Usage:**
```python
from SECedgarpyExtractor import GetAllSP500CSV
GetAllSP500CSV()
```

**Concepts Used:**
- Web scraping using `pandas`
- Saving data to CSV

### `getCSVfile(URLlist: list[str], nameOfFile: str) -> None`
Downloads the XLSX file from the list of URLs and converts them to CSV.

**Usage:**
```python
from SECedgarpyDownloading import getCSVfile
getCSVfile(["url1", "url2"], "output_file")
```

**Concepts Used:**
- HTTP requests
- File handling
- Data conversion using `pandas`

### `getXLSXfile(URLlist: list[str], nameOfFile: str) -> None`
Downloads the XLSX file from the list of URLs.

**Usage:**
```python
from SECedgarpyDownloading import getXLSXfile
getXLSXfile(["url1", "url2"], "output_file")
```

**Concepts Used:**
- HTTP requests
- File handling

### `GenerateCSVreport(nameOfFile)`
Generates a CSV report by filtering and keeping the necessary sheets only.

**Usage:**
```python
from SECedgarpyDownloading import GenerateCSVreport
GenerateCSVreport("input_file")
```

**Concepts Used:**
- Data filtering
- Data merging using `pandas`

### `download_and_convert_filtered_xlsx(URLlist: list[str], nameOfFile: str, target_sheets: list[str]) -> None`
Downloads and converts filtered XLSX files to CSV.

**Usage:**
```python
from SECedgarpyDownloading import download_and_convert_filtered_xlsx
download_and_convert_filtered_xlsx(["url1", "url2"], "output_file", ["sheet1", "sheet2"])
```

**Concepts Used:**
- HTTP requests
- Data filtering
- Data conversion using `pandas`

### `filter_and_convert_to_csv(xlsx_file_path: str, csv_file_path: str, target_sheets: list[str]) -> None`
Filters relevant sheets and converts them to CSV.

**Usage:**
```python
from SECedgarpyDownloading import filter_and_convert_to_csv
filter_and_convert_to_csv("input.xlsx", "output.csv", ["sheet1", "sheet2"])
```

**Concepts Used:**
- Data filtering
- Data conversion using `pandas`

### `filterfunc(a: list) -> bool`
Filters out and gets only the 10-K reports.

**Usage:**
```python
from SECedgarpyProcessing import filterfunc
filtered_list = filter(filterfunc, data_list)
```

**Concepts Used:**
- Data filtering using custom functions

### `extract10Kurl(cikval: str) -> list`
Extracts the URL using the CIK which is passed into the function.

**Usage:**
```python
from SECedgarpyProcessing import extract10Kurl
urls = extract10Kurl("0000320193")
print(urls)
```

**Concepts Used:**
- API requests
- Data extraction and transformation

### `URLtoXLSX(URLlist: list[str]) -> list`
Converts the URL to direct XLSX files.

**Usage:**
```python
from SECedgarpyProcessing import URLtoXLSX
xlsx_urls = URLtoXLSX(["url1", "url2"])
print(xlsx_urls)
```

**Concepts Used:**
- URL manipulation
