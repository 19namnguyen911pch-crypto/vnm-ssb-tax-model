# -*- coding: utf-8 -*-
import re

EN = "Manuscript_draft_v1.md"
VI = "Ban_thao_Tieng_Viet.md"
DOI = "https://doi.org/10.5281/zenodo.23852996"

pairs_en = [
 ("was registered on OSF on \u27e6date\u27e7 before the main model runs; deviations are recorded in Appendix D.\u27e6TBD-0\u27e7",
  "is archived with the analytic code at " + DOI + ". Because the model was run before the protocol was deposited, this study is not a pre-registration; the departures from the protocol as originally drafted are recorded in Appendix D."),
 ("from January 2000 to \u27e6date\u27e7", "from January 2000 to 1 November 2026"),
 ("- **Appendix D.** Deviation log relative to the OSF registration.",
  "- **Appendix D.** Deviation log relative to the archived protocol."),
 ("deposited with the protocol on OSF and updated until submission.",
  "deposited with the protocol at " + DOI + "."),
 ("Methods, *Uncertainty and sensitivity analysis*; OSF registration",
  "Methods, *Uncertainty and sensitivity analysis*; archived protocol"),
 ("**5 ch\u1ed7 th\u00f4ng tin h\u00e0nh ch\u00ednh:** t\u00e1c gi\u1ea3, CRediT, COI, t\u00e0i tr\u1ee3, m\u00e3 OSF.",
  "**C\u00f2n l\u1ea1i:** t\u00ean ng\u01b0\u1eddi \u0111\u1ecdc m\u00e3 \u0111\u1ed9c l\u1eadp (\u27e6TBD-37\u27e7)."),
 ("The protocol, including the analysis plan and the parameter feasibility assessment,",
  "The full protocol, including the analysis plan and the parameter feasibility assessment,"),
]

pairs_vi = [
 ("\u0111\u01b0\u1ee3c \u0111\u0103ng k\u00fd tr\u00ean OSF ng\u00e0y \u27e6ng\u00e0y\u27e7 tr\u01b0\u1edbc khi ch\u1ea1y m\u00f4 h\u00ecnh ch\u00ednh; c\u00e1c sai l\u1ec7ch \u0111\u01b0\u1ee3c ghi \u1edf Ph\u1ee5 l\u1ee5c D.\u27e6TBD-0\u27e7",
  "\u0111\u01b0\u1ee3c l\u01b0u c\u00f9ng m\u00e3 ph\u00e2n t\u00edch t\u1ea1i " + DOI + ". V\u00ec m\u00f4 h\u00ecnh \u0111\u00e3 \u0111\u01b0\u1ee3c ch\u1ea1y tr\u01b0\u1edbc khi protocol \u0111\u01b0\u1ee3c l\u01b0u tr\u1eef, nghi\u00ean c\u1ee9u n\u00e0y kh\u00f4ng ph\u1ea3i l\u00e0 \u0111\u0103ng k\u00fd tr\u01b0\u1edbc; c\u00e1c sai l\u1ec7ch so v\u1edbi protocol so\u1ea1n ban \u0111\u1ea7u \u0111\u01b0\u1ee3c ghi \u1edf Ph\u1ee5 l\u1ee5c D."),
 ("t\u1eeb th\u00e1ng 1/2000 \u0111\u1ebfn \u27e6ng\u00e0y\u27e7", "t\u1eeb th\u00e1ng 1/2000 \u0111\u1ebfn 1/11/2026"),
 ("- **Ph\u1ee5 l\u1ee5c D.** Nh\u1eadt k\u00fd sai l\u1ec7ch so v\u1edbi \u0111\u0103ng k\u00fd OSF.",
  "- **Ph\u1ee5 l\u1ee5c D.** Nh\u1eadt k\u00fd sai l\u1ec7ch so v\u1edbi protocol \u0111\u00e3 l\u01b0u tr\u1eef."),
 ("\u0111\u01b0\u1ee3c l\u01b0u c\u00f9ng protocol tr\u00ean OSF v\u00e0 c\u1eadp nh\u1eadt \u0111\u1ebfn khi n\u1ed9p b\u00e0i.",
  "\u0111\u01b0\u1ee3c l\u01b0u c\u00f9ng protocol t\u1ea1i " + DOI + "."),
 ("Ph\u01b0\u01a1ng ph\u00e1p, *B\u1ea5t \u0111\u1ecbnh v\u00e0 ph\u00e2n t\u00edch \u0111\u1ed9 nh\u1ea1y*; \u0111\u0103ng k\u00fd OSF",
  "Ph\u01b0\u01a1ng ph\u00e1p, *B\u1ea5t \u0111\u1ecbnh v\u00e0 ph\u00e2n t\u00edch \u0111\u1ed9 nh\u1ea1y*; protocol \u0111\u00e3 l\u01b0u tr\u1eef"),
 ("**5 ch\u1ed7 th\u00f4ng tin h\u00e0nh ch\u00ednh:** t\u00e1c gi\u1ea3, CRediT, xung \u0111\u1ed9t l\u1ee3i \u00edch, t\u00e0i tr\u1ee3, m\u00e3 OSF.",
  "**C\u00f2n l\u1ea1i:** t\u00ean ng\u01b0\u1eddi \u0111\u1ecdc m\u00e3 \u0111\u1ed9c l\u1eadp."),
 ("Protocol, g\u1ed3m k\u1ebf ho\u1ea1ch ph\u00e2n t\u00edch v\u00e0 \u0111\u00e1nh gi\u00e1 kh\u1ea3 thi tham s\u1ed1,",
  "Protocol \u0111\u1ea7y \u0111\u1ee7, g\u1ed3m k\u1ebf ho\u1ea1ch ph\u00e2n t\u00edch v\u00e0 \u0111\u00e1nh gi\u00e1 kh\u1ea3 thi tham s\u1ed1,"),
]

for path, pairs in [(EN, pairs_en), (VI, pairs_vi)]:
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        if a not in s:
            print("  MISS:", path, a[:50])
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
    left = sorted(set(re.findall(r"\u27e6[^\u27e7]*\u27e7", s)))
    print(path, "remaining:", left)
