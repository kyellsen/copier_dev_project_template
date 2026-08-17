"""Definition of ColumnDef — Single Source of Truth (SSOT) for data columns and symbols."""

from __future__ import annotations

import re

from pydantic import BaseModel, Field

_GREEK_LETTERS = (
    "alpha|beta|gamma|delta|epsilon|zeta|eta|theta|iota|kappa|lambda|mu|"
    "nu|xi|omicron|pi|rho|sigma|tau|upsilon|phi|chi|psi|omega|"
    "Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega"
)
_GREEK_RE = re.compile(rf"\b({_GREEK_LETTERS})\b")


def _typst_to_mathtext(typst_sym: str) -> str:
    """Convert a Typst math symbol to matplotlib-compatible mathtext syntax.

    Handles:
    - Subscripts with quoted strings: `F_"max"` → `F_{max}`
    - Subscripts with simple identifiers: `F_max` → `F_{max}`
    - Greek letters: `alpha` → `\\alpha`
    """
    # 1. Descriptive subscript: _"..." → _{...}
    s = re.sub(r'_"([^"]+)"', r"_{\1}", typst_sym)
    # 2. Identifier subscript: _xyz → _{xyz} (if length > 1)
    s = re.sub(r"_([a-zA-Z0-9]{2,})", r"_{\1}", s)
    # 3. Greek letters: alpha → \alpha
    s = _GREEK_RE.sub(r"\\\1", s)
    return s


class ColumnDef(BaseModel, frozen=True):
    """Definition of a single data column / physical quantity.

    This is the central metadata record for measured or computed variables.
    It feeds plot axis labels, table headers, formula symbols, and
    DataFrame column names from a single definition.

    Attributes:
        name: Identifier / DataFrame column name, e.g. ``"force_max"``.
        dtype: Data type string, e.g. ``"Float64"``, ``"Datetime"``.
        unit: Physical unit, e.g. ``"kN"``, ``"m"``, ``"°"``, ``"s"``.
        descriptions: Multilingual descriptions (keyed by ISO 639-1, e.g. ``"de"``, ``"en"``).
        labels: Multilingual short labels (keyed by ISO 639-1).
        symbol: Math symbol in Typst notation, e.g. ``"F_\"max\""``, ``"alpha"``.
        context: Namespace for symbol grouping/disambiguation, e.g. ``"mechanics"``, ``"geometry"``.
    """

    name: str
    dtype: str = "Float64"
    unit: str = "—"
    descriptions: dict[str, str] = Field(default_factory=dict)
    labels: dict[str, str] = Field(default_factory=dict)
    symbol: str = ""
    context: str = "general"

    def axis_label(self, lang: str = "de") -> str:
        """Generate a plot axis label like ``'Kraft [kN]'``."""
        label = self.labels.get(lang, self.labels.get("en", self.name))
        if self.unit and self.unit != "—":
            return f"{label} [{self.unit}]"
        return label

    def plot_label(self, lang: str = "de") -> str:
        """Generate a matplotlib axis label with math like ``'Kraft $F_{max}$ (kN)'``."""
        label = self.labels.get(lang, self.labels.get("en", self.name))
        parts = [label]
        if self.symbol:
            mathtext = _typst_to_mathtext(self.symbol)
            parts.append(f"${mathtext}$")
        if self.unit and self.unit != "—":
            parts.append(f"({self.unit})")
        return " ".join(parts)
