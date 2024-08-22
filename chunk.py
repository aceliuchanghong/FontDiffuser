import re
import time
import psutil
import sys

# Define variables for magic numbers
MAX_HEADING_LENGTH = 7
MAX_HEADING_CONTENT_LENGTH = 200
MAX_HEADING_UNDERLINE_LENGTH = 200
MAX_HTML_HEADING_ATTRIBUTES_LENGTH = 100
MAX_LIST_ITEM_LENGTH = 200
MAX_NESTED_LIST_ITEMS = 6
MAX_LIST_INDENT_SPACES = 7
MAX_BLOCKQUOTE_LINE_LENGTH = 200
MAX_BLOCKQUOTE_LINES = 15
MAX_CODE_BLOCK_LENGTH = 1500
MAX_CODE_LANGUAGE_LENGTH = 20
MAX_INDENTED_CODE_LINES = 20
MAX_TABLE_CELL_LENGTH = 200
MAX_TABLE_ROWS = 20
MAX_HTML_TABLE_LENGTH = 2000
MIN_HORIZONTAL_RULE_LENGTH = 3
MAX_SENTENCE_LENGTH = 400
MAX_QUOTED_TEXT_LENGTH = 300
MAX_PARENTHETICAL_CONTENT_LENGTH = 200
MAX_NESTED_PARENTHESES = 5
MAX_MATH_INLINE_LENGTH = 100
MAX_MATH_BLOCK_LENGTH = 500
MAX_PARAGRAPH_LENGTH = 1000
MAX_STANDALONE_LINE_LENGTH = 800
MAX_HTML_TAG_ATTRIBUTES_LENGTH = 100
MAX_HTML_TAG_CONTENT_LENGTH = 1000
LOOKAHEAD_RANGE = 100

AVOID_AT_START = r"[\s\]})>,']"
PUNCTUATION = r"[.!?…]|\.\.\.|[\u2026\u2047-\u2049]"
QUOTE_END = r"(?:'(?=\`)|''(?=\`\`))"
SENTENCE_END = f"(?:{PUNCTUATION}(?!{AVOID_AT_START}(?={PUNCTUATION}))|{QUOTE_END})(?=\S|$)"
SENTENCE_BOUNDARY = f"(?:{SENTENCE_END}|(?=[\r\n]|$))"
LOOKAHEAD_PATTERN = f"(?:(?!{SENTENCE_END}).){{1,{LOOKAHEAD_RANGE}}}{SENTENCE_END}"
NOT_PUNCTUATION_SPACE = f"(?!{PUNCTUATION}\s)"
SENTENCE_PATTERN = f"{NOT_PUNCTUATION_SPACE}(?:[^\r\n]{{1,{MAX_SENTENCE_LENGTH}}}{SENTENCE_BOUNDARY}|[^\r\n]{{1,{MAX_SENTENCE_LENGTH}}}(?={PUNCTUATION}|{QUOTE_END})(?:{LOOKAHEAD_PATTERN})?){AVOID_AT_START}*"

regex = re.compile(
    r"("
    # 1. Headings
    f"(?:^(?:[#*=-]{{1,{MAX_HEADING_LENGTH}}}|\w[^\r\n]{{0,{MAX_HEADING_CONTENT_LENGTH}}}\r?\n[-=]{{2,{MAX_HEADING_UNDERLINE_LENGTH}}}|<h[1-6][^>]{{0,{MAX_HTML_HEADING_ATTRIBUTES_LENGTH}}}>)[^\r\n]{{1,{MAX_HEADING_CONTENT_LENGTH}}}(?:</h[1-6]>)?(?:\r?\n|$))"
    "|"
    # 2. List items
    f"(?:(?:^|\r?\n)[ \t]{{0,3}}(?:[-*+•]|\d{{1,3}}\.\w\.|\[ [xX]\])[ \t]+{SENTENCE_PATTERN})"
    "|"
    # 3. Block quotes
    f"(?:(?:^>(?:>|\\s{{2,}}){{0,2}}{SENTENCE_PATTERN})\r?\n?{{1,{MAX_BLOCKQUOTE_LINES}}})"
    "|"
    # 4. Code blocks
    f"(?:(?:^|\r?\n)(?:```|~~~)(?:\w{{0,{MAX_CODE_LANGUAGE_LENGTH}}})?\r?\n[\s\S]{{0,{MAX_CODE_BLOCK_LENGTH}}}?(?:```|~~~)\r?\n?)"
    "|"
    # 5. Tables
    f"(?:(?:^|\r?\n)(?:\|[^\r\n]{{0,{MAX_TABLE_CELL_LENGTH}}}\|(?:\r?\n\|[-:]{{1,{MAX_TABLE_CELL_LENGTH}}}\|){{0,1}}(?:\r?\n\|[^\r\n]{{0,{MAX_TABLE_CELL_LENGTH}}}\|){{0,{MAX_TABLE_ROWS}}})"
    "|"
    # 6. Horizontal rules
    f"(?:^(?:[-*_]){{{MIN_HORIZONTAL_RULE_LENGTH},}}\s*$|<hr\s*/?>)"
    "|"
    # 7. Sentences or phrases
    f"{SENTENCE_PATTERN}"
    "|"
    # 8. Quoted text, parenthetical phrases
    r"(?:(?<!\w)\"\"\"[^\"]{0,300}\"\"\"(?!\w))"
    "|"
    # 9. Paragraphs
    f"(?:^|\r?\n\r?\n)(?:<p>)?{SENTENCE_PATTERN}(?:</p>)?(?=\r?\n\r?\n|$)"
    "|"
    # 10. Standalone lines or phrases
    f"(?!{AVOID_AT_START})(?:^(?:<[a-zA-Z][^>]{{0,{MAX_HTML_TAG_ATTRIBUTES_LENGTH}}}>)?{SENTENCE_PATTERN}(?:</[a-zA-Z]+>)?(?:\r?\n|$))"
    ")",
    re.MULTILINE | re.UNICODE
)

def format_bytes(bytes):
    if bytes < 1024:
        return f"{bytes} bytes"
    elif bytes < 1048576:
        return f"{bytes / 1024:.2f} KB"
    elif bytes < 1073741824:
        return f"{bytes / 1048576:.2f} MB"
    else:
        return f"{bytes / 1073741824:.2f} GB"

# Read the input file
with open(sys.argv[1], 'r', encoding='utf-8') as file:
    test_text = file.read()

# Start measuring time and memory
start_time = time.time()
start_memory = psutil.Process().memory_info().rss

# Apply the regex
matches = regex.findall(test_text)

# End measuring time and memory
end_time = time.time()
end_memory = psutil.Process().memory_info().rss

# Calculate execution time and memory usage
execution_time = end_time - start_time
memory_used = end_memory - start_memory

# Output results
print(f"Number of chunks: {len(matches)}")
print(f"Execution time: {execution_time:.3f} seconds")
print(f"Memory used: {format_bytes(memory_used)}")

# Output the first 10 matches (or fewer if there are less than 10)
print("\nFirst 10 chunks:")
for i, match in enumerate(matches[:10]):
    print(f"Chunk {i + 1}: {repr(match)}")

# Output regex flags
print(f"\nRegex flags: {regex.flags}")

# Check for potential issues
if execution_time > 5:
    print("\nWarning: Execution time exceeded 5 seconds. The regex might be too complex or the input too large.")
if memory_used > 100 * 1024 * 1024:
    print("\nWarning: Memory usage exceeded 100 MB. Consider processing the input in smaller chunks.")
