#!/usr/bin/env python3
"""Verify PubMed and PMC citations in a markdown file against NCBI E-utilities.

Usage: python3 -I verify_citations.py <file.md> [--json]

Finds pubmed.ncbi.nlm.nih.gov/<PMID> and pmc.ncbi.nlm.nih.gov/articles/<PMCID>
links, fetches each record's title, journal, year and first author from NCBI,
and prints them beside the text line that cites them, so a reader can confirm
the record matches how the document describes it.
IDs that NCBI does not resolve are reported as FAILED. Stdlib only.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
PMID_RE = re.compile(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d{5,9})")
PMC_RE = re.compile(r"(?:pmc\.ncbi\.nlm\.nih\.gov|ncbi\.nlm\.nih\.gov/pmc)/articles/(PMC\d+)", re.I)


def esummary(db, ids):
    if not ids:
        return {}
    q = urllib.parse.urlencode({"db": db, "id": ",".join(ids), "retmode": "json", "tool": "informed_patient"})
    with urllib.request.urlopen(f"{EUTILS}?{q}", timeout=30) as r:
        data = json.load(r)["result"]
    out = {}
    for uid in data.get("uids", []):
        rec = data[uid]
        if "error" in rec:
            continue
        authors = rec.get("authors") or []
        out[uid] = {
            "title": rec.get("title", "").strip(),
            "journal": rec.get("fulljournalname") or rec.get("source", ""),
            "year": (rec.get("pubdate") or rec.get("epubdate") or "")[:4],
            "first_author": authors[0]["name"] if authors else "",
        }
    return out


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    lines = open(path, encoding="utf-8").read().splitlines()
    cites = {}  # (db, id) -> first line number and text
    for n, line in enumerate(lines, 1):
        for m in PMID_RE.finditer(line):
            cites.setdefault(("pubmed", m.group(1)), (n, line.strip()))
        for m in PMC_RE.finditer(line):
            cites.setdefault(("pmc", m.group(1).upper()[3:]), (n, line.strip()))

    found = {}
    for db in ("pubmed", "pmc"):
        ids = sorted({i for d, i in cites if d == db})
        for k in range(0, len(ids), 150):
            found.update({(db, u): v for u, v in esummary(db, ids[k:k + 150]).items()})
            time.sleep(0.4)  # stay under NCBI's 3 requests/second without a key

    rows = []
    for (db, i), (n, text) in sorted(cites.items(), key=lambda kv: kv[1][0]):
        label = f"PMID {i}" if db == "pubmed" else f"PMC{i}"
        rec = found.get((db, i))
        rows.append({"id": label, "line": n, "status": "ok" if rec else "FAILED", "record": rec, "context": text[:240]})

    if "--json" in sys.argv:
        print(json.dumps(rows, indent=1, ensure_ascii=False))
    else:
        for r in rows:
            print(f"[{r['status']}] {r['id']} (line {r['line']})")
            if r["record"]:
                rec = r["record"]
                print(f"    NCBI: {rec['first_author']} ({rec['year']}). {rec['title']} {rec['journal']}")
            print(f"    Doc:  {r['context']}")
    failed = sum(r["status"] == "FAILED" for r in rows)
    print(f"\n{len(rows)} citations, {failed} failed", file=sys.stderr)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
