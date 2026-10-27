<!-- Created by Claude (Opus 5.5) on 2026-10-26. -->
# Nomogram's translations

Nomogram is a Mac app for programming with flowcharts: you build a program as a chart, run it step by step, and export
it as Swift. This is where its translations are reported on and improved. Nomogram's own source is not here.

## Languages

Each language's page lists every string Nomogram shows, with its translation and where it shows.

| Language | Folder | Status |
|---|---|---|
| English | `en` | The original |
| [Chinese, Simplified](strings/zh-Hans.md) | `zh-Hans` | Reviewed by the developer |
| [Chinese, Traditional (Taiwan)](strings/zh-Hant.md) | `zh-Hant` | Reviewed by the developer |
| [Chinese, Traditional (Hong Kong)](strings/zh-HK.md) | `zh-HK` | Reviewed by the developer |
| [Japanese](strings/ja.md) | `ja` | Drafted, not yet reviewed by a native speaker |
| [Spanish](strings/es.md) | `es` | Drafted, not yet reviewed by a native speaker |
| [Portuguese (Brazil)](strings/pt.md) | `pt` | Drafted, not yet reviewed by a native speaker |
| [German](strings/de.md) | `de` | Drafted, not yet reviewed by a native speaker |
| [French](strings/fr.md) | `fr` | Drafted, not yet reviewed by a native speaker |
| [Italian](strings/it.md) | `it` | Drafted, not yet reviewed by a native speaker |

## Report a problem or suggest better words

In Nomogram, choose **Help > Report a Translation Problem…**. It opens a short form here, already filled in with your
language and the app's version. Or [open the form](https://github.com/AnZhg/nomogram-translations/issues/new?template=translation.yml)
yourself. One problem per report, please; a screenshot helps. You need a GitHub account to report.

## What stays as it is

- **Swift.** A program in Nomogram is Swift, so code stays Swift in every language: `var`, `for`, `in`, `while`,
  `repeat`, `return`, `break`, `continue`, types such as `Int` and `String`, and examples such as `x > 0`. The words
  around the code are translated: Input, Output, Repeat … times, and the hints in empty fields.
- **Numbers**, which are written as code writes them in every language: 0.5, not 0,5. The one exception is the
  call depth in Preferences, which you type, so it is written your region's way (10.000 in Germany).
- **The app's name**, Nomogram, in every language.
