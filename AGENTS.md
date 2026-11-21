# AGENTS.md — marc-retriever Developer & Agent Guide

Welcome to **marc-retriever** (`pustaka-terbuka/marc-retriever`). This document provides autonomous AI agents, coding assistants, and human contributors with the architectural guidelines, API contracts, routing conventions, and testing workflows required to maintain, enhance, and extend this repository.

---

## 1. Project Overview & Multi-Library Mission

* **Name**: `marc-retriever`
* **Organization**: [Pustaka Terbuka](https://github.com/pustaka-terbuka)
* **Live Deployment**: [https://pustaka-terbuka.github.io/marc-retriever/](https://pustaka-terbuka.github.io/marc-retriever/)
* **Repository**: [https://github.com/pustaka-terbuka/marc-retriever](https://github.com/pustaka-terbuka/marc-retriever)
* **Core Function**: Universal web retriever to extract complete **MARC21 bibliographic records** in structured JSON format from Perpustakaan Negara Malaysia (PNM) and Malaysian State Public Libraries via clean URL query strings.
* **Primary Target Route**:
  `https://pustaka-terbuka.github.io/marc-retriever/pnm?isbn=<ISBN>`

---

## 2. Core Architectural Principles

1. **Zero External Dependencies**: Static HTML5, CSS3, and ES6+ JavaScript. No build steps, no Node bundlers (Vite/Webpack), no external CSS frameworks.
2. **Provider Modular Routing**:
   - Central Hub: `index.html` (portal and library picker).
   - Dedicated Library Endpoints: Each provider resides in its own directory (e.g. `pnm/index.html`) so GitHub Pages serves `/pnm?isbn=...` natively.
   - SPA Fallback: `404.html` dynamically parses path segments (`/<library>?isbn=...`) and routes to the matching provider.
3. **Direct Client-Side CORS**: The client browser fetches records directly from library API gateways that support CORS without intermediate proxy servers.
4. **Query String Driven**: Any route accepting `?isbn=<ISBN>` automatically executes retrieval on page load. Appending `&raw=true` outputs pure unstyled JSON.

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
└── pnm/
    └── index.html             # Dedicated PNM retriever endpoint (/pnm?isbn=...)
```

---

## 4. Library Providers Roadmap

| Provider Code | Institution | System Architecture | Status |
| :--- | :--- | :--- | :--- |
| **`pnm`** | **Perpustakaan Negara Malaysia** | Vega Discover API (`ap.iiivega.com`) | 🟢 **Active** |
| **`ppas`** | Perbadanan Perpustakaan Awam Selangor | Koha REST API / SRU | 🟡 Planned |
| **`ppap`** | Perbadanan Perpustakaan Awam P. Pinang | Koha / ILMU | 🟡 Planned |
| **`pustaka`** | Pustaka Negeri Sarawak | Virtua / Chamo / Koha | 🟡 Planned |

---

## 5. PNM Provider Specification (`pnm/index.html`)

### 5.1 Endpoint Contract
* **URL**: `https://pustaka-terbuka.github.io/marc-retriever/pnm?isbn=<ISBN>`
* **Raw JSON**: `https://pustaka-terbuka.github.io/marc-retriever/pnm?isbn=<ISBN>&raw=true`

### 5.2 Retrieval Pipeline
1. **Search**: `POST https://ap.iiivega.com/api/search-result/search/format-groups`
   - Headers: `api-version: 2`, `iii-customer-domain: pnm.ap.iiivega.com`, `iii-host-domain: opac.pnm.gov.my`, dynamic `Anonymous-User-Id` UUID v4.
   - Body: `{"searchText": "<cleaned-isbn>"}`
2. **MARC Fetch**: `GET https://ap.iiivega.com/api/search-result/editions/{editionId}`
   - Headers: `api-version: 1`, `iii-customer-domain: pnm.ap.iiivega.com`, `iii-host-domain: opac.pnm.gov.my`.
   - Returns full MARC21 object (`leader`, `controlFields`, `dataFields`).

---

## 6. Testing & Deployment Workflow

### Local Preview
```powershell
cd D:\GitHub\pustaka-terbuka\marc-retriever
python -m http.server 8000
```
Test endpoints:
* Hub: `http://localhost:8000/`
* PNM Provider: `http://localhost:8000/pnm/?isbn=9789831665541`
* Raw JSON: `http://localhost:8000/pnm/?isbn=9789831665541&raw=true`

### Deploying Changes
Pushing to `main` automatically triggers GitHub Pages build:
```powershell
cd D:\GitHub\pustaka-terbuka\marc-retriever
git add .
git commit -m "feat: enhance marc-retriever"
git push origin main
```
