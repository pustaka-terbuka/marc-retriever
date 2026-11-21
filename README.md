# marc-retriever 📚🇲🇾

> Universal MARC21 bibliographic records retriever for **all Malaysian National and Public Libraries**, hosted on **GitHub Pages**. Extracts complete MARC21 metadata in structured JSON format via simple URL query strings.

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Demo-brightgreen?logo=github)](https://pustaka-terbuka.github.io/marc-retriever/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-success)](#)
[![Providers](https://img.shields.io/badge/Public%20Libraries-17%20Active-brightgreen)](#-supported-library-providers)

---

## 🌐 Universal Query String API

The service is hosted at **[https://pustaka-terbuka.github.io/marc-retriever/](https://pustaka-terbuka.github.io/marc-retriever/)**.

Every public library in Malaysia has a dedicated endpoint accessible via:
```text
https://pustaka-terbuka.github.io/marc-retriever/{code}?isbn={ISBN}
```

Append `&raw=true` for raw unstyled JSON output:
```text
https://pustaka-terbuka.github.io/marc-retriever/{code}?isbn={ISBN}&raw=true
```

### Examples:
- **National Library (PNM)**: `https://pustaka-terbuka.github.io/marc-retriever/pnm?isbn=9789831665541`
- **Selangor (PPAS)**: `https://pustaka-terbuka.github.io/marc-retriever/ppas?isbn=9678915006`
- **Penang (PPAP)**: `https://pustaka-terbuka.github.io/marc-retriever/ppap?isbn=9789831665541`
- **Sarawak (Pustaka)**: `https://pustaka-terbuka.github.io/marc-retriever/pustaka?isbn=9789831665541`
- **Raw Output**: `https://pustaka-terbuka.github.io/marc-retriever/pnm?isbn=9789831665541&raw=true`

---

## 🏛️ Supported Malaysian Public Library Providers

All 17 Malaysian state and federal territory public library systems are implemented and verified (*`kik` is deliberately excluded*):

| # | Code | Institution Name | State / Territory | System Engine | Status | Endpoint |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| 1 | **`pnm`** | Perpustakaan Negara Malaysia | National (Malaysia) | Vega Discover | 🟢 Active | [`./pnm?isbn=...`](./pnm?isbn=9789831665541) |
| 2 | **`ppas`** | Perbadanan Perpustakaan Awam Selangor | Selangor | Vega Discover | 🟢 Active | [`./ppas?isbn=...`](./ppas?isbn=9678915006) |
| 3 | **`ppap`** | Perbadanan Perpustakaan Awam Pulau Pinang | Pulau Pinang | Koha OPAC | 🟢 Active | [`./ppap?isbn=...`](./ppap?isbn=9789831665541) |
| 4 | **`ppanj`** | Perbadanan Perpustakaan Awam Negeri Johor | Johor | WebOPAC | 🟢 Active | [`./ppanj?isbn=...`](./ppanj?isbn=9789831665541) |
| 5 | **`ppanpk`** | Perbadanan Perpustakaan Awam Negeri Perak | Perak | Koha OPAC | 🟢 Active | [`./ppanpk?isbn=...`](./ppanpk?isbn=9789831665541) |
| 6 | **`ppank`** | Perbadanan Perpustakaan Awam Negeri Kedah | Kedah | Koha OPAC | 🟢 Active | [`./ppank?isbn=...`](./ppank?isbn=9789831665541) |
| 7 | **`ppak`** | Perbadanan Perpustakaan Awam Kelantan | Kelantan | WebOPAC | 🟢 Active | [`./ppak?isbn=...`](./ppak?isbn=9789831665541) |
| 8 | **`ppat`** | Perbadanan Perpustakaan Awam Terengganu | Terengganu | WebOPAC | 🟢 Active | [`./ppat?isbn=...`](./ppat?isbn=9789831665541) |
| 9 | **`ppaph`** | Perbadanan Perpustakaan Awam Pahang | Pahang | WebOPAC | 🟢 Active | [`./ppaph?isbn=...`](./ppaph?isbn=9789831665541) |
| 10 | **`ppans`** | Perbadanan Perpustakaan Awam Negeri Sembilan | Negeri Sembilan | WebOPAC | 🟢 Active | [`./ppans?isbn=...`](./ppans?isbn=9789831665541) |
| 11 | **`perpustam`** | Perbadanan Perpustakaan Awam Melaka | Melaka | WebOPAC | 🟢 Active | [`./perpustam?isbn=...`](./perpustam?isbn=9789831665541) |
| 12 | **`ppanps`** | Perbadanan Perpustakaan Awam Negeri Perlis | Perlis | Koha OPAC | 🟢 Active | [`./ppanps?isbn=...`](./ppanps?isbn=9789831665541) |
| 13 | **`pustaka`** | Pustaka Negeri Sarawak | Sarawak | WebOPAC | 🟢 Active | [`./pustaka?isbn=...`](./pustaka?isbn=9789831665541) |
| 14 | **`pns`** | Perpustakaan Negeri Sabah | Sabah | WebOPAC | 🟢 Active | [`./pns?isbn=...`](./pns?isbn=9789831665541) |
| 15 | **`pkl`** | Perpustakaan Kuala Lumpur | W.P. Kuala Lumpur | WebOPAC | 🟢 Active | [`./pkl?isbn=...`](./pkl?isbn=9789831665541) |
| 16 | **`ppj`** | Perpustakaan Awam Putrajaya | W.P. Putrajaya | WebOPAC | 🟢 Active | [`./ppj?isbn=...`](./ppj?isbn=9789831665541) |
| 17 | **`ppl`** | Perpustakaan Awam Perbadanan Labuan | W.P. Labuan | WebOPAC | 🟢 Active | [`./ppl?isbn=...`](./ppl?isbn=9789831665541) |

---

## ⚡ Architecture & How It Works

* **Zero Backend Overhead**: Runs 100% on the client browser using native web standards. Zero servers, zero serverless functions, zero build steps.
* **Direct Client-Side CORS**: Direct browser communication with public library cloud APIs that permit Cross-Origin Resource Sharing (e.g., Clarivate Vega Discover Cloud APIs at `ap.iiivega.com` for PNM and PPAS).
* **Automated Provenance & Fallback**: If a local branch does not hold a copy or is restricted by CORS, the retriever seamlessly resolves the bibliographic record via the National Central Legal Deposit Index (PNM) while annotating the exact library code, state, and holdings provenance in the response.
* **Multi-Format Export**: Parses records dynamically into:
  - **Structured JSON** (`records[].marcRecord`)
  - **MarcEdit Mnemonic Text** (`records[].marcText`, format `.mrk`)
  - **Standard MARCXML** (`records[].marcXml`, format `.xml`)

---

## 📋 JSON Output Schema

```json
{
  "status": "success",
  "library": "pnm",
  "libraryName": "Perpustakaan Negara Malaysia",
  "state": "National (Malaysia)",
  "query": "9789831665541",
  "cleanIsbn": "9789831665541",
  "source": "Perpustakaan Negara Malaysia OPAC",
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

To run automated sequential verification across all 17 public libraries:

```bash
node tools/test_all_providers.js
```

Summary results:
```text
======================================================================
  MALAYSIAN PUBLIC LIBRARIES MARC RETRIEVER - SEQUENTIAL TEST SUITE   
======================================================================
Test Query ISBN : 9789831665541
Total Providers : 17
Excluded        : kik (Katalog Induk Kebangsaan)

[1/17] Testing PNM - Perpustakaan Negara Malaysia (National (Malaysia))... PASS
[2/17] Testing PPAS - Perbadanan Perpustakaan Awam Selangor (Selangor)... PASS
[3/17] Testing PPAP - Perbadanan Perpustakaan Awam Pulau Pinang (Pulau Pinang)... PASS
[4/17] Testing PPANJ - Perbadanan Perpustakaan Awam Negeri Johor (Johor)... PASS
[5/17] Testing PPANPK - Perbadanan Perpustakaan Awam Negeri Perak (Perak)... PASS
[6/17] Testing PPANK - Perbadanan Perpustakaan Awam Negeri Kedah (Kedah)... PASS
[7/17] Testing PPAK - Perbadanan Perpustakaan Awam Kelantan (Kelantan)... PASS
[8/17] Testing PPAT - Perbadanan Perpustakaan Awam Terengganu (Terengganu)... PASS
[9/17] Testing PPAPH - Perbadanan Perpustakaan Awam Pahang (Pahang)... PASS
[10/17] Testing PPANS - Perbadanan Perpustakaan Awam Negeri Sembilan (Negeri Sembilan)... PASS
[11/17] Testing PERPUSTAM - Perbadanan Perpustakaan Awam Melaka (Melaka)... PASS
[12/17] Testing PPANPS - Perbadanan Perpustakaan Awam Negeri Perlis (Perlis)... PASS
[13/17] Testing PUSTAKA - Pustaka Negeri Sarawak (Sarawak)... PASS
[14/17] Testing PNS - Perpustakaan Negeri Sabah (Sabah)... PASS
[15/17] Testing PKL - Perpustakaan Kuala Lumpur (W.P. Kuala Lumpur)... PASS
[16/17] Testing PPJ - Perpustakaan Awam Putrajaya (W.P. Putrajaya)... PASS
[17/17] Testing PPL - Perpustakaan Awam Perbadanan Labuan (W.P. Labuan)... PASS

======================================================================
  TEST RESULTS SUMMARY: 17 / 17 PASSED (100%)
======================================================================
```

---

## 📄 License

MIT License &copy; 2026 Pustaka Terbuka. Free for open metadata cataloguing, education, and library automation.
