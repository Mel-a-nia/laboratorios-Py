import argparse
import json
import csv
import sys

def main():
    parser = argparse.ArgumentParser(description="Data format converters")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    p1 = subparsers.add_parser("json2csv", help="Convert JSON to CSV")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)
    
    p2 = subparsers.add_parser("csv2json", help="Convert CSV to JSON") 
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)
    
    p3 = subparsers.add_parser("csv2xlsx", help="Convert CSV to XLSX")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)
          
          
    args = parser.parse_args()
    
    if args.command == "json2csv":
        with open(args.input, 'r') as f:
            data = json.load(f)
        with open(args.output, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"Converted {args.input} to {args.output}")
        
    elif args.command == "csv2json":
        data = []
        with open(args.input, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        with open(args.output, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Converted {args.input} to {args.output}")
        
    elif args.command == "csv2xlsx":
        print("CSV to XLSX requires openpyxl library")
        print("Run: pip install openpyxl")

if __name__ == "__main__":
    main()