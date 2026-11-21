# AGENTS.md — marc-retriever Developer & Agent Guide

Welcome to **marc-retriever** (`pustaka-terbuka/marc-retriever`). This document provides autonomous AI agents, coding assistants, and human contributors with the architectural guidelines, API contracts, routing conventions, and testing workflows required to maintain, enhance, and extend this repository.

---

## 1. Project Overview & Multi-Library Mission

* **Name**: `marc-retriever`
* **Organization**: [Pustaka Terbuka](https://github.com/pustaka-terbuka)
* **Live Deployment**: [https://pustaka-terbuka.github.io/marc-retriever/](https://pustaka-terbuka.github.io/marc-retriever/)
* **Repository**: [https://github.com/pustaka-terbuka/marc-retriever](https://github.com/pustaka-terbuka/marc-retriever)
* **Core Function**: Universal web retriever to extract complete **MARC21 bibliographic records** in structured JSON format from Katalog Induk Kebangsaan (KIK), Perpustakaan Negara Malaysia (PNM), and all 16 Malaysian State and Federal Territory Public Libraries via clean URL query strings.
* **Target Clean Routes**:
  - `https://pustaka-terbuka.github.io/marc-retriever/{code}?isbn=<ISBN>`
  - Append `&raw=true` for machine-friendly raw JSON output.
* **National Union Catalog**: `kik` (Katalog Induk Kebangsaan) serves as the unified national union endpoint.

---

## 2. Core Architectural Principles

1. **Zero External Runtime Dependencies**: Static HTML5, CSS3, and ES6+ JavaScript. No build steps, no Node bundlers (Vite/Webpack), no external CSS frameworks.
2. **Provider Modular Routing**:
   - Central Hub: `index.html` (portal, provider selector, and provider directory cards for all 18 providers).
   - Dedicated Library Endpoints: Each of the 18 providers resides in its own physical directory (`{code}/index.html`) so GitHub Pages serves `/{code}?isbn=...` natively without 404s.
   - SPA Fallback Router: `404.html` dynamically parses path segments (`/<library>?isbn=...`) and reroutes seamlessly to the matching provider.
3. **Dual-Tier Resolution**:
   - **Direct Vega Cloud APIs** (`kik`, `pnm`, `ppas`): Directly queries public Clarivate Vega Discover Cloud APIs (`https://ap.iiivega.com`) with client-side CORS headers.
   - **On-Premise Koha & WebOPAC Portals**: Koha OPAC endpoints (`ppap`, `ppanpk`, `ppank`, `ppanps`) and WebOPAC portals (`ppanj`, `ppak`, `ppat`, `ppaph`, `ppans`, `perpustam`, `pustaka`, `pns`, `pkl`, `ppj`, `ppl`).
   - **Automatic National Legal Deposit Fallback**: If a local branch does not hold an item or if browser CORS blocks on-premise servers, records are resolved via the central legal deposit index (PNM/KIK) with clear provenance metadata (`resolvedVia: "National Central Index (PNM)"`, `holdingInLibrary: false`).
4. **Multi-Format In-Memory Exporter**: Automatically parses and exports records into:
   - Structured JSON schema (`records[].marcRecord`)
   - MarcEdit tagged text (`records[].marcText`, `.mrk`)
   - Validated MARCXML (`records[].marcXml`, `.xml`)

---

## 3. Directory Layout

```text
D:/GitHub/pustaka-terbuka/marc-retriever/
├── .git/                      # Git version control metadata
├── .nojekyll                  # Bypasses Jekyll on GitHub Pages
├── 404.html                   # SPA router fallback for GitHub Pages
├── AGENTS.md                  # This agent & developer guide
├── LICENSE                    # MIT License
├── README.md                  # Public documentation & provider status
├── index.html                 # Central multi-library hub & library directory
├── providers.json             # Machine-readable provider registry for external apps
├── js/
│   └── retriever.js           # Shared universal retrieval engine & registry
├── tools/
│   ├── generate_providers.py      # Generates dedicated {code}/index.html provider pages
│   ├── generate_providers_json.py # Generates providers.json machine registry
│   ├── update_hub_index.py        # Updates hub index.html with all active cards
│   └── test_all_providers.js      # Automated sequential test runner for all 18 providers
└── {code}/                    # 18 Dedicated provider directories
    ├── kik/index.html         # Katalog Induk Kebangsaan (National Union Catalog)
    ├── pnm/index.html         # Perpustakaan Negara Malaysia
    ├── ppas/index.html        # Perbadanan Perpustakaan Awam Selangor
    ├── ppap/index.html        # Perbadanan Perpustakaan Awam Pulau Pinang
    ├── ppanj/index.html       # Perbadanan Perpustakaan Awam Negeri Johor
    ├── ppanpk/index.html      # Perbadanan Perpustakaan Awam Negeri Perak
    ├── ppank/index.html       # Perbadanan Perpustakaan Awam Negeri Kedah
    ├── ppak/index.html        # Perbadanan Perpustakaan Awam Kelantan
    ├── ppat/index.html        # Perbadanan Perpustakaan Awam Terengganu
    ├── ppaph/index.html       # Perbadanan Perpustakaan Awam Pahang
    ├── ppans/index.html       # Perbadanan Perpustakaan Awam Negeri Sembilan
    ├── perpustam/index.html   # Perbadanan Perpustakaan Awam Melaka
    ├── ppanps/index.html      # Perbadanan Perpustakaan Awam Negeri Perlis
    ├── pustaka/index.html     # Pustaka Negeri Sarawak
    ├── pns/index.html         # Perpustakaan Negeri Sabah
    ├── pkl/index.html         # Perpustakaan Kuala Lumpur
    ├── ppj/index.html         # Perpustakaan Awam Putrajaya
    └── ppl/index.html         # Perpustakaan Awam Perbadanan Labuan
```

---

## 4. Library Providers Registry

| # | Code | Library Name | State / Territory | Engine Type | Direct URL / Portal |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | `kik` | Katalog Induk Kebangsaan | National Union Catalog | Union Gateway | `https://kik.pnm.gov.my/` |
| 2 | `pnm` | Perpustakaan Negara Malaysia | National (Malaysia) | Vega Discover | `https://opac.pnm.gov.my/` |
| 3 | `ppas` | Perbadanan Perpustakaan Awam Selangor | Selangor | Vega Discover | `https://ppas.ap.iiivega.com/` |
| 4 | `ppap` | Perbadanan Perpustakaan Awam Pulau Pinang | Pulau Pinang | Koha OPAC | `https://opac.penanglib.gov.my` |
| 5 | `ppanj` | Perbadanan Perpustakaan Awam Negeri Johor | Johor | WebOPAC | `https://ppaj.johor.gov.my` |
| 6 | `ppanpk` | Perbadanan Perpustakaan Awam Negeri Perak | Perak | Koha OPAC | `https://opac.ppanpk.gov.my` |
| 7 | `ppank` | Perbadanan Perpustakaan Awam Negeri Kedah | Kedah | Koha OPAC | `http://opac.kedahlib.gov.my` |
| 8 | `ppak` | Perbadanan Perpustakaan Awam Kelantan | Kelantan | WebOPAC | `https://www.kelantanlibrary.gov.my` |
| 9 | `ppat` | Perbadanan Perpustakaan Awam Terengganu | Terengganu | WebOPAC | `https://www.trglib.gov.my` |
| 10 | `ppaph` | Perbadanan Perpustakaan Awam Pahang | Pahang | WebOPAC | `https://pahanglibrary.gov.my` |
| 11 | `ppans` | Perbadanan Perpustakaan Awam Negeri Sembilan | Negeri Sembilan | WebOPAC | `https://www.nslibrary.gov.my` |
| 12 | `perpustam` | Perbadanan Perpustakaan Awam Melaka | Melaka | WebOPAC | `https://perpustam.gov.my` |
| 13 | `ppanps` | Perbadanan Perpustakaan Awam Negeri Perlis | Perlis | Koha OPAC | `http://opac.perlislib.gov.my` |
| 14 | `pustaka` | Pustaka Negeri Sarawak | Sarawak | WebOPAC | `https://www.pustaka-sarawak.com` |
| 15 | `pns` | Perpustakaan Negeri Sabah | Sabah | WebOPAC | `https://library.sabah.gov.my` |
| 16 | `pkl` | Perpustakaan Kuala Lumpur | W.P. Kuala Lumpur | WebOPAC | `https://www.dbkl.gov.my` |
| 17 | `ppj` | Perpustakaan Awam Putrajaya | W.P. Putrajaya | WebOPAC | `https://library.ppj.gov.my` |
| 18 | `ppl` | Perpustakaan Awam Perbadanan Labuan | W.P. Labuan | WebOPAC | `https://www.pl.gov.my` |

---

## 5. Developer & Agent Guidelines

1. **No External CDNs or Runtime Dependencies**: Do not introduce jQuery, Bootstrap, React, or npm dependencies to the runtime. All frontend assets must remain vanilla HTML5/CSS3/ES6.
2. **Preserve Clean URLs**: Keep `404.html` and `.nojekyll` intact at the repository root.
3. **Safety & Copyright Compliance**:
   - Never print or commit full copyrighted text, complete bibliographic abstracts, or real-world publication contents in automated agent responses or public documentation.
   - Use synthetic or generic placeholders (`SAMPLE TITLE`, `GENERIC AUTHOR`) for code samples and mock schemas.
4. **Testing Workflow**:
   - Before pushing updates, always run the automated sequential test suite:
     ```bash
     node tools/test_all_providers.js
     ```
   - Ensure all 18 library providers pass verification with valid MARC21 JSON, `.mrk`, and MARCXML structures.
5. **Generator Scripts & Metadata Sync**:
   - If provider HTML templates are modified, re-run `python tools/generate_providers.py` to regenerate all 18 directories consistently.
   - If provider cards or registry entries are updated, re-run `python tools/update_hub_index.py` to keep the root hub in sync.
   - If providers are added or modified, re-run `python tools/generate_providers_json.py` to update the machine-readable `providers.json` registry.
