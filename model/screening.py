# -*- coding: utf-8 -*-
"""Build a real screening log from the four database exports."""
import csv, json, re, unicodedata, urllib.parse, urllib.request

UA = {"User-Agent": "SSB-audit/1.0 (mailto:ntnam.ddytcc23@ump.edu.vn)"}
def get(u):
    return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=45))

def norm(t):
    t = (t or "").lower().replace("đ", "d")
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()

records = []

# ---- PubMed (Viet Nam set, 2 records) -------------------------------------
records += [
 {"source": "PubMed", "year": 2023,
  "title": "Estimating the health impacts of sugar-sweetened beverage tax for informing policy decisions about the obesity burden in Vietnam",
  "doi": "10.1371/journal.pone.0274928"},
 {"source": "PubMed", "year": 1997,
  "title": "Current trends of sugar consumption in developing societies",
  "doi": "10.1111/j.1600-0528.1997.tb01735.x"},
]

# ---- Europe PMC (Viet Nam set, 3 records) ---------------------------------
q = ('(TITLE_ABS:"sugar-sweetened beverage" OR TITLE_ABS:"sugar sweetened beverage" '
     'OR TITLE_ABS:"sugary drink" OR TITLE_ABS:"soft drink" OR TITLE_ABS:"carbonated beverage" '
     'OR TITLE_ABS:soda) AND (TITLE_ABS:tax OR TITLE_ABS:taxation OR TITLE_ABS:excise '
     'OR TITLE_ABS:"fiscal policy") AND (TITLE_ABS:vietnam OR TITLE_ABS:"viet nam")')
u = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(
    {"query": q, "format": "json", "pageSize": 25})
for r in get(u)["resultList"]["result"]:
    records.append({"source": "Europe PMC", "year": int(r.get("pubYear") or 0),
                    "title": r.get("title", ""), "doi": r.get("doi", "")})

# ---- OpenAlex (Viet Nam set, 11 records) ----------------------------------
f = ('title_and_abstract.search:("sugar-sweetened beverage" OR "soft drink" OR soda) '
     'AND (tax OR taxation OR excise) AND (vietnam OR "viet nam")')
u = "https://api.openalex.org/works?" + urllib.parse.urlencode(
    {"filter": f, "per-page": 50, "mailto": "ntnam.ddytcc23@ump.edu.vn"})
for r in get(u)["results"]:
    records.append({"source": "OpenAlex", "year": r.get("publication_year") or 0,
                    "title": r.get("title", ""),
                    "doi": (r.get("doi") or "").replace("https://doi.org/", "")})

# ---- Scopus (user export, 6 records) --------------------------------------
for r in csv.DictReader(open("data/scopus_export.csv", encoding="utf-8-sig")):
    records.append({"source": "Scopus", "year": int(r["Year"] or 0),
                    "title": r["Title"], "doi": (r.get("DOI") or "").strip()})

# ---- de-duplicate ----------------------------------------------------------
seen_doi, seen_title, unique = {}, {}, []
for rec in records:
    d = rec["doi"].lower().strip()
    t = norm(rec["title"])
    if d and d in seen_doi:
        unique[seen_doi[d]]["sources"].add(rec["source"]); continue
    if t and t in seen_title:
        unique[seen_title[t]]["sources"].add(rec["source"]); continue
    rec = dict(rec); rec["sources"] = {rec["source"]}
    if d: seen_doi[d] = len(unique)
    if t: seen_title[t] = len(unique)
    unique.append(rec)

# ---- screening decisions ---------------------------------------------------
INCLUDE = {
 "estimating the health impacts of sugar sweetened beverage tax": "health-impact modelling of SSB tax scenarios in Viet Nam",
 "the impacts of alcoholic and non alcoholic beverage tax on different income groups": "distributional analysis of the 2025 excise design using VHLSS",
 "between commerce and conscience": "human-rights assessment of the enacted SSB excise tax",
 "public acceptability of policy interventions to reduce sugary drink consumption": "acceptability of SSB policies in urban Viet Nam",
 "impacts of excise taxation on non alcoholic beverage consumption": "empirical analysis of excise effects on beverage consumption",
 "the distributional impacts of health taxes": "distributional analysis of health taxes, including SSB, regional",
}
INCLUDE_VI = "thue tieu thu dac biet doi voi nuoc giai khat co duong"
EXCLUDE = {
 "current trends of sugar consumption": ("not about taxation", "dental review of sugar consumption trends"),
 "lyndon johnson and vietnam": ("wrong population", "unrelated historical record; false positive of the country term"),
 "building food smart cities": ("no SSB-tax estimate", "urban food systems, no beverage tax analysis"),
 "harmful marketing by commercial actors": ("no SSB-tax estimate", "food marketing to children, not taxation"),
}

rows = []
for rec in unique:
    t = norm(rec["title"])
    key = next((k for k in INCLUDE if t.startswith(k) or k in t), None)
    if key is None and INCLUDE_VI in t:
        key = INCLUDE_VI; INCLUDE[key] = "legal and theoretical analysis of the enacted tax"
    if key:
        dec, reason = "include", INCLUDE[key]
    else:
        k2 = next((k for k in EXCLUDE if k in t), None)
        dec, reason = ("exclude", EXCLUDE[k2][1]) if k2 else ("exclude", "not relevant after title/abstract screening")
    # a preprint of an included paper is a duplicate
    if "medrxiv" in rec["doi"].lower() or rec["doi"].startswith("10.1101/"):
        dec, reason = "exclude", "preprint duplicate of an included article"
    rows.append({"record": len(rows) + 1, "sources": "+".join(sorted(rec["sources"])),
                 "year": rec["year"], "title": rec["title"].replace("\n", " "),
                 "doi": rec["doi"], "decision": dec, "reason": reason})

with open("data/screening_log.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

n_total = len(records)
n_unique = len(unique)
n_inc = sum(1 for r in rows if r["decision"] == "include")
print(f"records identified      {n_total}")
print(f"after de-duplication    {n_unique}")
print(f"included                {n_inc}")
print(f"excluded                {n_unique - n_inc}")
print()
for r in rows:
    print(f"  [{r['decision'][:3]}] {r['year']} {r['sources']:28s} {r['title'][:70]}")
json.dump({"identified": n_total, "unique": n_unique, "included": n_inc},
          open("output/screening_counts.json", "w"), indent=2)
