#!/usr/bin/env python3
"""Ensambla index.html a partir de src/.

- template.html        : marcado y logica (UTF-8, legible)
- prompts-*.js         : biblioteca, un archivo por area, en el orden de AREAS_ORDER. Cada prompt es
                         {a:"clave", s:"Subarea", t:"titulo", r:"...", c:"...", i:"..."}
- rondas.js            : rondas del ejercicio
- assets/*.woff2, .png : tipografias y logos (Next Leap y UPTC), se incrustan en base64 (el hero es solo CSS)

El resultado es un unico archivo ASCII puro: fuera de <script> los caracteres
no ASCII van como entidades HTML (&#NNNN;) y dentro de <script> como \\uXXXX.
Uso:  python3 src/build.py [--estricto]
      Sin la bandera, un archivo de area ausente se avisa y se omite.
      Con --estricto, falta de archivos, subareas vacias o claves cruzadas detienen el build.
"""
import base64, pathlib, re, sys

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent
OUT = ROOT / "index.html"

AREAS_ORDER = ["civil", "comercial", "laboral", "penal", "administrativo", "constitucional",
               "tributario", "ambiental", "digital", "internacional", "practica"]
ESTRICTO = "--estricto" in sys.argv

def b64(path):
    return base64.b64encode(path.read_bytes()).decode("ascii")

def font_css():
    faces = [("IBM Plex Mono", 400, "ibmplexmono-400.woff2"),
             ("IBM Plex Mono", 500, "ibmplexmono-500.woff2"),
             ("Inter", 400, "inter-400.woff2"),
             ("Inter", 500, "inter-500.woff2"),
             ("Inter", 600, "inter-600.woff2")]
    out = []
    for fam, w, fn in faces:
        out.append("@font-face{font-family:'%s';font-style:normal;font-weight:%d;font-display:swap;"
                   "src:url(data:font/woff2;base64,%s) format('woff2');}" % (fam, w, b64(SRC / "assets" / fn)))
    return "\n".join(out)

def prompts_js():
    parts = []
    for a in AREAS_ORDER:
        p = SRC / f"prompts-{a}.js"
        if not p.exists():
            if ESTRICTO:
                sys.exit(f"falta {p}")
            print(f"aviso: falta {p.name}, se omite", file=sys.stderr)
            continue
        txt = p.read_text(encoding="utf-8").strip()
        if ESTRICTO:
            for m in re.finditer(r'^\{a:"([^"]*)",s:"([^"]*)"', txt, flags=re.M):
                if m.group(1) != a:
                    sys.exit(f"{p.name}: prompt con area {m.group(1)!r}, se esperaba {a!r}")
                if not m.group(2).strip():
                    sys.exit(f"{p.name}: prompt con subarea vacia")
            if len(re.findall(r'^\{a:"', txt, flags=re.M)) != len(re.findall(r'^\{a:"[^"]*",s:"[^"]+"', txt, flags=re.M)):
                sys.exit(f"{p.name}: hay prompts sin subarea (s:)")
        parts.append(txt)
    return "\n\n".join(parts)

def esc_html(s):
    return "".join(c if ord(c) < 128 else "&#%d;" % ord(c) for c in s)

def esc_js(s):
    out = []
    for c in s:
        o = ord(c)
        if o < 128:
            out.append(c)
        elif o <= 0xFFFF:
            out.append("\\u%04x" % o)
        else:
            o -= 0x10000
            out.append("\\u%04x\\u%04x" % (0xD800 + (o >> 10), 0xDC00 + (o & 0x3FF)))
    return "".join(out)

def asciify(html):
    # Separa bloques <script>...</script> del resto y escapa cada uno a su manera.
    out, pos = [], 0
    for m in re.finditer(r"<script\b[^>]*>.*?</script>", html, flags=re.S):
        out.append(esc_html(html[pos:m.start()]))
        out.append(esc_js(m.group(0)))
        pos = m.end()
    out.append(esc_html(html[pos:]))
    return "".join(out)

def main():
    tpl = (SRC / "template.html").read_text(encoding="utf-8")
    prompts = prompts_js()
    html = (tpl.replace("{{FONT_CSS}}", font_css())
               .replace("{{LOGO_PNG}}", "data:image/png;base64," + b64(SRC / "assets" / "nextleap-mark.png"))
               .replace("{{UPTC_PNG}}", "data:image/png;base64," + b64(SRC / "assets" / "uptc-logo.png"))
               .replace("{{PROMPTS}}", prompts)
               .replace("{{RONDAS}}", (SRC / "rondas.js").read_text(encoding="utf-8").strip()))
    left = re.findall(r"\{\{[A-Z_]+\}\}", html)
    if left:
        sys.exit(f"placeholders sin resolver: {left}")
    html = asciify(html)
    assert all(ord(c) < 128 for c in html), "quedaron caracteres no ASCII"
    OUT.write_text(html, encoding="ascii")
    n = len(re.findall(r'^\{a:"', prompts, flags=re.M))
    print(f"ok: {OUT} ({OUT.stat().st_size:,} bytes, {n} prompts)")

if __name__ == "__main__":
    main()
