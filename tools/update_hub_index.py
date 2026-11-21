import os

BASE_DIR = r"D:\GitHub\pustaka-terbuka\marc-retriever"

LIBRARIES = [
    ("pnm", "Perpustakaan Negara Malaysia", "National (Malaysia)", "🇲🇾", "Vega Discover", "National library legal deposit & central bibliographic repository."),
    ("ppas", "Perbadanan Perpustakaan Awam Selangor", "Selangor", "🔴🟡", "Vega Discover", "Selangor state public library network & Raja Tun Uda central repository."),
    ("ppap", "Perbadanan Perpustakaan Awam Pulau Pinang", "Pulau Pinang", "🟡🔵", "Koha OPAC", "Penang state public library consortium and community branches."),
    ("ppanj", "Perbadanan Perpustakaan Awam Negeri Johor", "Johor", "🔵🔴", "WebOPAC", "Johor state public library corporation & community networks."),
    ("ppanpk", "Perbadanan Perpustakaan Awam Negeri Perak", "Perak", "⚪🟡⚫", "Koha OPAC", "Perak state public library system and municipal branches."),
    ("ppank", "Perbadanan Perpustakaan Awam Negeri Kedah", "Kedah", "🔴🟢", "Koha OPAC", "Kedah state public library network and district services."),
    ("ppak", "Perbadanan Perpustakaan Awam Kelantan", "Kelantan", "🔴⚪", "WebOPAC", "Kelantan state public library network and resource centers."),
    ("ppat", "Perbadanan Perpustakaan Awam Terengganu", "Terengganu", "⚪⚫", "WebOPAC", "Terengganu public library corporation & regional divisions."),
    ("ppaph", "Perbadanan Perpustakaan Awam Pahang", "Pahang", "⚪⚫", "WebOPAC", "Pahang state public library network and rural library services."),
    ("ppans", "Perbadanan Perpustakaan Awam Negeri Sembilan", "Negeri Sembilan", "🟡🔴⚫", "WebOPAC", "Negeri Sembilan public library system and mobile library units."),
    ("perpustam", "Perbadanan Perpustakaan Awam Melaka", "Melaka", "🔵🔴⚪", "WebOPAC", "Melaka state public library corporation and heritage archives."),
    ("ppanps", "Perbadanan Perpustakaan Awam Negeri Perlis", "Perlis", "🟡🔵", "Koha OPAC", "Perlis state public library network and border community centers."),
    ("pustaka", "Pustaka Negeri Sarawak", "Sarawak", "🔴🟡⚫", "WebOPAC", "Sarawak state library and Borneo legal deposit repository."),
    ("pns", "Perpustakaan Negeri Sabah", "Sabah", "🔵⚪🔴", "WebOPAC", "Sabah state library network and North Borneo collections."),
    ("pkl", "Perpustakaan Kuala Lumpur", "W.P. Kuala Lumpur", "🔴⚪🔵", "WebOPAC", "Kuala Lumpur metropolitan public library system under DBKL."),
    ("ppj", "Perpustakaan Awam Putrajaya", "W.P. Putrajaya", "🟡🔵🔴", "WebOPAC", "Putrajaya administrative federal territory public library."),
    ("ppl", "Perpustakaan Awam Perbadanan Labuan", "W.P. Labuan", "🔴⚪🔵", "WebOPAC", "Federal Territory of Labuan public library corporation.")
]

select_options = []
for code, name, state, flag, engine, desc in LIBRARIES:
    select_options.append(f'            <option value="{code}">{flag} {code.upper()} - {name} ({state})</option>')
options_html = "\n".join(select_options)

cards = []
for code, name, state, flag, engine, desc in LIBRARIES:
    card_html = f"""      <!-- {code.upper()} Card -->
      <div class="lib-card">
        <div class="lib-card-header">
          <span class="lib-code">/{code}</span>
          <span class="status-pill status-active">Active</span>
        </div>
        <div class="lib-name">{flag} {name}</div>
        <div class="lib-state-engine"><span>{state}</span> &bull; <code>{engine}</code></div>
        <div class="lib-desc">{desc}</div>
        <a class="lib-endpoint" href="./{code}?isbn=9789831665541">
          GET ./{code}?isbn=9789831665541 &rarr;
        </a>
      </div>"""
    cards.append(card_html)
cards_html = "\n".join(cards)

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>marc-retriever: Universal Malaysian Public Libraries MARC21 Engine</title>
  <meta name="description" content="Retrieve MARC21 bibliographic records in JSON format from all Malaysian public libraries via URL query string.">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📚</text></svg>">
  <style>
    :root {{
      --bg-primary: #0a0e17;
      --bg-secondary: #131b2e;
      --bg-card: #182238;
      --bg-code: #0b1120;
      --border: #243354;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --accent: #38bdf8;
      --accent-hover: #0ea5e9;
      --accent-gold: #f59e0b;
      --accent-green: #10b981;
      --accent-rose: #f43f5e;
      --font-mono: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background-color: var(--bg-primary);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    .container {{
      width: 100%;
      max-width: 1100px;
      margin: 0 auto;
      padding: 2.5rem 1.25rem 4rem;
      flex: 1;
    }}

    header {{
      text-align: center;
      margin-bottom: 2.5rem;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(56, 189, 248, 0.12);
      color: var(--accent);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      font-size: 0.82rem;
      font-weight: 600;
      margin-bottom: 1rem;
      letter-spacing: 0.03em;
    }}
    h1 {{
      font-size: 2.4rem;
      font-weight: 800;
      color: #fff;
      letter-spacing: -0.02em;
      margin-bottom: 0.6rem;
    }}
    h1 .highlight {{
      color: var(--accent);
    }}
    .subtitle {{
      color: var(--text-muted);
      font-size: 1.05rem;
      max-width: 720px;
      margin: 0 auto;
    }}

    .search-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 2rem;
      margin-bottom: 2.5rem;
      box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
    }}
    .search-form {{
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }}
    @media (min-width: 768px) {{
      .search-form {{
        flex-direction: row;
      }}
    }}
    .select-wrapper {{
      flex: 1.2;
    }}
    .input-wrapper {{
      flex: 1.8;
    }}
    select, input[type="text"] {{
      width: 100%;
      padding: 0.9rem 1.1rem;
      background: var(--bg-code);
      border: 1px solid var(--border);
      border-radius: 10px;
      color: var(--text-main);
      font-size: 0.95rem;
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
    }}
    select:focus, input[type="text"]:focus {{
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
    }}
    button {{
      background: var(--accent);
      color: #0b1120;
      border: none;
      border-radius: 10px;
      padding: 0.9rem 1.75rem;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      transition: background-color 0.2s, transform 0.1s;
    }}
    button:hover {{
      background: var(--accent-hover);
    }}
    button:active {{
      transform: scale(0.98);
    }}

    .examples {{
      margin-top: 1rem;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .example-tag {{
      background: var(--bg-secondary);
      border: 1px solid var(--border);
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
      cursor: pointer;
      font-family: var(--font-mono);
      transition: all 0.15s;
    }}
    .example-tag:hover {{
      border-color: var(--accent);
      color: var(--accent);
    }}

    .section-title {{
      font-size: 1.3rem;
      font-weight: 700;
      margin-bottom: 1.25rem;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .section-count {{
      font-size: 0.85rem;
      font-weight: 600;
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-green);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
    }}

    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 1.25rem;
      margin-bottom: 2.5rem;
    }}
    .lib-card {{
      background: var(--bg-secondary);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.25rem;
      transition: border-color 0.2s, transform 0.15s;
      position: relative;
      display: flex;
      flex-direction: column;
    }}
    .lib-card:hover {{
      border-color: var(--accent);
      transform: translateY(-2px);
    }}
    .lib-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 0.6rem;
    }}
    .lib-code {{
      font-family: var(--font-mono);
      font-size: 0.85rem;
      background: rgba(56, 189, 248, 0.1);
      color: var(--accent);
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      font-weight: 700;
    }}
    .status-pill {{
      font-size: 0.72rem;
      padding: 0.15rem 0.5rem;
      border-radius: 9999px;
      font-weight: 700;
    }}
    .status-active {{
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-green);
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}
    .lib-name {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 0.25rem;
    }}
    .lib-state-engine {{
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-bottom: 0.6rem;
    }}
    .lib-state-engine code {{
      font-family: var(--font-mono);
      color: var(--accent-gold);
    }}
    .lib-desc {{
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.45;
      margin-bottom: 1rem;
      flex: 1;
    }}
    .lib-endpoint {{
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.8rem;
      color: var(--accent);
      text-decoration: none;
      word-break: break-all;
      background: var(--bg-code);
      padding: 0.4rem 0.6rem;
      border-radius: 6px;
      border: 1px solid var(--border);
      transition: background 0.15s, border-color 0.15s;
    }}
    .lib-endpoint:hover {{
      background: rgba(56, 189, 248, 0.1);
      border-color: var(--accent);
    }}

    .docs-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 2rem;
      margin-bottom: 2.5rem;
    }}
    .docs-card h2 {{
      font-size: 1.25rem;
      color: #fff;
      margin-bottom: 1rem;
    }}
    .docs-card p {{
      color: var(--text-muted);
      font-size: 0.95rem;
      margin-bottom: 1rem;
    }}
    .docs-card code {{
      font-family: var(--font-mono);
      color: var(--accent);
      background: var(--bg-code);
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      font-size: 0.9em;
    }}
    .endpoint-box {{
      background: var(--bg-code);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 0.85rem 1.1rem;
      font-family: var(--font-mono);
      font-size: 0.88rem;
      color: var(--accent-green);
      margin-bottom: 1rem;
      word-break: break-all;
    }}
    .endpoint-box a {{
      color: var(--accent-green);
      text-decoration: none;
    }}
    .endpoint-box a:hover {{
      text-decoration: underline;
    }}
    .badge-method {{
      background: rgba(16, 185, 129, 0.2);
      color: var(--accent-green);
      padding: 0.15rem 0.45rem;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 700;
      margin-right: 0.5rem;
    }}

    footer {{
      border-top: 1px solid var(--border);
      padding: 2rem 1.25rem;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.85rem;
    }}
    footer a {{
      color: var(--accent);
      text-decoration: none;
    }}
    footer a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>

<div class="container">
  <header>
    <div class="badge">
      <span>🇲🇾</span> Universal Malaysian Public Libraries Engine
    </div>
    <h1>marc-<span class="highlight">retriever</span></h1>
    <p class="subtitle">
      Zero-dependency, client-side web application resolving MARC21 bibliographic records in JSON, MarcEdit (.mrk), and MARCXML format across all Malaysian public libraries via clean URL query strings.
    </p>
  </header>

  <div class="search-card">
    <form class="search-form" id="searchForm" onsubmit="handleUniversalSearch(event)">
      <div class="select-wrapper">
        <select id="librarySelect">
{options_html}
        </select>
      </div>
      <div class="input-wrapper">
        <input 
          type="text" 
          id="isbnInput" 
          placeholder="Enter ISBN (e.g. 9789831665541 or 9678915006)" 
          autocomplete="off" 
          autofocus 
        />
      </div>
      <button type="submit">
        <span>🔍 Retrieve</span>
      </button>
    </form>

    <div class="examples">
      <span>Try sample ISBNs:</span>
      <span class="example-tag" onclick="quickFill('9789831665541')">9789831665541</span>
      <span class="example-tag" onclick="quickFill('9678915006')">9678915006</span>
      <span class="example-tag" onclick="quickFill('0755438140')">0755438140</span>
    </div>
  </div>

  <div class="section-title">
    <span>🏛️ Library Providers Directory</span>
    <span class="section-count">17 Active Providers</span>
  </div>
  <div class="grid">
{cards_html}
  </div>

  <div class="docs-card">
    <h2>📖 Universal URL Query String API</h2>
    <p>Retrieve MARC records for any supported Malaysian public library using the clean path format <code>/{code}?isbn=&lt;ISBN&gt;</code>:</p>
    
    <div class="endpoint-box">
      <div>
        <span class="badge-method">GET</span>
        <a href="./pnm?isbn=9789831665541" target="_blank">
          https://pustaka-terbuka.github.io/marc-retriever/pnm?isbn=9789831665541
        </a>
      </div>
    </div>

    <div class="endpoint-box">
      <div>
        <span class="badge-method">GET</span>
        <a href="./ppas?isbn=9678915006" target="_blank">
          https://pustaka-terbuka.github.io/marc-retriever/ppas?isbn=9678915006
        </a>
      </div>
    </div>

    <p>Append <code>&raw=true</code> for raw unstyled JSON output (ideal for machine ingestion, curl, and Python requests):</p>
    <div class="endpoint-box">
      <div>
        <span class="badge-method">GET</span>
        <a href="./pnm?isbn=9789831665541&raw=true" target="_blank">
          https://pustaka-terbuka.github.io/marc-retriever/pnm?isbn=9789831665541&raw=true
        </a>
      </div>
    </div>
  </div>
</div>

<footer>
  <p>
    Powered by <a href="https://github.com/pustaka-terbuka" target="_blank">Pustaka Terbuka</a> &bull; Open Metadata & Public Library Technology &bull;
    <a href="https://github.com/pustaka-terbuka/marc-retriever" target="_blank">GitHub Repository</a>
  </p>
</footer>

<script>
  function handleUniversalSearch(e) {{
    e.preventDefault();
    const lib = document.getElementById("librarySelect").value || "pnm";
    const isbn = document.getElementById("isbnInput").value.trim().replace(/[-\s]/g, "");
    if (!isbn) return;

    window.location.href = `./${{lib}}?isbn=${{encodeURIComponent(isbn)}}`;
  }}

  function quickFill(isbn) {{
    document.getElementById("isbnInput").value = isbn;
    const lib = document.getElementById("librarySelect").value || "pnm";
    window.location.href = `./${{lib}}?isbn=${{encodeURIComponent(isbn)}}`;
  }}

  // Auto-redirect if accessed at root with query string (?isbn=...&lib=...)
  window.addEventListener("DOMContentLoaded", () => {{
    const params = new URLSearchParams(window.location.search);
    const isbn = params.get("isbn") || params.get("q");
    const lib = params.get("lib") || params.get("library") || "pnm";
    const raw = params.get("raw");

    if (isbn) {{
      let target = `./${{lib}}?isbn=${{encodeURIComponent(isbn)}}`;
      if (raw) target += `&raw=${{encodeURIComponent(raw)}}`;
      window.location.replace(target);
    }}
  }});
</script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print("Updated root index.html with all 17 public libraries!")
