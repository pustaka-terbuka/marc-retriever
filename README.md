# marc-pnm 🇲🇾

> Client-side web app hosted on **GitHub Pages** to search books by ISBN in the **Perpustakaan Negara Malaysia (PNM) OPAC** and extract complete MARC21 records in JSON format.

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Demo-brightgreen?logo=github)](https://pustaka-terbuka.github.io/marc-pnm/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-success)](#)

---

## 🌐 Live URL & Query String API

The web app is hosted on **GitHub Pages** at:
**[https://pustaka-terbuka.github.io/marc-pnm/](https://pustaka-terbuka.github.io/marc-pnm/)**

### 1. Standard Formatted View (with JSON, MarcEdit, and MARCXML viewers)
```text
https://pustaka-terbuka.github.io/marc-pnm/?isbn=9789831665541
```

### 2. Raw JSON Mode (Direct unstyled JSON text in browser)
```text
https://pustaka-terbuka.github.io/marc-pnm/?isbn=9789831665541&raw=true
```

---

## ⚡ How It Works

1. **Zero Backend Required**: Runs 100% on the client's browser via GitHub Pages.
2. **Direct PNM Cloud API Integration**: Communicates directly with the cloud gateway powering PNM's **Innovative Vega Discover** OPAC (`https://ap.iiivega.com`), which natively permits Cross-Origin Resource Sharing (CORS) from any domain including `github.io`.
3. **2-Step Fetching Pipeline**:
   - **Search**: `POST https://ap.iiivega.com/api/search-result/search/format-groups` with `{ "searchText": "<ISBN>" }` to discover matching titles and edition UUIDs.
   - **MARC Extraction**: `GET https://ap.iiivega.com/api/search-result/editions/{editionId}` to retrieve the full, unredacted MARC21 record (Leader, 001–008 control fields, and 010–999 data fields with indicators and subfields).

---

## 📋 JSON Output Schema

When queried with `?isbn=9789831665541`, the app produces:

```json
{
  "status": "success",
  "query": "9789831665541",
  "cleanIsbn": "9789831665541",
  "source": "Perpustakaan Negara Malaysia (PNM OPAC)",
  "totalResults": 1,
  "records": [
    {
      "editionId": "409e6b2a-c598-11f0-823a-1914bccc8ee1",
      "recordId": "1356755",
      "title": "MUDAHNYA SIFIR : TEKNIK MUDAH SIFIR DAN ASAS LATIHAN PENGUKUHAN HARIAN. TAHUN 1 - TAHUN 6",
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
          "015": [
            {
              "ind1": " ",
              "ind2": " ",
              "subfields": [{ "code": "a", "value": "MB221295" }]
            }
          ],
          "020": [
            {
              "ind1": " ",
              "ind2": " ",
              "subfields": [
                { "code": "a", "value": "9789831665541" },
                { "code": "q", "value": "paperback" },
                { "code": "c", "value": "RM9.90" }
              ]
            }
          ],
          "100": [
            {
              "ind1": "0",
              "ind2": " ",
              "subfields": [
                { "code": "a", "value": "Salina," },
                { "code": "e", "value": "author." }
              ]
            }
          ],
          "245": [
            {
              "ind1": "1",
              "ind2": "0",
              "subfields": [
                { "code": "a", "value": "MUDAHNYA SIFIR :" },
                { "code": "b", "value": "TEKNIK MUDAH SIFIR DAN ASAS LATIHAN PENGUKUHAN HARIAN." },
                { "code": "n", "value": "TAHUN 1 - TAHUN 6 /" },
                { "code": "c", "value": "CIKGU SALINA, MOHAMED ISAK" }
              ]
            }
          ]
        }
      },
      "marcText": "=LDR  00000aam a2200000 i 4500\n=001  1356755\n=020  \\\\$a9789831665541$qpaperback$cRM9.90\n=245  10$aMUDAHNYA SIFIR :$bTEKNIK MUDAH SIFIR...",
      "marcXml": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<record xmlns=\"http://www.loc.gov/MARC21/slim\">\n  <leader>00000aam a2200000 i 4500</leader>\n  <controlfield tag=\"001\">1356755</controlfield>..."
    }
  ]
}
```

### When No Records are Found:
```json
{
  "status": "not_found",
  "query": "9780000000000",
  "cleanIsbn": "9780000000000",
  "source": "Perpustakaan Negara Malaysia (PNM OPAC)",
  "totalResults": 0,
  "records": [],
  "message": "No bibliographic records found for ISBN 9780000000000 in PNM OPAC."
}
```

---

## 🛠️ Direct API Code Examples

If you wish to call PNM's API directly in your own scripts or applications:

### JavaScript (Fetch)
```javascript
async function getMarcFromPNM(isbn) {
  const cleanIsbn = isbn.replace(/[-\s]/g, "");
  const headers = {
    "Accept": "application/json, text/plain, */*",
    "iii-customer-domain": "pnm.ap.iiivega.com",
    "iii-host-domain": "opac.pnm.gov.my",
    "Anonymous-User-Id": crypto.randomUUID()
  };

  // 1. Search for title & edition IDs
  const searchRes = await fetch("https://ap.iiivega.com/api/search-result/search/format-groups", {
    method: "POST",
    headers: { ...headers, "Content-Type": "application/json", "api-version": "2" },
    body: JSON.stringify({ searchText: cleanIsbn })
  });
  const searchData = await searchRes.json();
  const edition = searchData.data?.[0]?.materialTabs?.[0]?.editions?.[0];
  if (!edition) return null;

  // 2. Fetch full MARC21 record
  const edRes = await fetch(`https://ap.iiivega.com/api/search-result/editions/${edition.id}`, {
    headers: { ...headers, "api-version": "1" }
  });
  const edData = await edRes.json();
  return edData.marcRecord;
}

getMarcFromPNM("9789831665541").then(console.log);
```

### Python
```python
import urllib.request, uuid, json

isbn = "9789831665541"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json, text/plain, */*",
    "iii-customer-domain": "pnm.ap.iiivega.com",
    "iii-host-domain": "opac.pnm.gov.my",
    "Anonymous-User-Id": str(uuid.uuid4())
}

# 1. Search
search_req = urllib.request.Request(
    "https://ap.iiivega.com/api/search-result/search/format-groups",
    data=json.dumps({"searchText": isbn}).encode("utf-8"),
    headers=dict(headers, **{"Content-Type": "application/json", "api-version": "2"}),
    method="POST"
)
search_data = json.loads(urllib.request.urlopen(search_req).read())
edition_id = search_data["data"][0]["materialTabs"][0]["editions"][0]["id"]

# 2. Get MARC
ed_req = urllib.request.Request(
    f"https://ap.iiivega.com/api/search-result/editions/{edition_id}",
    headers=dict(headers, **{"api-version": "1"})
)
marc_data = json.loads(urllib.request.urlopen(ed_req).read())
print(json.dumps(marc_data["marcRecord"], indent=2))
```

---

## 🚀 Deployment Instructions

1. Push this repository to GitHub:
   ```bash
   git add .
   git commit -m "feat: complete marc-pnm web app"
   git branch -M main
   git push -u origin main
   ```
2. In your GitHub repository:
   - Navigate to **Settings** > **Pages**.
   - Under **Build and deployment** > **Source**, select **Deploy from a branch**.
   - Select branch: **`main`** and folder: **`/ (root)`**.
   - Click **Save**.
3. Your site will be live at:
   `https://pustaka-terbuka.github.io/marc-pnm/`

---

## 📄 License

MIT &copy; 2026 [Pustaka Terbuka](https://github.com/pustaka-terbuka).
Bibliographic metadata &copy; Perpustakaan Negara Malaysia (PNM).
