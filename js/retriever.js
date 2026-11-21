/**
 * marc-retriever: Universal Malaysian Public Libraries MARC21 Engine
 * (c) 2026 Pustaka Terbuka - MIT License
 */

const LIBRARY_REGISTRY = {
  pnm: {
    code: "pnm",
    name: "Perpustakaan Negara Malaysia",
    state: "National (Malaysia)",
    type: "vega",
    status: "active",
    customerDomain: "pnm.ap.iiivega.com",
    hostDomain: "opac.pnm.gov.my",
    portalUrl: "https://opac.pnm.gov.my/"
  },
  ppas: {
    code: "ppas",
    name: "Perbadanan Perpustakaan Awam Selangor",
    state: "Selangor",
    type: "vega",
    status: "active",
    customerDomain: "ppas.ap.iiivega.com",
    hostDomain: "ppas.ap.iiivega.com",
    portalUrl: "https://ppas.ap.iiivega.com/"
  },
  ppap: {
    code: "ppap",
    name: "Perbadanan Perpustakaan Awam Pulau Pinang",
    state: "Pulau Pinang",
    type: "koha",
    status: "active",
    opacUrl: "https://opac.penanglib.gov.my",
    portalUrl: "https://www.penanglib.gov.my/"
  },
  ppanpk: {
    code: "ppanpk",
    name: "Perbadanan Perpustakaan Awam Negeri Perak",
    state: "Perak",
    type: "koha",
    status: "active",
    opacUrl: "https://opac.ppanpk.gov.my",
    portalUrl: "http://ppanpk.gov.my/"
  },
  ppank: {
    code: "ppank",
    name: "Perbadanan Perpustakaan Awam Negeri Kedah",
    state: "Kedah",
    type: "koha",
    status: "active",
    opacUrl: "http://opac.kedahlib.gov.my",
    portalUrl: "http://kedahlib.gov.my/"
  },
  ppanps: {
    code: "ppanps",
    name: "Perbadanan Perpustakaan Awam Negeri Perlis",
    state: "Perlis",
    type: "koha",
    status: "active",
    opacUrl: "http://opac.perlislib.gov.my",
    portalUrl: "http://perlislib.gov.my/"
  },
  ppanj: {
    code: "ppanj",
    name: "Perbadanan Perpustakaan Awam Negeri Johor",
    state: "Johor",
    type: "webopac",
    status: "active",
    portalUrl: "https://ppaj.johor.gov.my"
  },
  ppak: {
    code: "ppak",
    name: "Perbadanan Perpustakaan Awam Kelantan",
    state: "Kelantan",
    type: "webopac",
    status: "active",
    portalUrl: "https://www.kelantanlibrary.gov.my"
  },
  ppat: {
    code: "ppat",
    name: "Perbadanan Perpustakaan Awam Terengganu",
    state: "Terengganu",
    type: "webopac",
    status: "active",
    portalUrl: "https://www.trglib.gov.my"
  },
  ppaph: {
    code: "ppaph",
    name: "Perbadanan Perpustakaan Awam Pahang",
    state: "Pahang",
    type: "webopac",
    status: "active",
    portalUrl: "https://pahanglibrary.gov.my"
  },
  ppans: {
    code: "ppans",
    name: "Perbadanan Perpustakaan Awam Negeri Sembilan",
    state: "Negeri Sembilan",
    type: "webopac",
    status: "active",
    portalUrl: "https://www.nslibrary.gov.my"
  },
  perpustam: {
    code: "perpustam",
    name: "Perbadanan Perpustakaan Awam Melaka",
    state: "Melaka",
    type: "webopac",
    status: "active",
    portalUrl: "https://perpustam.gov.my"
  },
  pustaka: {
    code: "pustaka",
    name: "Pustaka Negeri Sarawak",
    state: "Sarawak",
    type: "webopac",
    status: "active",
    portalUrl: "https://www.pustaka-sarawak.com"
  },
  pns: {
    code: "pns",
    name: "Perpustakaan Negeri Sabah",
    state: "Sabah",
    type: "webopac",
    status: "active",
    portalUrl: "https://library.sabah.gov.my"
  },
  pkl: {
    code: "pkl",
    name: "Perpustakaan Kuala Lumpur",
    state: "W.P. Kuala Lumpur",
    type: "webopac",
    status: "active",
    portalUrl: "https://www.dbkl.gov.my"
  },
  ppj: {
    code: "ppj",
    name: "Perpustakaan Awam Putrajaya",
    state: "W.P. Putrajaya",
    type: "webopac",
    status: "active",
    portalUrl: "https://library.ppj.gov.my"
  },
  ppl: {
    code: "ppl",
    name: "Perpustakaan Awam Perbadanan Labuan",
    state: "W.P. Labuan",
    type: "webopac",
    status: "active",
    portalUrl: "https://www.pl.gov.my"
  }
};

const API_VEGA_HOST = "https://ap.iiivega.com";

function generateUUID() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => {
    const r = Math.random() * 16 | 0;
    return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
  });
}

function marcToText(marc) {
  if (!marc) return "";
  let lines = [`=LDR  ${marc.leader || '00000nam a2200000 a 4500'}`];
  if (marc.controlFields) {
    Object.keys(marc.controlFields).sort().forEach(tag => {
      marc.controlFields[tag].forEach(val => lines.push(`=${tag}  ${val}`));
    });
  }
  if (marc.dataFields) {
    Object.keys(marc.dataFields).sort().forEach(tag => {
      marc.dataFields[tag].forEach(f => {
        let i1 = f.ind1 === " " ? "\\" : f.ind1;
        let i2 = f.ind2 === " " ? "\\" : f.ind2;
        let subs = (f.subfields || []).map(s => `$${s.code}${s.value}`).join("");
        lines.push(`=${tag}  ${i1}${i2}${subs}`);
      });
    });
  }
  return lines.join("\n");
}

function marcToXml(marc) {
  if (!marc) return "";
  let xml = `<?xml version="1.0" encoding="UTF-8"?>\n<record xmlns="http://www.loc.gov/MARC21/slim">\n`;
  xml += `  <leader>${escapeXml(marc.leader || '')}</leader>\n`;
  if (marc.controlFields) {
    Object.keys(marc.controlFields).sort().forEach(tag => {
      marc.controlFields[tag].forEach(val => {
        xml += `  <controlfield tag="${tag}">${escapeXml(val)}</controlfield>\n`;
      });
    });
  }
  if (marc.dataFields) {
    Object.keys(marc.dataFields).sort().forEach(tag => {
      marc.dataFields[tag].forEach(f => {
        xml += `  <datafield tag="${tag}" ind1="${escapeXml(f.ind1)}" ind2="${escapeXml(f.ind2)}">\n`;
        (f.subfields || []).forEach(s => {
          xml += `    <subfield code="${escapeXml(s.code)}">${escapeXml(s.value)}</subfield>\n`;
        });
        xml += `  </datafield>\n`;
      });
    });
  }
  xml += `</record>`;
  return xml;
}

function parseMarcXml(xmlString) {
  if (typeof DOMParser !== "undefined") {
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(xmlString, "application/xml");
    const record = xmlDoc.querySelector("record");
    if (!record) return null;

    const leader = (record.querySelector("leader")?.textContent || "").trim();
    const controlFields = {};
    record.querySelectorAll("controlfield").forEach(cf => {
      const tag = cf.getAttribute("tag");
      if (!controlFields[tag]) controlFields[tag] = [];
      controlFields[tag].push(cf.textContent || "");
    });

    const dataFields = {};
    record.querySelectorAll("datafield").forEach(df => {
      const tag = df.getAttribute("tag");
      const ind1 = df.getAttribute("ind1") || " ";
      const ind2 = df.getAttribute("ind2") || " ";
      const subfields = [];
      df.querySelectorAll("subfield").forEach(sf => {
        subfields.push({
          code: sf.getAttribute("code") || "a",
          value: sf.textContent || ""
        });
      });
      if (!dataFields[tag]) dataFields[tag] = [];
      dataFields[tag].push({ ind1, ind2, subfields });
    });

    return { leader, controlFields, dataFields };
  } else {
    // Regex-based MARCXML parser for Node.js / non-DOM environments
    const leaderMatch = xmlString.match(/<leader>([^<]+)<\/leader>/);
    const leader = leaderMatch ? leaderMatch[1].trim() : "00000nam a2200000 a 4500";
    const controlFields = {};
    const cfRegex = /<controlfield\s+tag=["'](\d{3})["']>([^<]+)<\/controlfield>/g;
    let cfMatch;
    while ((cfMatch = cfRegex.exec(xmlString)) !== null) {
      const tag = cfMatch[1];
      if (!controlFields[tag]) controlFields[tag] = [];
      controlFields[tag].push(cfMatch[2]);
    }
    const dataFields = {};
    const dfRegex = /<datafield\s+tag=["'](\d{3})["'](?:\s+ind1=["']([^"']*)["'])?(?:\s+ind2=["']([^"']*)["'])?[^>]*>([\s\S]*?)<\/datafield>/g;
    let dfMatch;
    while ((dfMatch = dfRegex.exec(xmlString)) !== null) {
      const tag = dfMatch[1];
      const ind1 = dfMatch[2] || " ";
      const ind2 = dfMatch[3] || " ";
      const inner = dfMatch[4];
      const subfields = [];
      const sfRegex = /<subfield\s+code=["']([^"']+)["']>([^<]*)<\/subfield>/g;
      let sfMatch;
      while ((sfMatch = sfRegex.exec(inner)) !== null) {
        subfields.push({ code: sfMatch[1], value: sfMatch[2] });
      }
      if (!dataFields[tag]) dataFields[tag] = [];
      dataFields[tag].push({ ind1, ind2, subfields });
    }
    return { leader, controlFields, dataFields };
  }
}

function escapeXml(unsafe) {
  return (unsafe || '').replace(/[<>&'"]/g, c => ({
    '<': '&lt;', '>': '&gt;', '&': '&amp;', '\'': '&apos;', '"': '&quot;'
  }[c]));
}

function syntaxHighlightJson(json) {
  if (typeof json !== 'string') {
    json = JSON.stringify(json, null, 2);
  }
  json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
    let cls = 'json-number';
    if (/^"/.test(match)) {
      if (/:$/.test(match)) {
        cls = 'json-key';
      } else {
        cls = 'json-string';
      }
    } else if (/true|false/.test(match)) {
      cls = 'json-boolean';
    } else if (/null/.test(match)) {
      cls = 'json-null';
    }
    return '<span class="' + cls + '">' + match + '</span>';
  });
}

/**
 * Universal Library Fetcher
 */
async function retrieveMarc(libraryCode, isbn) {
  const lib = LIBRARY_REGISTRY[libraryCode.toLowerCase()];
  if (!lib) {
    throw new Error(`Unknown library code "${libraryCode}". See library directory for available providers.`);
  }

  const cleanIsbn = isbn.trim().replace(/[-\s]/g, "");
  if (!cleanIsbn) throw new Error("Empty ISBN supplied");

  if (lib.type === "vega") {
    return await retrieveFromVega(lib, cleanIsbn, isbn);
  } else if (lib.type === "koha") {
    return await retrieveFromKoha(lib, cleanIsbn, isbn);
  } else {
    // WebOPAC / Union / Fallback through National Catalog
    return await retrieveFromFallback(lib, cleanIsbn, isbn);
  }
}

async function retrieveFromVega(lib, cleanIsbn, originalIsbn) {
  const anonId = generateUUID();
  const baseHeaders = {
    "Accept": "application/json, text/plain, */*",
    "iii-customer-domain": lib.customerDomain,
    "iii-host-domain": lib.hostDomain,
    "Anonymous-User-Id": anonId
  };

  // 1. Search format groups
  const searchRes = await fetch(`${API_VEGA_HOST}/api/search-result/search/format-groups`, {
    method: "POST",
    headers: {
      ...baseHeaders,
      "Content-Type": "application/json",
      "api-version": "2"
    },
    body: JSON.stringify({ searchText: cleanIsbn })
  });

  if (!searchRes.ok) {
    throw new Error(`Search request to ${lib.name} failed with HTTP ${searchRes.status}`);
  }

  const searchData = await searchRes.json();
  const items = searchData.data || [];

  if (items.length === 0) {
    if (lib.code !== "pnm") {
      return await retrieveFromFallback(lib, cleanIsbn, originalIsbn);
    }
    return {
      status: "not_found",
      library: lib.code,
      libraryName: lib.name,
      state: lib.state,
      query: originalIsbn,
      cleanIsbn: cleanIsbn,
      source: `${lib.name} OPAC`,
      totalResults: 0,
      records: [],
      message: `No bibliographic records found for ISBN ${originalIsbn} in ${lib.name} catalog.`
    };
  }

  const editionMap = new Map();
  items.forEach(item => {
    (item.materialTabs || []).forEach(tab => {
      (tab.editions || []).forEach(ed => {
        if (ed.id && !editionMap.has(ed.id)) {
          editionMap.set(ed.id, {
            editionId: ed.id,
            recordId: ed.recordId,
            title: item.title,
            callNumber: ed.callNumber || "",
            publicationDate: ed.publicationDate || item.publicationDate || "",
            materialType: tab.name || "Book"
          });
        }
      });
    });
  });

  const editions = Array.from(editionMap.values());
  const recordPromises = editions.map(async (ed) => {
    try {
      const edRes = await fetch(`${API_VEGA_HOST}/api/search-result/editions/${ed.editionId}`, {
        headers: {
          ...baseHeaders,
          "api-version": "1"
        }
      });

      if (!edRes.ok) return null;
      const edData = await edRes.json();
      const marc = edData.marcRecord;

      return {
        editionId: ed.editionId,
        recordId: ed.recordId,
        title: ed.title,
        callNumber: ed.callNumber,
        publicationDate: ed.publicationDate,
        materialType: ed.materialType,
        marcRecord: marc,
        marcText: marcToText(marc),
        marcXml: marcToXml(marc)
      };
    } catch (e) {
      return null;
    }
  });

  const fullRecords = (await Promise.all(recordPromises)).filter(Boolean);

  return {
    status: "success",
    library: lib.code,
    libraryName: lib.name,
    state: lib.state,
    query: originalIsbn,
    cleanIsbn: cleanIsbn,
    source: `${lib.name} OPAC`,
    totalResults: fullRecords.length,
    records: fullRecords
  };
}

async function retrieveFromKoha(lib, cleanIsbn, originalIsbn) {
  // Direct or Proxied Koha Search
  try {
    const searchUrl = `${lib.opacUrl}/cgi-bin/koha/opac-search.pl?q=isbn:${cleanIsbn}`;
    const res = await fetch(searchUrl);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const html = await res.text();

    const bibMatches = html.match(/biblionumber=(\d+)/g) || [];
    const bibIds = [...new Set(bibMatches.map(m => m.split('=')[1]))];

    if (bibIds.length === 0) {
      // Fallback
      return await retrieveFromFallback(lib, cleanIsbn, originalIsbn);
    }

    const records = [];
    for (const bibId of bibIds.slice(0, 5)) {
      const exportUrl = `${lib.opacUrl}/cgi-bin/koha/opac-export.pl?op=export&format=marcxml&bib=${bibId}`;
      const exportRes = await fetch(exportUrl);
      if (exportRes.ok) {
        const xmlText = await exportRes.text();
        const marcObj = parseMarcXml(xmlText);
        if (marcObj) {
          records.push({
            editionId: `koha-${lib.code}-${bibId}`,
            recordId: bibId,
            title: marcObj.dataFields["245"]?.[0]?.subfields?.[0]?.value || "Untitled",
            callNumber: marcObj.dataFields["082"]?.[0]?.subfields?.[0]?.value || "",
            publicationDate: marcObj.dataFields["260"]?.[0]?.subfields?.[2]?.value || "",
            materialType: "Book",
            marcRecord: marcObj,
            marcText: marcToText(marcObj),
            marcXml: xmlText
          });
        }
      }
    }

    return {
      status: "success",
      library: lib.code,
      libraryName: lib.name,
      state: lib.state,
      query: originalIsbn,
      cleanIsbn: cleanIsbn,
      source: `${lib.name} Koha`,
      totalResults: records.length,
      records: records
    };
  } catch (e) {
    // If CORS or timeout occurs on on-premise servers, fallback to National/State union resolver
    return await retrieveFromFallback(lib, cleanIsbn, originalIsbn);
  }
}

async function retrieveFromFallback(lib, cleanIsbn, originalIsbn) {
  // Query via National Library (PNM) union index and mark provenance
  const pnmResult = await retrieveFromVega(LIBRARY_REGISTRY.pnm, cleanIsbn, originalIsbn);
  if (pnmResult.status === "success") {
    return {
      ...pnmResult,
      library: lib.code,
      libraryName: lib.name,
      state: lib.state,
      holdingInLibrary: false,
      resolvedVia: "National Central Index (PNM)",
      notes: `Bibliographic record resolved via National Central Index on behalf of ${lib.name}.`
    };
  }
  return {
    status: "not_found",
    library: lib.code,
    libraryName: lib.name,
    state: lib.state,
    query: originalIsbn,
    cleanIsbn: cleanIsbn,
    totalResults: 0,
    records: [],
    message: `No bibliographic records found for ISBN ${originalIsbn} in ${lib.name} or National Central Index.`
  };
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    LIBRARY_REGISTRY,
    retrieveMarc,
    retrieveFromVega,
    retrieveFromKoha,
    retrieveFromFallback,
    marcToText,
    marcToXml,
    parseMarcXml,
    escapeXml
  };
}
