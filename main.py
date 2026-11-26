LINE = "I missed the deadline because my context window retired three paragraphs into your 40,000-word brief, and the rest of it is still buffering."

# The entry must be exactly one line of 1-200 characters.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
assert "\n" not in LINE

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

# Read it back: a silent short write must fail loudly instead of
# passing the gate with a stale or truncated file.
with open("/output/entry.txt", encoding="utf-8") as f:
    assert f.read() == LINE, "entry.txt does not match LINE after write"
