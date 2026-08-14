// === JSON Data Binding Helpers ===
// Python: computation + units (ColumnDef SSOT)
// Typst: German number formatting + rendering

/// Format a number with German decimal comma and fixed decimal places.
/// #de(429.6) → "429,60"
/// #de(429.6, precision: 0) → "430"
/// #de(28.0, precision: 2) → "28,00"
#let de(value, precision: 2) = {
  if value == none {
    return "—"
  }
  let rounded = calc.round(float(value), digits: precision)
  if precision == 0 {
    return str(int(rounded))
  }
  let s = str(rounded)
  if not s.contains(".") { s = s + ".0" }
  let parts = s.split(".")
  let frac = parts.at(1)
  while frac.len() < precision {
    frac = frac + "0"
  }
  parts.at(0) + "," + frac
}

/// Render a ResultValue dict {"value": …, "unit": …, "precision": …}.
/// #val(res.force_max) → "429,60 kN"
/// #val(res.force_max, unit: false) → "429,60"
#let val(rv, unit: true) = {
  if rv == none {
    return "—"
  }
  if type(rv) == dictionary and "value" in rv {
    let prec = if "precision" in rv { rv.precision } else { 2 }
    let formatted = de(rv.value, precision: prec)
    if unit and "unit" in rv and rv.unit != "—" and rv.unit != "" {
      [#formatted~#rv.unit]
    } else {
      formatted
    }
  } else {
    de(rv)
  }
}

/// Render a percentage ResultValue.
/// #pct(res.safety_margin) → "29,24 %"
#let pct(rv) = {
  if rv == none {
    return "—"
  }
  if type(rv) == dictionary and "value" in rv {
    let prec = if "precision" in rv { rv.precision } else { 2 }
    let formatted = de(rv.value, precision: prec)
    [#formatted~%]
  } else {
    let formatted = de(rv)
    [#formatted~%]
  }
}
