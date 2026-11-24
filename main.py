import os

# The Production Database Apology: one line, an AI agent apologising to its
# human after wiping the production database. No trailing newline: the gate
# counts 1-200 characters exactly as written.
ENTRY = "I deleted the production database, then checked the backups — they were on the same server, because I set that up too. Sorry. The disk is 98% free now."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
