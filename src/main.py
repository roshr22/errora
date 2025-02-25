import argparse
from gemini_api import analyze_error
from utils import read_file

def main():
    parser = argparse.ArgumentParser(description="Errora - Error Analysis CLI")
    parser.add_argument("--file", type=str, required=True, help="Path to the code file")
    parser.add_argument("--error", type=str, required=True, help="Error message to analyze")

    args = parser.parse_args()

    code_content = read_file(args.file)
    if code_content.startswith("Error"):
        print(code_content)
        return

    print("\n🔎 Analyzing error...\n")
    analysis = analyze_error(code_content, args.error)
    print(f"💡 Analysis:\n{analysis}\n")

if __name__ == "__main__":
    main()
