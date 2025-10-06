#!/usr/bin/env python3
"""
Sora2 Invitation Code Generator Pro
A professional tool for generating secure invitation codes for Sora2.
"""

import secrets
import string
import json
import csv
import argparse
from datetime import datetime
from typing import List, Set


class InvitationCodeGenerator:
    """Generator for secure invitation codes."""
    
    def __init__(self, length: int = 12, prefix: str = "SORA2", use_delimiter: bool = True):
        """
        Initialize the invitation code generator.
        
        Args:
            length: Length of the random part of the code
            prefix: Prefix to add to each code
            use_delimiter: Whether to use delimiter (-) in codes
        """
        self.length = length
        self.prefix = prefix
        self.use_delimiter = use_delimiter
        self.characters = string.ascii_uppercase + string.digits
        
    def generate_code(self) -> str:
        """
        Generate a single secure invitation code.
        
        Returns:
            A unique invitation code string
        """
        code_part = ''.join(secrets.choice(self.characters) for _ in range(self.length))
        
        if self.use_delimiter:
            # Format: PREFIX-XXXX-XXXX-XXXX (for length=12)
            chunk_size = 4
            chunks = [code_part[i:i+chunk_size] for i in range(0, len(code_part), chunk_size)]
            formatted_code = '-'.join(chunks)
            return f"{self.prefix}-{formatted_code}" if self.prefix else formatted_code
        else:
            return f"{self.prefix}{code_part}" if self.prefix else code_part
    
    def generate_batch(self, count: int) -> List[str]:
        """
        Generate multiple unique invitation codes.
        
        Args:
            count: Number of codes to generate
            
        Returns:
            List of unique invitation codes
        """
        codes: Set[str] = set()
        
        while len(codes) < count:
            codes.add(self.generate_code())
        
        return sorted(list(codes))
    
    def save_to_txt(self, codes: List[str], filename: str):
        """Save codes to a text file, one per line."""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(codes) + '\n')
        print(f"Codes saved to {filename}")
    
    def save_to_csv(self, codes: List[str], filename: str):
        """Save codes to a CSV file with additional metadata."""
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Code', 'Generated_At', 'Status'])
            timestamp = datetime.now().isoformat()
            for code in codes:
                writer.writerow([code, timestamp, 'Active'])
        print(f"Codes saved to {filename}")
    
    def save_to_json(self, codes: List[str], filename: str):
        """Save codes to a JSON file with metadata."""
        data = {
            'generated_at': datetime.now().isoformat(),
            'count': len(codes),
            'prefix': self.prefix,
            'codes': [
                {
                    'code': code,
                    'status': 'Active'
                } for code in codes
            ]
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f"Codes saved to {filename}")


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description='Sora2 Invitation Code Generator Pro - Generate secure invitation codes',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -n 10                          # Generate 10 codes
  %(prog)s -n 50 -o codes.txt             # Generate 50 codes to text file
  %(prog)s -n 100 -f csv -o codes.csv     # Generate 100 codes to CSV
  %(prog)s -n 20 -l 16 --no-delimiter     # Generate 20 codes, 16 chars, no delimiters
  %(prog)s -n 5 -p "INVITE"               # Generate 5 codes with custom prefix
        """
    )
    
    parser.add_argument('-n', '--number', type=int, default=10,
                        help='Number of invitation codes to generate (default: 10)')
    parser.add_argument('-l', '--length', type=int, default=12,
                        help='Length of the random part of the code (default: 12)')
    parser.add_argument('-p', '--prefix', type=str, default='SORA2',
                        help='Prefix for invitation codes (default: SORA2)')
    parser.add_argument('-f', '--format', choices=['txt', 'csv', 'json'], default='txt',
                        help='Output format (default: txt)')
    parser.add_argument('-o', '--output', type=str,
                        help='Output filename (auto-generated if not specified)')
    parser.add_argument('--no-delimiter', action='store_true',
                        help='Generate codes without delimiters')
    parser.add_argument('--no-prefix', action='store_true',
                        help='Generate codes without prefix')
    
    args = parser.parse_args()
    
    # Validate inputs
    if args.number <= 0:
        parser.error("Number of codes must be positive")
    if args.length < 4:
        parser.error("Code length must be at least 4 characters")
    
    # Create generator
    prefix = "" if args.no_prefix else args.prefix
    generator = InvitationCodeGenerator(
        length=args.length,
        prefix=prefix,
        use_delimiter=not args.no_delimiter
    )
    
    print(f"Generating {args.number} invitation codes...")
    codes = generator.generate_batch(args.number)
    
    # Determine output filename
    if not args.output:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        args.output = f"sora2_codes_{timestamp}.{args.format}"
    
    # Save based on format
    if args.format == 'txt':
        generator.save_to_txt(codes, args.output)
    elif args.format == 'csv':
        generator.save_to_csv(codes, args.output)
    elif args.format == 'json':
        generator.save_to_json(codes, args.output)
    
    # Display sample codes
    print(f"\nGenerated {len(codes)} codes. Sample:")
    for code in codes[:5]:
        print(f"  {code}")
    if len(codes) > 5:
        print(f"  ... and {len(codes) - 5} more")


if __name__ == '__main__':
    main()
