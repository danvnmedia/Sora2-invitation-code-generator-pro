# Sora2 Invitation Code Generator Pro

A professional, secure invitation code generator for Sora2. Generate unique, cryptographically secure invitation codes with customizable formats and export options.

## Features

- 🔐 **Cryptographically Secure**: Uses Python's `secrets` module for secure random generation
- 📦 **Batch Generation**: Generate thousands of unique codes at once
- 🎨 **Customizable Format**: Configure code length, prefix, and delimiters
- 💾 **Multiple Export Formats**: Export to TXT, CSV, or JSON
- ✅ **Duplicate Prevention**: Ensures all generated codes are unique
- 🚀 **CLI Interface**: Easy-to-use command-line interface

## Installation

### Requirements
- Python 3.6 or higher

### Setup
1. Clone the repository:
```bash
git clone https://github.com/danvnmedia/Sora2-invitation-code-generator-pro.git
cd Sora2-invitation-code-generator-pro
```

2. Make the script executable (optional):
```bash
chmod +x generator.py
```

## Usage

### Basic Usage

Generate 10 invitation codes (default):
```bash
python generator.py
```

Generate a specific number of codes:
```bash
python generator.py -n 50
```

### Advanced Options

```bash
python generator.py [OPTIONS]
```

#### Options:
- `-n, --number N`: Number of codes to generate (default: 10)
- `-l, --length L`: Length of the random part (default: 12)
- `-p, --prefix PREFIX`: Custom prefix (default: SORA2)
- `-f, --format FORMAT`: Output format: txt, csv, or json (default: txt)
- `-o, --output FILE`: Output filename (auto-generated if not specified)
- `--no-delimiter`: Generate codes without delimiters
- `--no-prefix`: Generate codes without prefix

### Examples

Generate 100 codes and save to a text file:
```bash
python generator.py -n 100 -o invites.txt
```

Generate 50 codes in CSV format with metadata:
```bash
python generator.py -n 50 -f csv -o invites.csv
```

Generate 20 codes in JSON format:
```bash
python generator.py -n 20 -f json -o invites.json
```

Generate codes with custom length (16 characters):
```bash
python generator.py -n 10 -l 16
```

Generate codes with custom prefix:
```bash
python generator.py -n 10 -p "INVITE"
```

Generate codes without delimiters:
```bash
python generator.py -n 10 --no-delimiter
```

Generate codes without prefix:
```bash
python generator.py -n 10 --no-prefix
```

## Code Format

### Default Format
```
SORA2-XXXX-XXXX-XXXX
```

Example codes:
```
SORA2-A7B2-C9D1-E4F8
SORA2-K3M5-N7P9-Q2R6
SORA2-T1U4-V8W2-X5Y9
```

### Without Delimiters
```
SORA2XXXXXXXXXXXX
```

### Without Prefix
```
XXXX-XXXX-XXXX
```

## Output Formats

### TXT Format
Simple text file with one code per line:
```
SORA2-A7B2-C9D1-E4F8
SORA2-K3M5-N7P9-Q2R6
SORA2-T1U4-V8W2-X5Y9
```

### CSV Format
CSV file with metadata:
```csv
Code,Generated_At,Status
SORA2-A7B2-C9D1-E4F8,2024-01-15T10:30:00,Active
SORA2-K3M5-N7P9-Q2R6,2024-01-15T10:30:00,Active
```

### JSON Format
JSON file with structured data:
```json
{
  "generated_at": "2024-01-15T10:30:00",
  "count": 3,
  "prefix": "SORA2",
  "codes": [
    {
      "code": "SORA2-A7B2-C9D1-E4F8",
      "status": "Active"
    }
  ]
}
```

## Use Cases

- 🎯 **Beta Testing**: Generate invitation codes for beta testers
- 🎁 **Promotional Campaigns**: Create unique promo codes
- 🔑 **Access Control**: Generate one-time access codes
- 👥 **User Registration**: Control user registration with invite-only system
- 🎪 **Event Management**: Generate event access codes

## Security

- Uses `secrets` module for cryptographically strong random generation
- All codes are uppercase alphanumeric (A-Z, 0-9) for clarity
- Automatic duplicate detection ensures uniqueness
- No ambiguous characters (configurable if needed)

## API Usage

You can also use the generator programmatically:

```python
from generator import InvitationCodeGenerator

# Create generator
gen = InvitationCodeGenerator(length=12, prefix="SORA2", use_delimiter=True)

# Generate a single code
code = gen.generate_code()
print(code)  # SORA2-A7B2-C9D1-E4F8

# Generate multiple codes
codes = gen.generate_batch(100)

# Save to files
gen.save_to_txt(codes, "codes.txt")
gen.save_to_csv(codes, "codes.csv")
gen.save_to_json(codes, "codes.json")
```

## License

MIT License - Feel free to use this in your projects!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.