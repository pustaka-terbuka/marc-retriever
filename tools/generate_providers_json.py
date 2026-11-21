import json
import os
from datetime import datetime

BASE_DIR = r"D:\GitHub\pustaka-terbuka\marc-retriever"
BASE_URL = "https://pustaka-terbuka.github.io/marc-retriever"

PROVIDERS_DATA = [
    {
        "code": "kik",
        "name": "Katalog Induk Kebangsaan",
        "english_name": "National Union Catalog of Malaysia",
        "category": "national_union",
        "state": "National (Malaysia)",
        "flag": "🇲🇾",
        "engine": "Union Gateway",
        "type": "union",
        "portal_url": "https://kik.pnm.gov.my/",
        "description": "National Union Catalog uniting collections of Malaysian public, academic, and special libraries."
    },
    {
        "code": "pnm",
        "name": "Perpustakaan Negara Malaysia",
        "english_name": "National Library of Malaysia",
        "category": "national_library",
        "state": "National (Malaysia)",
        "flag": "🇲🇾",
        "engine": "Clarivate Vega Discover",
        "type": "vega",
        "portal_url": "https://opac.pnm.gov.my/",
        "description": "National legal deposit depository and central bibliographic repository."
    },
    {
        "code": "ppas",
        "name": "Perbadanan Perpustakaan Awam Selangor",
        "english_name": "Selangor Public Library Corporation",
        "category": "state_public",
        "state": "Selangor",
        "flag": "🔴🟡",
        "engine": "Clarivate Vega Discover",
        "type": "vega",
        "portal_url": "https://ppas.ap.iiivega.com/",
        "description": "Selangor state public library network & Raja Tun Uda central repository."
    },
    {
        "code": "ppap",
        "name": "Perbadanan Perpustakaan Awam Pulau Pinang",
        "english_name": "Penang Public Library Corporation",
        "category": "state_public",
        "state": "Pulau Pinang",
        "flag": "🟡🔵",
        "engine": "Koha OPAC",
        "type": "koha",
        "portal_url": "https://www.penanglib.gov.my/",
        "description": "Penang state public library consortium and community branch network."
    },
    {
        "code": "ppanj",
        "name": "Perbadanan Perpustakaan Awam Negeri Johor",
        "english_name": "Johor State Public Library Corporation",
        "category": "state_public",
        "state": "Johor",
        "flag": "🔵🔴",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://ppaj.johor.gov.my",
        "description": "Johor state public library corporation & regional community divisions."
    },
    {
        "code": "ppanpk",
        "name": "Perbadanan Perpustakaan Awam Negeri Perak",
        "english_name": "Perak State Public Library Corporation",
        "category": "state_public",
        "state": "Perak",
        "flag": "⚪🟡⚫",
        "engine": "Koha OPAC",
        "type": "koha",
        "portal_url": "http://ppanpk.gov.my/",
        "description": "Perak state public library system and municipal branches."
    },
    {
        "code": "ppank",
        "name": "Perbadanan Perpustakaan Awam Negeri Kedah",
        "english_name": "Kedah State Public Library Corporation",
        "category": "state_public",
        "state": "Kedah",
        "flag": "🔴🟢",
        "engine": "Koha OPAC",
        "type": "koha",
        "portal_url": "http://kedahlib.gov.my/",
        "description": "Kedah state public library network and district branches."
    },
    {
        "code": "ppak",
        "name": "Perbadanan Perpustakaan Awam Kelantan",
        "english_name": "Kelantan Public Library Corporation",
        "category": "state_public",
        "state": "Kelantan",
        "flag": "🔴⚪",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://www.kelantanlibrary.gov.my",
        "description": "Kelantan state public library network and resource centers."
    },
    {
        "code": "ppat",
        "name": "Perbadanan Perpustakaan Awam Terengganu",
        "english_name": "Terengganu Public Library Corporation",
        "category": "state_public",
        "state": "Terengganu",
        "flag": "⚪⚫",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://www.trglib.gov.my",
        "description": "Terengganu public library corporation & regional divisions."
    },
    {
        "code": "ppaph",
        "name": "Perbadanan Perpustakaan Awam Pahang",
        "english_name": "Pahang Public Library Corporation",
        "category": "state_public",
        "state": "Pahang",
        "flag": "⚪⚫",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://pahanglibrary.gov.my",
        "description": "Pahang state public library network and rural library services."
    },
    {
        "code": "ppans",
        "name": "Perbadanan Perpustakaan Awam Negeri Sembilan",
        "english_name": "Negeri Sembilan Public Library Corporation",
        "category": "state_public",
        "state": "Negeri Sembilan",
        "flag": "🟡🔴⚫",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://www.nslibrary.gov.my",
        "description": "Negeri Sembilan public library system and community mobile libraries."
    },
    {
        "code": "perpustam",
        "name": "Perbadanan Perpustakaan Awam Melaka",
        "english_name": "Melaka Public Library Corporation",
        "category": "state_public",
        "state": "Melaka",
        "flag": "🔵🔴⚪",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://perpustam.gov.my",
        "description": "Melaka state public library corporation and historical collections."
    },
    {
        "code": "ppanps",
        "name": "Perbadanan Perpustakaan Awam Negeri Perlis",
        "english_name": "Perlis State Public Library Corporation",
        "category": "state_public",
        "state": "Perlis",
        "flag": "🟡🔵",
        "engine": "Koha OPAC",
        "type": "koha",
        "portal_url": "http://perlislib.gov.my/",
        "description": "Perlis state public library network and community services."
    },
    {
        "code": "pustaka",
        "name": "Pustaka Negeri Sarawak",
        "english_name": "Sarawak State Library",
        "category": "state_public",
        "state": "Sarawak",
        "flag": "🔴🟡⚫",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://www.pustaka-sarawak.com",
        "description": "Sarawak state library and Borneo legal deposit repository."
    },
    {
        "code": "pns",
        "name": "Perpustakaan Negeri Sabah",
        "english_name": "Sabah State Library",
        "category": "state_public",
        "state": "Sabah",
        "flag": "🔵⚪🔴",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://library.sabah.gov.my",
        "description": "Sabah state library network and North Borneo collections."
    },
    {
        "code": "pkl",
        "name": "Perpustakaan Kuala Lumpur",
        "english_name": "Kuala Lumpur Library",
        "category": "territory_public",
        "state": "W.P. Kuala Lumpur",
        "flag": "🔴⚪🔵",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://www.dbkl.gov.my",
        "description": "Kuala Lumpur metropolitan public library system under DBKL."
    },
    {
        "code": "ppj",
        "name": "Perpustakaan Awam Putrajaya",
        "english_name": "Putrajaya Public Library",
        "category": "territory_public",
        "state": "W.P. Putrajaya",
        "flag": "🟡🔵🔴",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://library.ppj.gov.my",
        "description": "Putrajaya administrative federal territory public library."
    },
    {
        "code": "ppl",
        "name": "Perpustakaan Awam Perbadanan Labuan",
        "english_name": "Labuan Corporation Public Library",
        "category": "territory_public",
        "state": "W.P. Labuan",
        "flag": "🔴⚪🔵",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://www.pl.gov.my",
        "description": "Federal Territory of Labuan public library corporation."
    },
    {
        "code": "u-pustaka",
        "name": "u-Pustaka",
        "english_name": "u-Pustaka National Information Hub & Consortium",
        "category": "national_consortium",
        "state": "National Consortium (Malaysia)",
        "flag": "🇲🇾",
        "engine": "Union Gateway",
        "type": "union",
        "portal_url": "https://www.u-pustaka.gov.my/",
        "description": "National digital library and public library consortium gateway under Perpustakaan Negara Malaysia."
    },
    {
        "code": "malcat",
        "name": "MALCat (Malaysian Academic Library Union Catalog)",
        "english_name": "Malaysian Academic Library Union Catalog",
        "category": "academic_union",
        "state": "National Academic (PERPUN / JKPUA)",
        "flag": "🎓🇲🇾",
        "engine": "Union Gateway",
        "type": "webopac",
        "portal_url": "https://perpun.upm.edu.my",
        "description": "Union catalog of Malaysian public and research universities managed by PERPUN / JKPUA."
    },
    {
        "code": "um",
        "name": "Universiti Malaya (UM)",
        "english_name": "University of Malaya Library",
        "category": "academic",
        "state": "W.P. Kuala Lumpur",
        "flag": "🔵🟡",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://pendeta.um.edu.my",
        "description": "Perpustakaan Universiti Malaya (Pendeta Discovery), comprehensive academic and heritage repository."
    },
    {
        "code": "ukm",
        "name": "Universiti Kebangsaan Malaysia (UKM)",
        "english_name": "National University of Malaysia - Tun Seri Lanang Library",
        "category": "academic",
        "state": "Selangor",
        "flag": "🔴🔵🟡",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://gemilang.ukm.my",
        "description": "Perpustakaan Tun Seri Lanang UKM, premier national research and Malay studies collection."
    },
    {
        "code": "uitm",
        "name": "Universiti Teknologi MARA (UiTM)",
        "english_name": "UiTM - Tun Abdul Razak Library (PTAR)",
        "category": "academic",
        "state": "Selangor",
        "flag": "🟣🟡",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://ptar.uitm.edu.my",
        "description": "Perpustakaan Tun Abdul Razak (PTAR), largest university library network across Malaysia."
    },
    {
        "code": "upsi",
        "name": "Universiti Pendidikan Sultan Idris (UPSI)",
        "english_name": "Sultan Idris Education University - Tuanku Bainun Library",
        "category": "academic",
        "state": "Perak",
        "flag": "🔵🟡🔴",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://pustaka.upsi.edu.my",
        "description": "Perpustakaan Tuanku Bainun UPSI, specialized in education, school pedagogy, and children's literature."
    },
    {
        "code": "dbp",
        "name": "Dewan Bahasa dan Pustaka (DBP)",
        "english_name": "Institute of Language and Literature Library",
        "category": "special_heritage",
        "state": "W.P. Kuala Lumpur",
        "flag": "🔵🔴",
        "engine": "WebOPAC",
        "type": "webopac",
        "portal_url": "https://dbp.gov.my",
        "description": "Perpustakaan DBP, the definitive repository for Malay language, literature, and lexicography."
    }
]

def generate_providers_json():
    providers_list = []
    by_code = {}

    for item in PROVIDERS_DATA:
        code = item["code"]
        endpoint = f"{BASE_URL}/{code}"
        url_template = f"{BASE_URL}/{code}?isbn={{isbn}}"
        raw_url_template = f"{BASE_URL}/{code}?isbn={{isbn}}&raw=true"
        
        sample_isbn = "9678915006" if code == "ppas" else "9789831665541"
        example_url = f"{BASE_URL}/{code}?isbn={sample_isbn}&raw=true"

        provider_obj = {
            "code": code,
            "name": item["name"],
            "english_name": item["english_name"],
            "category": item["category"],
            "state": item["state"],
            "flag": item["flag"],
            "system_engine": item["engine"],
            "status": "active",
            "portal_url": item["portal_url"],
            "description": item["description"],
            "endpoint": endpoint,
            "url_template": url_template,
            "raw_url_template": raw_url_template,
            "example_url": example_url,
            "supported_formats": ["json", "mrk", "xml"]
        }

        providers_list.append(provider_obj)
        by_code[code] = provider_obj

    registry = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "name": "marc-retriever",
        "title": "Malaysian Library MARC21 Providers Registry",
        "description": "Machine-readable directory of supported Malaysian union and public library providers for automated MARC21 bibliographic record retrieval.",
        "version": "1.0.0",
        "homepage": BASE_URL + "/",
        "repository": "https://github.com/pustaka-terbuka/marc-retriever",
        "license": "MIT",
        "total_providers": len(providers_list),
        "standards": {
            "protocol": "HTTP GET",
            "query_parameters": {
                "isbn": "ISBN-10 or ISBN-13 (hyphens and spaces automatically sanitized)",
                "raw": "Set to 'true' or '1' to return pure raw JSON without HTML formatting",
                "format": "Optional format specification ('json', 'mrk', 'xml', or 'raw')"
            },
            "output_formats": [
                {
                    "format": "json",
                    "mime_type": "application/json",
                    "description": "Structured JSON containing MARC leader, control fields, and data fields with subfields"
                },
                {
                    "format": "mrk",
                    "mime_type": "text/plain",
                    "description": "MarcEdit tagged mnemonic text format (=LDR, =001, =020, =245, etc.)"
                },
                {
                    "format": "xml",
                    "mime_type": "application/xml",
                    "description": "Standard Library of Congress MARCXML slim schema"
                }
            ]
        },
        "providers": providers_list,
        "by_code": by_code
    }

    out_file = os.path.join(BASE_DIR, "providers.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
    
    print(f"Generated {out_file} with {len(providers_list)} providers successfully!")

if __name__ == "__main__":
    generate_providers_json()
