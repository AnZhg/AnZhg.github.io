# Created by Claude (Opus 5.5) on 2026-10-26.
#
# Writes strings/<language>.md, one table a language of every string Nomogram shows: the English, the translation, and
# where it shows, from the app's string catalogs. Run it after the catalogs change:
#
#   python3 -I tools/strings_tables.py <path to the Nomogram repository>
import json, os, sys

app = sys.argv[1]
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOGS = ["App/Mac/mul.lproj/MainMenu.xcstrings", "App/Mac/Localizable.xcstrings", "App/Shared/Shared.xcstrings", "App/Mac/InfoPlist.xcstrings"]
NAMES = {"zh-Hans": "Chinese, Simplified", "zh-Hant": "Chinese, Traditional (Taiwan)", "zh-HK": "Chinese, Traditional (Hong Kong)", "ja": "Japanese", "es": "Spanish", "pt": "Portuguese (Brazil)", "de": "German", "fr": "French", "it": "Italian"}

def text(localization):
    """A localization's words: its string, or its plural forms one after another."""
    if localization is None:
        return ""
    if "stringUnit" in localization:
        return localization["stringUnit"]["value"]
    forms = localization.get("variations", {}).get("plural", {})
    return " / ".join(f"{form}: {unit['stringUnit']['value']}" for form, unit in sorted(forms.items()))

def cell(value):
    return value.replace("|", "\\|").replace("\n", " ")

rows = []
for path in CATALOGS:
    catalog = json.load(open(os.path.join(app, path), encoding="utf-8"))
    for key, entry in sorted(catalog["strings"].items(), key=lambda item: item[0].lower()):
        if entry.get("shouldTranslate") is False:
            continue
        localizations = entry.get("localizations", {})
        english = text(localizations.get("en")) or key
        where = "Menu bar" if path.endswith("MainMenu.xcstrings") else entry.get("comment", "").split("\n")[0]
        rows.append((english, where, localizations))
os.makedirs(os.path.join(here, "strings"), exist_ok=True)
for language, name in NAMES.items():
    lines = [f"# {name} (`{language}`)", "", "Every string Nomogram shows, with where it shows. To suggest better words, [open the form](https://github.com/AnZhg/nomogram-translations/issues/new?template=translation.yml).", "", "| English | " + name + " | Where |", "|---|---|---|"]
    for english, where, localizations in rows:
        lines.append(f"| {cell(english)} | {cell(text(localizations.get(language)))} | {cell(where)} |")
    open(os.path.join(here, "strings", f"{language}.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(language, len(rows), "strings")
