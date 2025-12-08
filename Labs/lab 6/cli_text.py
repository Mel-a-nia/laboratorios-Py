import argparse
import sys
from pathlib import Path

def cat_command(input_file, number_lines=False):
    try:
        input_path = Path(input_file)
        if not input_path.exists():
            print(f"Error: File '{input_file}' not found")
            return False
            
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for i, line in enumerate(lines, 1):
            if number_lines:
                print(f"{i:6}  {line.rstrip()}")
            else:
                print(line.rstrip())
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

def stats_command(input_file, top=5):
    try:
        input_path = Path(input_file)
        if not input_path.exists():
            print(f"Error: File '{input_file}' not found")
            return False
            
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()
            
        words = text.lower().split()
        word_count = {}
        
        for word in words:
            clean_word = ''.join(c for c in word if c.isalnum())
            if clean_word and len(clean_word) > 2:
                word_count[clean_word] = word_count.get(clean_word, 0) + 1
        
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        
        print(f"Top {top} most frequent words in '{input_file}':")
        print("-" * 40)
        for i, (word, count) in enumerate(sorted_words[:top], 1):
            print(f"{i:2}. {word:<15} {count:>3} times")
            
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="CLI tools for text processing")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    cat_parser = subparsers.add_parser("cat", help="Display file content")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Number lines")
    
    stats_parser = subparsers.add_parser("stats", help="Word frequency statistics")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)
    
    args = parser.parse_args()
    
    if args.command == "cat":
        success = cat_command(args.input, args.n)
    elif args.command == "stats":
        success = stats_command(args.input, args.top)
    else:
        print("Command not recognized")
        success = False
        
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()