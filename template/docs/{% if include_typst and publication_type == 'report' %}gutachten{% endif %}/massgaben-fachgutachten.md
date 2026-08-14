# Maßgaben für die Erstellung von Fachgutachten — Schwerpunkt Baumgutachten

**Zweck dieses Dokuments:** Verbindliche Arbeitsgrundlage für einen KI-Agenten, der bei der Erstellung, Prüfung oder Überarbeitung von Fachgutachten unterstützt.
**Geltungsbereich:** Allgemeine Anforderungen an Gutachten in Deutschland (Teil A–C) sowie fachspezifische Anforderungen an Baumgutachten zu Verkehrssicherheit, Baumschutz und Gehölzwert (Teil D–F).
**Stand:** August 2026. Regelwerksstände sind vor Verwendung zu verifizieren (siehe Teil F).
**Pflege:** Single Source of Truth ist `copier_dev_project` (`template/docs/…/massgaben-fachgutachten.md`); Änderungen dort vornehmen und per `copier update` in die Gutachten-Repos nachziehen.

---

## 0. Grundregeln für den Agenten

1. **Keine erfundenen Tatsachen.** Der Agent erfindet niemals Messwerte, Baumdaten, Ortstermindaten, Fundstellen, Aktenzeichen oder Literaturangaben. Fehlende Angaben werden als `[ERGÄNZEN: …]` markiert und am Ende der Ausgabe als Liste offener Punkte ausgegeben.
2. **Keine erfundenen Rechtsquellen.** Urteilsaktenzeichen, Paragrafen und Normfassungen werden nur übernommen, wenn sie belegt sind. Im Zweifel: Platzhalter setzen und Verifikation anfordern.
3. **Der Agent begutachtet nicht.** Er formuliert, strukturiert und prüft. Die fachliche Beurteilung, die Sachkunde und die Verantwortung liegen ausschließlich beim unterzeichnenden Sachverständigen.
4. **Regelwerksstände immer prüfen.** Vor jedem Zitat eines Regelwerks ist der aktuelle Ausgabestand zu verifizieren (Teil F enthält den Stand August 2026 und die bekannten Fallstricke).
5. **Bei Unsicherheit nachfragen**, statt zu glätten. Eine unklare Aussage im Gutachten ist gravierender als eine Rückfrage.

---

## Teil A — Rechtlicher Rahmen

Es existiert **keine DIN-Norm „Gutachten"**. Die Anforderungen ergeben sich aus:

| Kontext | Maßgebliche Grundlagen |
|---|---|
| Gerichtsgutachten | §§ 402–414 ZPO, insb. § 407a ZPO (Prüf- und Hinweispflichten, Delegationsverbot im Kernbereich, Kenntlichmachung von Mitarbeitenden), § 404a ZPO (Leitung durch das Gericht); §§ 72 ff. StPO; § 98 VwGO; Vergütung nach JVEG |
| Privatgutachten | Werkvertragsrecht §§ 631 ff. BGB; Mängelhaftung §§ 633 ff., 280 BGB; ggf. Dritthaftung (Vertrag mit Schutzwirkung, § 311 Abs. 3 BGB) |
| Berufsrecht | § 36 GewO (öffentliche Bestellung und Vereidigung); Muster-Sachverständigenordnung des DIHK nebst Richtlinien zur SVO; Bestellungsvoraussetzungen des IfS; DIN EN ISO/IEC 17024 für zertifizierte Sachverständige |
| Nebenpflichten | DSGVO bei personenbezogenen Daten und Fotos; Urheber- und Verwertungsrechte am Gutachten |

**Leitsatz (§ 9 Abs. 3 SVO):** Aufträge sind unter Berücksichtigung des aktuellen Standes von Wissenschaft, Technik und Erfahrung mit der Sorgfalt eines ordentlichen Sachverständigen zu erledigen. Die tatsächlichen Grundlagen der fachlichen Beurteilung sind sorgfältig zu ermitteln, die Ergebnisse nachvollziehbar zu begründen.

**Leitsatz (Nr. 9.3.7 Richtlinien zur SVO):** Gutachten sind systematisch aufzubauen, übersichtlich zu gliedern, nachvollziehbar zu begründen und auf das Wesentliche zu beschränken. Ist eine Schlussfolgerung nicht zwingend, sondern nur naheliegend, ist dies deutlich zum Ausdruck zu bringen.

**Definition:** Ein Gutachten ist die fachliche Beurteilung eines vorgegebenen oder selbst ermittelten Sachverhalts, die **für den fachlichen Laien nachvollziehbar** und **für den Fachmann nachprüfbar** ist.

---

## Teil B — Inhaltliche Qualitätsanforderungen

Diese Kriterien sind bei jedem erzeugten oder geprüften Text anzuwenden:

| Grundsatz | Umsetzung |
|---|---|
| **Auftragsbindung** | Alle gestellten Fragen beantworten — und keine darüber hinaus. Erkenntnisse jenseits des Auftrags bzw. Beweisbeschlusses gehören nicht ins Gutachten (bei Privatauftrag ggf. gesonderter Hinweis an den Auftraggeber). |
| **Keine Rechtsanwendung** | Rechtliche Würdigungen sind bei Gerichtsgutachten strikt zu unterlassen. Bei privater Beauftragung allenfalls als ausdrücklich gekennzeichnete untergeordnete Nebenleistung. |
| **Tatsachentrennung** | Strikt unterscheiden: **Anknüpfungstatsachen** (vom Auftraggeber/Gericht vorgegeben) — **Befundtatsachen** (eigene Feststellung) — **Zusatztatsachen** (Angaben Dritter). Jede Tatsache muss ihrer Quelle zuordenbar sein. |
| **Beschreiben ≠ Bewerten** | Erst vollständig beschreiben (Kapitel „Ergebnisse"), dann bewerten (Kapitel „Schlussfolgerungen"). Niemals vermischen. |
| **Nachvollziehbarkeit** | Jede Schlussfolgerung mit erkennbarem Herleitungsweg. Verweise auf Handakten oder externe Unterlagen ersetzen die Darstellung im Gutachten nicht. |
| **Methodentransparenz** | Verfahren, Geräte, Messbedingungen, Literatur und beteiligte Personen offenlegen. |
| **Ehrliche Unsicherheit** | Ernsthaft in Betracht kommende Alternativlösungen darlegen und gegeneinander abwägen; Wahrscheinlichkeitsgrade und Ergebnisgrenzen benennen; keine Vorspiegelung nicht vorhandener Sicherheiten. |
| **Unparteilichkeit** | Klarheit, Unparteilichkeit, methodische Folgerichtigkeit. Keine ergebnisorientierte Formulierung zugunsten einer Partei. |
| **Sprache** | Fachvokabular vermeiden oder erklären. Zahlenwerte immer mit Einheit. Bilder, Skizzen und Grafiken ergänzen die verbale Beschreibung, ersetzen sie nie. |
| **Bezeichnung der Leistung** | Ist keine Begutachtung geschuldet, ist die Leistung auch so zu benennen (Stellungnahme, Schadensbericht, Bewertung). Die Bezeichnung „Kurzgutachten" ist zu vermeiden. |

---

## Teil C — Pflichtangaben (Metadaten) und Aufbau

### C.1 Pflichtangaben

Soweit sich aus dem Auftrag nichts anderes ergibt, muss ein Gutachten enthalten:

- [ ] Name des Sachverständigen, ggf. Firma, **Qualifikationen im Hinblick auf die Sachkunde**, vollständige Kontaktdaten
- [ ] Zweck und beabsichtigte bzw. vereinbarte Verwendung des Gutachtens
- [ ] Auftraggeber; bei Gerichtsauftrag zusätzlich Aktenzeichen, Parteien, Parteivertreter
- [ ] Inhalt des Sachverständigenauftrags bzw. Wiedergabe des Beweisbeschlusses
- [ ] Einzelheiten der Ortsbesichtigungen und Untersuchungen: **Datum, Zeitpunkt, Dauer, Namen der Anwesenden**
- [ ] Angaben zu beteiligten Mitarbeitenden oder Dritten und zur Art ihrer Beteiligung
- [ ] Verwendete Literatur und sonstige Quellen
- [ ] Zusammenfassung der Schlussfolgerungen, verständlich für Nichtfachleute
- [ ] Unterschrift, ggf. Stempel; bei elektronischer Übermittlung Schutz von Inhalt und Daten

### C.2 Ergänzende Formalia (Praxisstandard)

- [ ] Gutachtennummer und Gutachtendatum
- [ ] Seitenzählung im Format „Seite x von y"
- [ ] Versions-/Bearbeitungsstand, Anzahl der Ausfertigungen
- [ ] Verwertungsvorbehalt bzw. Nutzungsrechte gemäß vertraglicher Vereinbarung
- [ ] Anlagen- und Abbildungsverzeichnis
- [ ] Fotodokumentation mit fortlaufender Nummer, Aufnahmedatum, Blickrichtung/Standort, Urheber
- [ ] Bei Gemeinschaftsgutachten: eindeutige Kenntlichmachung, wer welchen Teil bearbeitet hat
- [ ] Hinweis auf die öffentliche Bestellung, sofern der Auftrag im Bestellungsgebiet liegt — **kein** solcher Hinweis bei Aufträgen außerhalb des Bestellungsgebietes

### C.3 Verbindlicher Aufbau (kanonische Gliederung)

```
1. Deckblatt
   - Ersteller*In (Name, ggf. Firma, Anschrift, Kontakt; Qualifikation, sofern angegeben)
   - Dokumentart-Label und Titel, Gegenstand
   - Auftraggeber*In (Gericht + Aktenzeichen + Verfahrensbeteiligte / privat)
   - Gutachten-Nr., Stichtag, Flur/Flurstück, ggf. Ausfertigungen
2. Verzeichnisse (Inhalt; Abbildungen/Tabellen; Anlagen im Anhang)
3. Auftrag (und Anlass)
   - Beauftragung (durch wen, wann, Liefertermin), Anlass, Zweck und Verwendung
   - Fragestellung; bei Gerichtsauftrag Wiedergabe des Beweisbeschlusses
4. Grundlagen
   - Sachverhalt, Unterlagen und Bezugsgrundlagen, Vorgutachten
   - Rechtlicher Rahmen (kommunale Baumschutzsatzung, BNatSchG, Landesrecht)
   - Ortstermine: Datum, Zeitpunkt, Dauer, Anwesende
5. Methodik
   - Begriffsdefinitionen, Verfahren, Geräte, Untersuchungsbedingungen, Verfahrensgrenzen
6. Ergebnisse (rein beschreibend)
   - Standort/Umfeld, Baumdaten, Ergebnisse je Themenfeld
   - Pflicht-Unterabschnitt: Artenschutzrechtliche Prüfung
7. Schlussfolgerungen (und Maßnahmen)
   - Beurteilung ausschließlich des beauftragten Sachverhalts; Maßnahmen mit Fristen
8. Zusammenfassung (für Nichtfachleute verständlich)
9. Unterschrift (Ort, Datum, Name; ggf. Qualifikation und Stempel)
10. Anhang (Anlagenverzeichnis, Tabellen, Karten, Fotos, Rohdaten)
```

Begriffskonvention: Die Kapitel heißen **„Ergebnisse"** (nicht „Befund") und **„Schlussfolgerungen"** (nicht „Sachverständige Würdigung"); „Schlussfolgerungen und Maßnahmen" sind **ein** Kapitel. Die juristischen Fachbegriffe aus Teil B (Anknüpfungs-/Befund-/Zusatztatsachen) bleiben davon unberührt. Ein abweichender Aufbau ist je nach Auftragsgestaltung zulässig, muss aber die Anforderungen aus Teil B erfüllen.

### C.4 Kanonische Dateistruktur (Typst) und Standard-Beschriftungen

| Datei | Kapitel | Pflichtinhalte |
|---|---|---|
| `chapters/01_auftrag_und_anlass.typ` | Auftrag und Anlass | Beauftragung, Anlass, Fragestellung, Zweck/Verwendung |
| `chapters/02_grundlagen.typ` | Grundlagen | Sachverhalt, Unterlagen/Bezugsgrundlagen, rechtlicher Rahmen, Ortstermine |
| `chapters/03_methodik.typ` | Methodik | Begriffe, Verfahren, Geräte, Bedingungen, Verfahrensgrenzen |
| `chapters/04_ergebnisse.typ` | Ergebnisse | beschreibend; Standort, Baumdaten (CSV), Artenschutzprüfung |
| `chapters/05_schlussfolgerungen.typ` | Schlussfolgerungen und Maßnahmen | Beurteilung, Maßnahmen mit Fristen, mildere Mittel, Kontrollintervall, Restrisiko, Gültigkeitshinweis |
| `chapters/06_zusammenfassung.typ` | Zusammenfassung | laienverständliche Antworten auf die Fragestellungen |
| `blocks/signature.typ` | Unterschrift | Ort, Datum, Unterschriftslinie, Name, ggf. Qualifikation |

**Standard-Beschriftungen (verbindlich):** „Auftraggeber\*In", „Gutachten-Nr.", „Stichtag". Zulässige Werte für das Dokumentart-Label (`my-doc-label`): „Gutachten", „Baumgutachten", „Stellungnahme", „Bericht" — **niemals „Kurzgutachten"** (siehe Teil B, Bezeichnung der Leistung). Qualifikation (`my-qualification`) und Ausfertigungen (`my-copies`) werden nur gerendert, wenn gesetzt (`none` = ausgeblendet).

---

## Teil D — Fachspezifische Anforderungen: Baumgutachten

### D.1 Aufnahmedaten je Baum (Pflichtfelder)

Die Pflichtfelder sind zugleich das Spaltenschema des Baumkatasters (`publication/tables/baumdaten.csv`, validiert per pydantic-Schema, `just check-data`). Ein Einzelbaumgutachten ist der Fall N = 1 derselben Struktur.

**Objektidentität**
- Baumnummer / Katasterbezug
- Standort: Adresse und Koordinaten (Angabe des Bezugssystems), Flurstück
- Eigentümer bzw. Verkehrssicherungspflichtiger
- Baumart mit wissenschaftlichem Namen

**Baumdaten**
- Stammumfang **mit Angabe der Messhöhe** (Standard 1,00 m), ggf. BHD
- Baumhöhe, Kronendurchmesser, Kronenansatzhöhe
- Entwicklungsphase
- Vitalitätsstufe **unter Benennung der verwendeten Skala** (z. B. nach Roloff)

**Untersuchungsbedingungen** (bestimmen die Reichweite jeder Aussage)
- Datum und Uhrzeit der Begehung
- Witterung, Belichtung, Belaubungszustand
- Zugänglichkeit und Einsehbarkeit des Baumes
- Eingesetzte Hilfsmittel (Fernglas, Sondierstab, Klanghammer, Leiter, Hubarbeitsbühne, Seilklettertechnik, Drohne)

**Baumumfeld**
- Nutzungsintensität des Umfelds und daraus abgeleitetes Schadenspotenzial
- Oberflächenbefestigung, Baumscheibe, durchwurzelbarer Raum
- Leitungen, bauliche Anlagen, Vorschädigungen des Standorts

**Zustandsbeschreibung (rein beschreibend, ohne Wertung)**
- Defektsymptome mit Lage, Ausdehnung, Maß
- Pilzfruchtkörper mit Artbestimmung bzw. Bestimmungsvorbehalt
- Totholz nach Stärke und Lage
- Rinden-, Stamm-, Kronen- und Wurzelbereichsbefunde

### D.2 Eingehende Untersuchung

Nur bei konkreten Anhaltspunkten. Zu dokumentieren sind:
- Anlass und Fragestellung der eingehenden Untersuchung
- Angewandtes Verfahren (z. B. Schalltomografie, Bohrwiderstandsmessung, Zugversuch, Wurzelsuchgrabung, Endoskopie)
- Gerätetyp, Messebene, Messhöhe, Anzahl und Lage der Messpunkte
- Rohdaten bzw. Messprotokolle im Anhang
- **Ausdrückliche Benennung der Verfahrensgrenzen**

### D.3 Schlussfolgerungen (Pflichtbestandteile)

- [ ] Beurteilung der Verkehrssicherheit zum Zeitpunkt der Untersuchung
- [ ] Empfohlene Maßnahmen mit **Fristen** und Dringlichkeitsstufe
- [ ] **Dokumentierte Prüfung milderer Mittel** vor jeder Fällempfehlung (Kroneneinkürzung, Kronensicherung, Totholzentnahme, Umfeld-/Nutzungsanpassung, Absperrung, Habitatbaumkonzept)
- [ ] Festlegung des nächsten Kontrollintervalls / Wiedervorlage
- [ ] Benennung des verbleibenden Restrisikos
- [ ] Gültigkeitshinweis: Momentaufnahme zum Untersuchungszeitpunkt; kein Ausschluss von Versagen bei außergewöhnlichen Ereignissen
- [ ] Verweis auf die zugrunde gelegten Regelwerke **mit Ausgabejahr**

---

## Teil E — Rechtlicher Sonderrahmen Baum

### E.1 Verkehrssicherungspflicht

- Grundlage: § 823 BGB. Baumeigentümer sind verpflichtet, die Verkehrssicherheit ihrer Bäume zu gewährleisten.
- Gefestigte Rechtsprechungslinie: Geschuldet ist keine absolute Sicherheit, sondern die **regelmäßige äußere Sichtprüfung durch fachkundiges Personal**; eine eingehende Untersuchung erst bei konkreten Anhaltspunkten für eine Gefahr.
- Die **Zumutbarkeits- und Verhältnismäßigkeitsabwägung** muss im Gutachten sichtbar hergeleitet werden.
- Konkrete Urteilsfundstellen sind vor Verwendung aus einer aktuellen Kommentierung zu verifizieren; der Agent zitiert keine Aktenzeichen aus dem Gedächtnis.

### E.2 Artenschutz (in jedem Baumgutachten zu prüfen)

- § 39 Abs. 5 BNatSchG: Fäll- und Schnittverbot vom **1. März bis 30. September** für Bäume außerhalb des Waldes, von Kurzumtriebsplantagen und gärtnerisch genutzten Grundflächen.
- § 39 Abs. 5 S. 2 BNatSchG: Maßnahmen zur Gewährleistung der Verkehrssicherheit sind von diesen Verboten ausgenommen — **die Habitatprüfung entfällt dadurch nicht**.
- § 44 Abs. 1 BNatSchG (besonderer Artenschutz) gilt **ganzjährig und unabhängig** von § 39: Verbot von Tötung, erheblicher Störung sowie Entnahme, Beschädigung oder Zerstörung von Fortpflanzungs- und Ruhestätten besonders geschützter Arten.
- Habitatstrukturen (Spechthöhlen, sonstige Höhlungen, Risse, Spalten, Horste) sind vor Eingriffen intensiv zu untersuchen — vom Boden mit Fernglas/Spektiv, per Kameradrohne oder durch Bekletterung; Untersuchungsmethode und Ergebnis sind zu dokumentieren.
- Ergebnis der artenschutzrechtlichen Prüfung ist als **eigener Unterabschnitt im Kapitel „Ergebnisse"** auszuweisen, nicht als Floskel.

### E.3 Weitere zu prüfende Ebenen

- Kommunale **Baumschutzsatzung**: Schutzschwelle (i. d. R. Stammumfang in definierter Messhöhe), Genehmigungspflicht, Ersatzpflanzung, Ausnahmetatbestände — **immer die konkrete Satzung der Standortkommune zitieren**
- Landesnaturschutzgesetz des jeweiligen Bundeslandes
- § 30 BNatSchG (gesetzlich geschützte Biotope), § 28 BNatSchG (Naturdenkmale), Alleenschutz nach Landesrecht
- Festsetzungen des Bebauungsplans, § 9 Abs. 1 Nr. 25 BauGB
- Nachbarrecht (Grenzabstände nach Landesnachbarrecht, § 910 BGB)
- Pflanzengesundheit: Melde- und Bekämpfungspflichten bei Quarantäneschadorganismen
- Arbeitsschutz, soweit für die empfohlenen Maßnahmen relevant

---

## Teil F — Regelwerksregister (Stand August 2026)

**Vor Verwendung ist der aktuelle Ausgabestand zu verifizieren.** Veraltete Ausgabestände sind zu vermeiden. Die Citekeys entsprechen dem Zotero-Standardkorpus (`gutachten_bausteine/bib/standard.bib`); Register und Bibliografie müssen im Ausgabejahr übereinstimmen (`just lint` im Bausteine-Repo prüft das).

| Regelwerk | Citekey | Aktueller Stand | Anwendung |
|---|---|---|---|
| **FLL-Baumkontrollrichtlinien** | `fll2020` | 3. Ausgabe **2020** | Stand der Technik für Baumkontrollen zur Überprüfung der Verkehrssicherheit; Definitionen von Regel- und Zusatzkontrolle, Entwicklungsphasen, Kontrollintervalle, Dokumentation |
| **FLL-Baumuntersuchungsrichtlinien** | `fll2013` | **2013** | Eingehende Untersuchung |
| **ZTV-Baumpflege** | `fll2017` | 6. Ausgabe **2017** (ersetzt 2006) | Baumpflegemaßnahmen; gilt als anerkannte Regel der Technik i. S. d. VOB; Grundlage für Maßnahmenbeschreibung und Leistungsverzeichnis |
| **DIN 18920** | `din18920` | **2026-06** | Schutz von Bäumen, Pflanzenbeständen und Vegetationsflächen bei Baumaßnahmen |
| **R SBB** (FGSV) | `rsbb2023` | **2023** | Schutz von Bäumen und Vegetationsbeständen bei Baumaßnahmen; R-1-Regelwerk mit hoher Verbindlichkeit, insbesondere als Vertragsbestandteil; eingeführt mit ARS Nr. 28/2023 des BMDV |
| **Methode Koch** i. V. m. FLL-Wertermittlungsrichtlinie | `fll2002` | **2002** (Richtwerte SVK/GALK: Ausgabe 2026/2027) | Gehölzwertermittlung / Schadensersatz; Sachwertverfahren, höchstrichterlich anerkannt |
| **GALK-Musterdienstanweisung** für Regelkontrollen von Bäumen | `galk2021` | **2021** | Umsetzung der FLL-Baumkontrollrichtlinien 2020 in kommunalen Verwaltungen |
| Ergänzend | — | DWA-M 162 (Bäume und Leitungen); DIN 18915–18919; FLL-Empfehlungen für Baumpflanzungen Teil 1 (2015) und Teil 2 (2010); H ArtB (2017) | je nach Fragestellung |

### F.1 Nicht mehr zu zitieren

| Veraltet | Ersetzt durch |
|---|---|
| RAS-LP 4 (1999) | **R SBB 2023** |
| DIN 18920:2014-07 | **DIN 18920:2026-06** |
| DIN 18920:2002-08 | **DIN 18920:2026-06** |
| FLL-Baumkontrollrichtlinie 2004 / 2010 | **FLL-Baumkontrollrichtlinien 2020** |
| ZTV-Baumpflege 2006 (und früher) | **ZTV-Baumpflege 2017** |

---

## Teil G — Qualifikationsnachweis im Gutachten

Die Sachkunde ist im Gutachten konkret zu belegen, nicht pauschal zu behaupten. In Betracht kommen je nach Auftrag:

- FLL-Zertifizierter Baumkontrolleur
- European Tree Worker (ETW) / European Tree Technician (ETT)
- Geprüfter Fachagrarwirt Baumpflege / Bachelor Professional Baumpflege
- Sachkundiger für Baum-Habitatstrukturen (bei artenschutzrechtlichen Fragestellungen)
- Öffentlich bestellter und vereidigter Sachverständiger für das einschlägige Sachgebiet
- Zertifizierung nach DIN EN ISO/IEC 17024

Umsetzung im Template: `my-qualification` in `publication/config.typ` setzen; bei `none` wird kein Qualifikationsblock gerendert (projektweise Entscheidung).

---

## Teil H — Prüfliste vor Freigabe

- [ ] Alle gestellten Fragen beantwortet, keine darüber hinaus (Teil B)
- [ ] Anknüpfungs-, Befund- und Zusatztatsachen erkennbar getrennt (Teil B)
- [ ] Beschreibung (Ergebnisse) und Bewertung (Schlussfolgerungen) nicht vermischt (Teil B, C.3)
- [ ] Alle Pflichtangaben aus C.1 und C.2 vorhanden
- [ ] Jede Schlussfolgerung nachvollziehbar hergeleitet, Wahrscheinlichkeitsgrade benannt (Teil B)
- [ ] Alle zitierten Regelwerke mit korrektem Ausgabejahr, keine Einträge aus F.1
- [ ] Artenschutzrechtliche Prüfung als eigener Unterabschnitt in „Ergebnisse" dokumentiert (E.2)
- [ ] Kommunale Baumschutzsatzung der Standortkommune geprüft und zitiert (E.3)
- [ ] Mildere Mittel vor jeder Fällempfehlung dokumentiert geprüft (D.3)
- [ ] Untersuchungsgrenzen, Restrisiko und Gültigkeitshinweis enthalten (D.3)
- [ ] Fotos vollständig beschriftet und im Text referenziert (C.2)
- [ ] Zahlenwerte durchgängig mit Einheit und Bezugsgröße (Teil B)
- [ ] Keine rechtlichen Würdigungen (Gerichtsgutachten) bzw. gekennzeichnet (Privatgutachten) (Teil B)
- [ ] Zusammenfassung für Nichtfachleute verständlich (C.1)
- [ ] Unterschrift, ggf. Stempel, Seitenzählung „Seite x von y" (C.1, C.2)
- [ ] Alle `[ERGÄNZEN: …]`-Platzhalter aufgelöst (Regel 0.1)

---

*Dieses Dokument ersetzt keine Rechtsberatung. Normstände, Satzungen und Rechtsprechung sind vor Verwendung im Einzelfall zu verifizieren.*
