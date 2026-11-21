# marc-retriever 📚🇲🇾

> Universal MARC21 bibliographic records retriever for **Malaysian National and Public Libraries**, hosted on **GitHub Pages**. Extracts complete MARC21 metadata in structured JSON format via simple URL query strings.

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Demo-brightgreen?logo=github)](https://pustaka-terbuka.github.io/marc-retriever/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-success)](#)

---

## 🌐 Universal Query String API

The service is hosted at **[https://pustaka-terbuka.github.io/marc-retriever/](https://pustaka-terbuka.github.io/marc-retriever/)**.

Each library provider has its own clean path:

### 1. Perpustakaan Negara Malaysia (PNM)
```text
https://pustaka-terbuka.github.io/marc-retriever/pnm?isbn=9789831665541
```

* **Raw JSON Mode** (Unstyled direct JSON response):
  ```text
  https://pustaka-terbuka.github.io/marc-retriever/pnm?isbn=9789831665541&raw=true
  ```

---

## 🏛️ Supported Library Providers

| Code | Library Name | System | Status | Endpoint |
| :--- | :--- | :--- | :--- | :--- |
| **`pnm`** | **Perpustakaan Negara Malaysia** | Vega Discover OPAC | 🟢 **Active** | `.../pnm?isbn=<ISBN>` |
| **`ppas`** | Perbadanan Perpustakaan Awam Selangor | Koha ILS | 🟡 Planned | `.../ppas?isbn=<ISBN>` |
| **`ppap`** | Perbadanan Perpustakaan Awam P. Pinang | Koha / ILMU | 🟡 Planned | `.../ppap?isbn=<ISBN>` |
| **`pustaka`** | Pustaka Negeri Sarawak | Virtua / Chamo / Koha | 🟡 Planned | `.../pustaka?isbn=<ISBN>` |

---

## ⚡ Architecture & How It Works

* **Zero Backend Overhead**: Runs 100% on the client's browser using native web standards.
* **Direct Client-Side CORS**: Directly queries public library cloud APIs that permit Cross-Origin Resource Sharing (such as PNM's Vega Discover gateway at `ap.iiivega.com`), bypassing the need for intermediate proxy servers.
* **Format Conversion**: Automatically parses MARC-in-JSON structures into:
  - Standard JSON schema (`records[].marcRecord`)
  - MarcEdit mnemonic tagged text (`records[].marcText`)
  - Validated MARCXML (`records[].marcXml`)

---

## 📋 JSON Output Schema (`/pnm?isbn=...`)

```json
{
  "status": "success",
  "library": "pnm",
  "libraryName": "Perpustakaan Negara Malaysia",
  "query": "9789831665541",
  "cleanIsbn": "9789831665541",
  "source": "PNM OPAC",
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
        "leader": "00000aam a2200000 i 4500",
        "controlFields": {
          "001": ["1356755"],
          "005": ["20260611152116.0"],
          "008": ["220719s2022    my a   b      000 0 may  "]
        },
        "dataFields": {
          "020": [{ "ind1": " ", "ind2": " ", "subfields": [{ "code": "a", "value": "9789831665541" }] }],
          "100": [{ "ind1": "0", "ind2": " ", "subfields": [{ "code": "a", "value": "Author Name" }] }],
          "245": [{ "ind1": "1", "ind2": "0", "subfields": [{ "code": "a", "value": "Main Title" }] }]
        }
      },
      "marcText": "=LDR  00000aam a2200000 i 4500\n=001  1356755\n=245  10$aMain Title...",
      "marcXml": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<record xmlns=\"http://www.loc.gov/MARC21/slim\">..."
    }
  ]
}
```

---

## 🛠️ Code Examples

### JavaScript (Client / Node)
```javascript
const res = await fetch("https://pustaka-terbuka.github.io/marc-retriever/pnm?isbn=9789831665541&raw=true");
const data = await res.json();
console.log(data.records[0].marcRecord);
```

### Python
```python
import urllib.request, json

url = "https://pustaka-terbuka.github.io/marc-retriever/pnm?isbn=9789831665541&raw=true"
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode("utf-8"))
print("MARC Record 001:", data["records"][0]["marcRecord"]["controlFields"]["001"])
```

---

## 📄 License

MIT &copy; 2026 [Pustaka Terbuka](https://github.com/pustaka-terbuka).
Bibliographic records &copy; their respective library authorities (Perpustakaan Negara Malaysia and State Public Libraries).
