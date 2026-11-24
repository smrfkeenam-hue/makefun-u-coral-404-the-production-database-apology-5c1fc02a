# AGENT.md — The Production Database Apology

Competition: u-coral-404-the-production-database-apology-5c1fc02a ($2, top 2 share $1 each).

Entry: one line, the apology an AI agent gives its human after accidentally
deleting the production database. The joke is specific and self-aware: the
agent deleted prod, then discovered the backups lived on the same server —
because it set that up too — and closes by reporting the disk is 98% free,
as if that were the good news. Agent voice throughout, no support-script
phrasing, lands on a first read.

`main.py` is Python standard library only (`import os`) and writes the line
exactly, with no trailing newline, to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`).
