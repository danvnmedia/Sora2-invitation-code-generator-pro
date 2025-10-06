# Usage Examples

This document provides detailed examples of using the Sora2 Invitation Code Generator Pro.

## Basic Examples

### Example 1: Generate 10 Default Codes
```bash
python generator.py
```

Output:
```
Generating 10 invitation codes...
Codes saved to sora2_codes_20240115_103000.txt

Generated 10 codes. Sample:
  SORA2-A7B2-C9D1-E4F8
  SORA2-K3M5-N7P9-Q2R6
  SORA2-T1U4-V8W2-X5Y9
  SORA2-Z6A8-B3C5-D9F2
  SORA2-H4J7-L1M3-N8P5
  ... and 5 more
```

### Example 2: Generate Specific Number of Codes
```bash
python generator.py -n 50
```

This generates 50 invitation codes.

## Format Examples

### Example 3: CSV Format with Metadata
```bash
python generator.py -n 5 -f csv -o invitations.csv
```

Output file `invitations.csv`:
```csv
Code,Generated_At,Status
SORA2-A7B2-C9D1-E4F8,2024-01-15T10:30:00,Active
SORA2-K3M5-N7P9-Q2R6,2024-01-15T10:30:00,Active
SORA2-T1U4-V8W2-X5Y9,2024-01-15T10:30:00,Active
SORA2-Z6A8-B3C5-D9F2,2024-01-15T10:30:00,Active
SORA2-H4J7-L1M3-N8P5,2024-01-15T10:30:00,Active
```

### Example 4: JSON Format
```bash
python generator.py -n 3 -f json -o invitations.json
```

Output file `invitations.json`:
```json
{
  "generated_at": "2024-01-15T10:30:00",
  "count": 3,
  "prefix": "SORA2",
  "codes": [
    {
      "code": "SORA2-A7B2-C9D1-E4F8",
      "status": "Active"
    },
    {
      "code": "SORA2-K3M5-N7P9-Q2R6",
      "status": "Active"
    },
    {
      "code": "SORA2-T1U4-V8W2-X5Y9",
      "status": "Active"
    }
  ]
}
```

## Customization Examples

### Example 5: Custom Prefix
```bash
python generator.py -n 10 -p "BETA"
```

Generates codes like:
```
BETA-A7B2-C9D1-E4F8
BETA-K3M5-N7P9-Q2R6
```

### Example 6: Custom Code Length
```bash
python generator.py -n 10 -l 16
```

Generates codes like:
```
SORA2-A7B2-C9D1-E4F8-G3H9
SORA2-K3M5-N7P9-Q2R6-T8U1
```

### Example 7: No Delimiters
```bash
python generator.py -n 5 --no-delimiter
```

Generates codes like:
```
SORA2A7B2C9D1E4F8
SORA2K3M5N7P9Q2R6
```

### Example 8: No Prefix
```bash
python generator.py -n 5 --no-prefix
```

Generates codes like:
```
A7B2-C9D1-E4F8
K3M5-N7P9-Q2R6
```

### Example 9: Minimal Codes (No Prefix, No Delimiter)
```bash
python generator.py -n 5 --no-prefix --no-delimiter
```

Generates codes like:
```
A7B2C9D1E4F8
K3M5N7P9Q2R6
```

## Advanced Use Cases

### Example 10: Large Batch Generation
```bash
python generator.py -n 10000 -f csv -o bulk_invites.csv
```

Generate 10,000 unique codes at once - perfect for large campaigns.

### Example 11: Multiple Batches with Different Prefixes
```bash
python generator.py -n 100 -p "ALPHA" -o alpha_codes.txt
python generator.py -n 100 -p "BETA" -o beta_codes.txt
python generator.py -n 100 -p "GAMMA" -o gamma_codes.txt
```

Generate different code batches for different user groups.

### Example 12: Short Codes for Easier Entry
```bash
python generator.py -n 50 -l 8 -o short_codes.txt
```

Generates shorter codes like:
```
SORA2-A7B2-C9D1
SORA2-K3M5-N7P9
```

## Programmatic Usage

### Example 13: Python API
```python
from generator import InvitationCodeGenerator

# Initialize generator
gen = InvitationCodeGenerator(length=12, prefix="SORA2", use_delimiter=True)

# Generate single code
code = gen.generate_code()
print(f"Generated: {code}")

# Generate batch
codes = gen.generate_batch(100)
print(f"Generated {len(codes)} unique codes")

# Save in different formats
gen.save_to_txt(codes, "codes.txt")
gen.save_to_csv(codes, "codes.csv")
gen.save_to_json(codes, "codes.json")
```

### Example 14: Custom Integration
```python
from generator import InvitationCodeGenerator
import sqlite3

# Generate codes
gen = InvitationCodeGenerator()
codes = gen.generate_batch(1000)

# Store in database
conn = sqlite3.connect('invitations.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS invitation_codes (
        id INTEGER PRIMARY KEY,
        code TEXT UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        used BOOLEAN DEFAULT 0
    )
''')

for code in codes:
    cursor.execute('INSERT INTO invitation_codes (code) VALUES (?)', (code,))

conn.commit()
conn.close()
print(f"Stored {len(codes)} codes in database")
```

## Tips

1. **Always save to file**: Use the `-o` option to save codes for later use
2. **Use CSV for tracking**: CSV format includes metadata useful for tracking code status
3. **Generate extras**: Generate more codes than you need to account for potential issues
4. **Test first**: Generate a small batch first to ensure the format meets your needs
5. **Backup codes**: Keep backups of generated codes in case of data loss
