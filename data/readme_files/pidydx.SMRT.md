# Sublime Malware Research Tool
This is a Plugin for Sublime Text 3 to provide a number of commonly used tools related to malware analysis and research.  The original version for Sublime Text 2 can be found in the SublimeText2 branch, but it is unlikely development will continue on that branch.

## Installation
Recommended installation is to git clone into the Packages directory of Sublime Text 3

## Prerequisites
You must have libmagic installed or SMRT will fail to load.

Examples:

OSX (using Homebrew): `brew install libmagic`

Windows: https://github.com/pidydx/libmagicwin64

## Current Commands
- SMRT: Int To Unix Timestamp 
- SMRT: UTF-8 To Base64
- SMRT: UTF-8 To Base32
- SMRT: Base64 To UTF-8
- SMRT: Base32 To UTF-8
- SMRT: Rot13 Encode
- SMRT: RotX Encode (Prompts for integer distance to rotate text)
- SMRT: Swap Char (Prompts for substitution map in Xx:Yy format)
- SMRT: UTF-8 To MD5
- SMRT: UTF-8 To SHA1
- SMRT: UTF-8 To SHA256
- SMRT: Hex To Int 
- SMRT: Int To Hex
- SMRT: Byte Format Hex
- SMRT: Word Format Hex
- SMRT: DWord Format Hex
- SMRT: Base64 Encode Binary
- SMRT: Base64 Decode Binary
- SMRT: ASCII To Hex
- SMRT: UTF-8 To Hex
- SMRT: UTF-16 To Hex
- SMRT: Hex To ASCII
- SMRT: Hex To UTF-8
- SMRT: Hex To UTF-16
- SMRT: Binary To Hex (Expects string of 1's and 0's)
- SMRT: Hex to Binary 
- SMRT: Zlib Decompress Hex
- SMRT: Zlib Compress Hex
- SMRT: Gzip Decompress Hex
- SMRT: Gzip Compress Hex
- SMRT: INFLATE Decompress Hex
- SMRT: DEFLATE Compress Hex
- SMRT: URL Quote
- SMRT: URL Unquote
- SMRT: NBO Int To IP
- SMRT: HBO Int To IP
- SMRT: IP To NBO Int
- SMRT: IP To HBO Int
- SMRT: Switch Endianness (Expects Hex Text)
- SMRT: PE Scanner (Expects Hex Text)
- SMRT: Find PE (Expects Hex Text)
- SMRT: Brute XOR Find PE (Expects Hex Text. This can take some time and Sublime will appear to be unresponsive while running)
- SMRT: Apply XOR (Prompts for hex key or range. Examples: FF, 00-FF, DEAD, 0000-FFFF)
- SMRT: Apply XOR Skip Zero and Key (Prompts for hex key or range. Examples: FF, 00-FF, DEAD, 0000-FFFF)
- SMRT: Int to Alpha (Converts 1->A, 2->B, 3->C, etc. Expects ints 1-26 separated by spaces)
- SMRT: Alpha to Int (Converts Aa->1, Bb->2, Cc->3, etc. Expects upper/lower alpha a-z)
- SMRT: Code Point to Unicode (Expects code point representation. Examples: U+XXXX, %uXXXX, \uXXXX)
- SMRT: Unicode to Code Point
- SMRT: Hex Bitwise ROL (Prompts for number of bytes to include in rotation and number of bits to rotatein x,y format)
- SMRT: Hex Bitwise ROR (Prompts for number of bytes to include in rotation and number of bits to rotatein x,y format)

## Coming Soon

- Custom BaseXX Encode/Decodes
- Bit Operations (NEG,INV)
- Mail Extraction
- Strings on PE
- Mach-o, ELF features
