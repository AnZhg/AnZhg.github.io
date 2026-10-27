<!-- Created by Claude (Opus 5.5) on 2026-10-26. -->
# anzhg.github.io

The source of [anzhg.github.io](https://anzhg.github.io), the public pages of AnZhg's apps, and the place their bugs and
translation problems are reported, as issues of this repository.

- `nomogram/`: [Nomogram](https://anzhg.github.io/nomogram/)'s pages. `nomogram/report/<kind>/` forwards to the issue
  form `.github/ISSUE_TEMPLATE/nomogram-<kind>.yml`, passing on the query, so the app links to the page and the form can
  move without breaking a version already shipped.
- `tools/strings_tables.py <path to the Nomogram repository>` writes `nomogram/translations/<language>.md` from the
  app's string catalogs. Run it when they change.
