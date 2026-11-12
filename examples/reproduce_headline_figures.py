#!/usr/bin/env python3
"""Recompute, from data/prices.csv alone, the headline figures Telehealth Ledger
published for this snapshot: for each treatment, how many providers publish a
calendar-month continuing price, and the lowest, highest and median of those prices.

Rule used (it reproduces the published figures for the 2026-11-12 snapshot):
  - keep rows whose priceRole is "continuing-monthly"
  - take each provider's lowest comparisonPriceUsd for the treatment
  - report count, min, max and median across providers

Standard library only. Run from the repository root:
    python3 examples/reproduce_headline_figures.py
"""
import csv
import statistics
from collections import defaultdict
from pathlib import Path

rows = list(csv.DictReader(open(Path(__file__).resolve().parent.parent / "data" / "prices.csv", newline="")))

lowest = defaultdict(dict)  # treatment -> provider slug -> lowest continuing monthly price
labels = {}
for r in rows:
    if r["priceRole"] != "continuing-monthly":
        continue
    price = float(r["comparisonPriceUsd"])
    t, p = r["treatment"], r["slug"]
    labels[t] = r["treatmentLabel"]
    if p not in lowest[t] or price < lowest[t][p]:
        lowest[t][p] = price

print(f"{'treatment':42} {'providers':>9} {'low':>8} {'median':>8} {'high':>8}")
for t in sorted(lowest, key=lambda k: -len(lowest[k])):
    v = sorted(lowest[t].values())
    print(f"{labels[t][:42]:42} {len(v):>9} {v[0]:>8.0f} {statistics.median(v):>8.0f} {v[-1]:>8.0f}")

dates = sorted(r["verifiedAt"] for r in rows)
print(f"\n{len(rows)} rows, {len({r['slug'] for r in rows})} providers, checked {dates[0]} to {dates[-1]}.")
print("A row is a dated reading of a page the provider publishes, not a quote.")
