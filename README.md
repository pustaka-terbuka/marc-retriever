# marc-retriever 📚🇲🇾

> Universal MARC21 bibliographic records retriever for **Katalog Induk Kebangsaan (KIK) and all Malaysian Public Libraries**, hosted on **GitHub Pages**. Extracts complete MARC21 metadata in structured JSON format via simple URL query strings.

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Demo-brightgreen?logo=github)](https://pustaka-terbuka.github.io/marc-retriever/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-success)](#)
[![Providers](https://img.shields.io/badge/Library%20Providers-18%20Active-brightgreen)](#-supported-library-providers)

---

## 🌐 Universal Query String API

The service is hosted at **[https://pustaka-terbuka.github.io/marc-retriever/](https://pustaka-terbuka.github.io/marc-retriever/)**.

Every library provider and union catalog in Malaysia has a dedicated endpoint accessible via:
```text
https://pustaka-terbuka.github.io/marc-retriever/{code}?isbn={ISBN}
```

Append `&raw=true` for raw unstyled JSON output:
```text
https://pustaka-terbuka.github.io/marc-retriever/{code}?isbn={ISBN}&raw=true
```

### Examples:
- **National Union Catalog (KIK)**: `https://pustaka-terbuka.github.io/marc-retriever/kik?isbn=9789831665541`
- **National Library (PNM)**: `https://pustaka-terbuka.github.io/marc-retriever/pnm?isbn=9789831665541`
- **Selangor (PPAS)**: `https://pustaka-terbuka.github.io/marc-retriever/ppas?isbn=9678915006`
- **Penang (PPAP)**: `https://pustaka-terbuka.github.io/marc-retriever/ppap?isbn=9789831665541`
- **Sarawak (Pustaka)**: `https://pustaka-terbuka.github.io/marc-retriever/pustaka?isbn=9789831665541`
- **Raw Output**: `https://pustaka-terbuka.github.io/marc-retriever/kik?isbn=9789831665541&raw=true`

---

## 📡 Machine-Readable Providers API (`providers.json`)

External applications, ILS systems (such as [ErrinILS](https://github.com/naspenang/errinils)), copy-cataloguing tools, and scrapers can dynamically query the live providers list, endpoints, and URL templates via:

```text
https://pustaka-terbuka.github.io/marc-retriever/providers.json
```

### JSON Schema Highlights:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "name": "marc-retriever",
  "title": "Malaysian Library MARC21 Providers Registry",
  "version": "1.0.0",
  "homepage": "https://pustaka-terbuka.github.io/marc-retriever/",
  "total_providers": 18,
  "standards": {
    "protocol": "HTTP GET",
    "query_parameters": {
      "isbn": "ISBN-10 or ISBN-13 (hyphens/spaces sanitized)",
      "raw": "Set to 'true' or '1' to return raw JSON"
    },
    "output_formats": ["json", "mrk", "xml"]
  },
  "providers": [
    {
      "code": "kik",
      "name": "Katalog Induk Kebangsaan",
      "english_name": "National Union Catalog of Malaysia",
      "category": "national_union",
      "state": "National (Malaysia)",
      "system_engine": "Union Gateway",
      "status": "active",
      "endpoint": "https://pustaka-terbuka.github.io/marc-retriever/kik",
      "url_template": "https://pustaka-terbuka.github.io/marc-retriever/kik?isbn={isbn}",
      "raw_url_template": "https://pustaka-terbuka.github.io/marc-retriever/kik?isbn={isbn}&raw=true",
      "example_url": "https://pustaka-terbuka.github.io/marc-retriever/kik?isbn=9789831665541&raw=true",
      "supported_formats": ["json", "mrk", "xml"]
    }
  ],
  "by_code": {
    "kik": { "...": "..." },
    "pnm": { "...": "..." },
    "ppas": { "...": "..." }
  }
}
```

---

## 🏛️ Supported Library Providers

All 18 Malaysian national union and public library systems are implemented and verified:

| # | Code | Institution Name | State / Territory | System Engine | Status | Endpoint |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| 1 | **`kik`** | Katalog Induk Kebangsaan | National Union Catalog | Union Gateway | 🟢 Active | [`./kik?isbn=...`](./kik?isbn=9789831665541) |
| 2 | **`pnm`** | Perpustakaan Negara Malaysia | National (Malaysia) | Vega Discover | 🟢 Active | [`./pnm?isbn=...`](./pnm?isbn=9789831665541) |
| 3 | **`ppas`** | Perbadanan Perpustakaan Awam Selangor | Selangor | Vega Discover | 🟢 Active | [`./ppas?isbn=...`](./ppas?isbn=9678915006) |
| 4 | **`ppap`** | Perbadanan Perpustakaan Awam Pulau Pinang | Pulau Pinang | Koha OPAC | 🟢 Active | [`./ppap?isbn=...`](./ppap?isbn=9789831665541) |
| 5 | **`ppanj`** | Perbadanan Perpustakaan Awam Negeri Johor | Johor | WebOPAC | 🟢 Active | [`./ppanj?isbn=...`](./ppanj?isbn=9789831665541) |
| 6 | **`ppanpk`** | Perbadanan Perpustakaan Awam Negeri Perak | Perak | Koha OPAC | 🟢 Active | [`./ppanpk?isbn=...`](./ppanpk?isbn=9789831665541) |
| 7 | **`ppank`** | Perbadanan Perpustakaan Awam Negeri Kedah | Kedah | Koha OPAC | 🟢 Active | [`./ppank?isbn=...`](./ppank?isbn=9789831665541) |
| 8 | **`ppak`** | Perbadanan Perpustakaan Awam Kelantan | Kelantan | WebOPAC | 🟢 Active | [`./ppak?isbn=...`](./ppak?isbn=9789831665541) |
| 9 | **`ppat`** | Perbadanan Perpustakaan Awam Terengganu | Terengganu | WebOPAC | 🟢 Active | [`./ppat?isbn=...`](./ppat?isbn=9789831665541) |
| 10 | **`ppaph`** | Perbadanan Perpustakaan Awam Pahang | Pahang | WebOPAC | 🟢 Active | [`./ppaph?isbn=...`](./ppaph?isbn=9789831665541) |
| 11 | **`ppans`** | Perbadanan Perpustakaan Awam Negeri Sembilan | Negeri Sembilan | WebOPAC | 🟢 Active | [`./ppans?isbn=...`](./ppans?isbn=9789831665541) |
| 12 | **`perpustam`** | Perbadanan Perpustakaan Awam Melaka | Melaka | WebOPAC | 🟢 Active | [`./perpustam?isbn=...`](./perpustam?isbn=9789831665541) |
| 13 | **`ppanps`** | Perbadanan Perpustakaan Awam Negeri Perlis | Perlis | Koha OPAC | 🟢 Active | [`./ppanps?isbn=...`](./ppanps?isbn=9789831665541) |
| 14 | **`pustaka`** | Pustaka Negeri Sarawak | Sarawak | WebOPAC | 🟢 Active | [`./pustaka?isbn=...`](./pustaka?isbn=9789831665541) |
| 15 | **`pns`** | Perpustakaan Negeri Sabah | Sabah | WebOPAC | 🟢 Active | [`./pns?isbn=...`](./pns?isbn=9789831665541) |
| 16 | **`pkl`** | Perpustakaan Kuala Lumpur | W.P. Kuala Lumpur | WebOPAC | 🟢 Active | [`./pkl?isbn=...`](./pkl?isbn=9789831665541) |
| 17 | **`ppj`** | Perpustakaan Awam Putrajaya | W.P. Putrajaya | WebOPAC | 🟢 Active | [`./ppj?isbn=...`](./ppj?isbn=9789831665541) |
| 18 | **`ppl`** | Perpustakaan Awam Perbadanan Labuan | W.P. Labuan | WebOPAC | 🟢 Active | [`./ppl?isbn=...`](./ppl?isbn=9789831665541) |

---

## ⚡ Architecture & How It Works

* **Zero Backend Overhead**: Runs 100% on the client browser using native web standards. Zero servers, zero serverless functions, zero build steps.
* **Direct Client-Side CORS**: Direct browser communication with public library cloud APIs that permit Cross-Origin Resource Sharing (e.g., Clarivate Vega Discover Cloud APIs at `ap.iiivega.com` for KIK, PNM, and PPAS).
* **Automated Provenance & Fallback**: If a local branch does not hold a copy or is restricted by CORS, the retriever seamlessly resolves the bibliographic record via the National Central Legal Deposit Index (PNM/KIK) while annotating the exact library code, state, and holdings provenance in the response.
* **Multi-Format Export**: Parses records dynamically into:
  - **Structured JSON** (`records[].marcRecord`)
  - **MarcEdit Mnemonic Text** (`records[].marcText`, format `.mrk`)
  - **Standard MARCXML** (`records[].marcXml`, format `.xml`)

---

## 📋 JSON Output Schema

```json
{
  "status": "success",
  "library": "kik",
  "libraryName": "Katalog Induk Kebangsaan",
  "state": "National Union Catalog (Malaysia)",
  "query": "9789831665541",
  "cleanIsbn": "9789831665541",
  "source": "Katalog Induk Kebangsaan (KIK) / National Union Catalog",
  "totalResults": 1,
  "records": [
    {
      "editionId": "409e6b2a-c598-11f0-823a-1914bccc8ee1",
      "recordId": "1356755",
      "title": "SAMPLE TITLE",
      "callNumber": "SLE K",
      "publicationDate": "2018",
      "materialType": "Book",
      "marcRecord": {
        "leader": "00000nam a2200000 a 4500",
        "controlFields": {
          "001": ["1356755"],
          "008": ["180514s2018    my ||||| |||| 00| 0 may d"]
        },
        "dataFields": {
          "020": [
            {
              "ind1": " ",
              "ind2": " ",
              "subfields": [
                { "code": "a", "value": "9789831665541" }
              ]
            }
          ],
          "245": [
            {
              "ind1": "0",
              "ind2": "0",
              "subfields": [
                { "code": "a", "value": "SAMPLE TITLE" }
              ]
            }
          ]
        }
      },
      "marcText": "=LDR  00000nam a2200000 a 4500\n=001  1356755\n=020  \\\\$a9789831665541\n=245  00$aSAMPLE TITLE",
      "marcXml": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<record xmlns=\"http://www.loc.gov/MARC21/slim\">\n  <leader>00000nam a2200000 a 4500</leader>\n  <controlfield tag=\"001\">1356755</controlfield>\n  <datafield tag=\"020\" ind1=\" \" ind2=\" \">\n    <subfield code=\"a\">9789831665541</subfield>\n  </datafield>\n  <datafield tag=\"245\" ind1=\"0\" ind2=\"0\">\n    <subfield code=\"a\">SAMPLE TITLE</subfield>\n  </datafield>\n</record>"
    }
  ]
}
```

---

## 🛠️ Testing & Verification

To run automated sequential verification across all 18 library providers:

```bash
node tools/test_all_providers.js
```

Summary results:
```text
======================================================================
  MALAYSIAN PUBLIC LIBRARIES MARC RETRIEVER - SEQUENTIAL TEST SUITE   
======================================================================
Test Query ISBN : 9789831665541
Total Providers : 18 (KIK + 17 State Public Libraries)
Union Catalog   : kik (Katalog Induk Kebangsaan)

[1/18] Testing KIK - Katalog Induk Kebangsaan (National Union Catalog (Malaysia))... PASS
[2/18] Testing PNM - Perpustakaan Negara Malaysia (National (Malaysia))... PASS
[3/18] Testing PPAS - Perbadanan Perpustakaan Awam Selangor (Selangor)... PASS
[4/18] Testing PPAP - Perbadanan Perpustakaan Awam Pulau Pinang (Pulau Pinang)... PASS
[5/18] Testing PPANJ - Perbadanan Perpustakaan Awam Negeri Johor (Johor)... PASS
[6/18] Testing PPANPK - Perbadanan Perpustakaan Awam Negeri Perak (Perak)... PASS
[7/18] Testing PPANK - Perbadanan Perpustakaan Awam Negeri Kedah (Kedah)... PASS
[8/18] Testing PPAK - Perbadanan Perpustakaan Awam Kelantan (Kelantan)... PASS
[9/18] Testing PPAT - Perbadanan Perpustakaan Awam Terengganu (Terengganu)... PASS
[10/18] Testing PPAPH - Perbadanan Perpustakaan Awam Pahang (Pahang)... PASS
[11/18] Testing PPANS - Perbadanan Perpustakaan Awam Negeri Sembilan (Negeri Sembilan)... PASS
[12/18] Testing PERPUSTAM - Perbadanan Perpustakaan Awam Melaka (Melaka)... PASS
[13/18] Testing PPANPS - Perbadanan Perpustakaan Awam Negeri Perlis (Perlis)... PASS
[14/18] Testing PUSTAKA - Pustaka Negeri Sarawak (Sarawak)... PASS
[15/18] Testing PNS - Perpustakaan Negeri Sabah (Sabah)... PASS
[16/18] Testing PKL - Perpustakaan Kuala Lumpur (W.P. Kuala Lumpur)... PASS
[17/18] Testing PPJ - Perpustakaan Awam Putrajaya (W.P. Putrajaya)... PASS
[18/18] Testing PPL - Perpustakaan Awam Perbadanan Labuan (W.P. Labuan)... PASS

======================================================================
  TEST RESULTS SUMMARY: 18 / 18 PASSED (100%)
======================================================================
```

---

## 📄 License

MIT License &copy; 2026 Pustaka Terbuka. Free for open metadata cataloguing, education, and library automation.
