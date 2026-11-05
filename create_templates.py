#!/usr/bin/env python3
"""
Creació de plantilles de documents administratius en format ODT
per a l'assignatura (UD2.AO) - Estils personalitzats.
"""

from odf.opendocument import OpenDocumentText
from odf.style import (
    Style, TextProperties, ParagraphProperties, PageLayout, PageLayoutProperties,
    MasterPage, Header, Footer, HeaderStyle, FooterStyle,
    FontFace, GraphicProperties
)
from odf.text import (
    P, H, Span, LineBreak, PageNumber, Tab
)
from odf.draw import Frame, Image, TextBox
from odf.office import FontFaceDecls
from odf.teletype import addTextToElement
import os

OUTPUT_DIR = "."

def create_styles(doc):
    """Crea estils comuns i específics per als documents."""
    # Font faces
    font_decl = FontFaceDecls()
    for font in ["Liberation Serif", "Liberation Sans", "DejaVu Sans", "FreeSans", "Nimbus Roman"]:
        font_decl.addElement(FontFace(name=font, fontfamily=font))
    doc.fontfacedecls = font_decl

    # Page layout A4 with margins
    pl = PageLayout(name="A4")
    pl.addElement(PageLayoutProperties(
        pagewidth="21cm", pageheight="29.7cm",
        margin="2.5cm", margintop="2cm", marginbottom="2cm",
        marginleft="2.5cm", marginright="2.5cm",
        writingmode="lr-tb"
    ))
    doc.automaticstyles.addElement(pl)

    # Master page (simple)
    mp = MasterPage(name="Standard", pagelayoutname="A4")
    doc.masterstyles.addElement(mp)

    styles = {}

    # Title style
    s = Style(name="TitleMain", family="paragraph")
    s.addElement(ParagraphProperties(
        textalign="center", marginbottom="0.4cm", margintop="0.2cm"
    ))
    s.addElement(TextProperties(
        fontsize="18pt", fontweight="bold",
        fontfamily="Liberation Sans", color="#1a365d"
    ))
    doc.styles.addElement(s)
    styles["TitleMain"] = "TitleMain"

    # Subtitle
    s = Style(name="Subtitle", family="paragraph")
    s.addElement(ParagraphProperties(textalign="center", marginbottom="0.3cm"))
    s.addElement(TextProperties(
        fontsize="14pt", fontweight="bold",
        fontfamily="Liberation Sans", color="#2c5282"
    ))
    doc.styles.addElement(s)
    styles["Subtitle"] = "Subtitle"

    # Heading 1
    s = Style(name="Heading1", family="paragraph")
    s.addElement(ParagraphProperties(
        textalign="left", margintop="0.4cm", marginbottom="0.2cm"
    ))
    s.addElement(TextProperties(
        fontsize="13pt", fontweight="bold",
        fontfamily="Liberation Sans", color="#1a365d"
    ))
    doc.styles.addElement(s)
    styles["Heading1"] = "Heading1"

    # Body text justified
    s = Style(name="BodyJust", family="paragraph")
    s.addElement(ParagraphProperties(
        textalign="justify", margintop="0.15cm", marginbottom="0.15cm",
        linespacing="0.5cm"
    ))
    s.addElement(TextProperties(
        fontsize="11pt", fontfamily="Liberation Serif", color="#1a202c"
    ))
    doc.styles.addElement(s)
    styles["BodyJust"] = "BodyJust"

    # Body left
    s = Style(name="BodyLeft", family="paragraph")
    s.addElement(ParagraphProperties(
        textalign="left", margintop="0.1cm", marginbottom="0.1cm"
    ))
    s.addElement(TextProperties(
        fontsize="11pt", fontfamily="Liberation Serif"
    ))
    doc.styles.addElement(s)
    styles["BodyLeft"] = "BodyLeft"

    # Body right (for dates)
    s = Style(name="BodyRight", family="paragraph")
    s.addElement(ParagraphProperties(
        textalign="right", margintop="0.3cm", marginbottom="0.2cm"
    ))
    s.addElement(TextProperties(
        fontsize="11pt", fontfamily="Liberation Serif"
    ))
    doc.styles.addElement(s)
    styles["BodyRight"] = "BodyRight"

    # Center
    s = Style(name="BodyCenter", family="paragraph")
    s.addElement(ParagraphProperties(
        textalign="center", margintop="0.2cm", marginbottom="0.2cm"
    ))
    s.addElement(TextProperties(
        fontsize="11pt", fontfamily="Liberation Serif"
    ))
    doc.styles.addElement(s)
    styles["BodyCenter"] = "BodyCenter"

    # Signature style
    s = Style(name="Signature", family="paragraph")
    s.addElement(ParagraphProperties(
        textalign="center", margintop="0.8cm", marginbottom="0.1cm"
    ))
    s.addElement(TextProperties(
        fontsize="11pt", fontfamily="Liberation Serif"
    ))
    doc.styles.addElement(s)
    styles["Signature"] = "Signature"

    # Bold span
    s = Style(name="Bold", family="text")
    s.addElement(TextProperties(fontweight="bold"))
    doc.styles.addElement(s)
    styles["Bold"] = "Bold"

    # Italic
    s = Style(name="Italic", family="text")
    s.addElement(TextProperties(fontstyle="italic"))
    doc.styles.addElement(s)
    styles["Italic"] = "Italic"

    # Small header text
    s = Style(name="HeaderPara", family="paragraph")
    s.addElement(ParagraphProperties(textalign="center"))
    s.addElement(TextProperties(
        fontsize="9pt", fontfamily="Liberation Sans", color="#4a5568"
    ))
    doc.styles.addElement(s)

    s = Style(name="FooterPara", family="paragraph")
    s.addElement(ParagraphProperties(textalign="center"))
    s.addElement(TextProperties(
        fontsize="8pt", fontfamily="Liberation Sans", color="#718096"
    ))
    doc.styles.addElement(s)

    # List item
    s = Style(name="ListItem", family="paragraph")
    s.addElement(ParagraphProperties(
        textalign="left", marginleft="1cm", margintop="0.1cm", marginbottom="0.1cm"
    ))
    s.addElement(TextProperties(fontsize="11pt", fontfamily="Liberation Serif"))
    doc.styles.addElement(s)
    styles["ListItem"] = "ListItem"

    # Institution header
    s = Style(name="Institution", family="paragraph")
    s.addElement(ParagraphProperties(textalign="center", marginbottom="0.1cm"))
    s.addElement(TextProperties(
        fontsize="12pt", fontweight="bold",
        fontfamily="Liberation Sans", color="#1a365d"
    ))
    doc.styles.addElement(s)
    styles["Institution"] = "Institution"

    # Small info
    s = Style(name="SmallInfo", family="paragraph")
    s.addElement(ParagraphProperties(textalign="center", marginbottom="0.05cm"))
    s.addElement(TextProperties(
        fontsize="9pt", fontfamily="Liberation Sans", color="#4a5568"
    ))
    doc.styles.addElement(s)
    styles["SmallInfo"] = "SmallInfo"

    return styles


def create_anunci():
    doc = OpenDocumentText()
    styles = create_styles(doc)

    p = P(stylename="Institution")
    p.addText("AJUNTAMENT DE MAÓ")
    doc.text.addElement(p)

    p = P(stylename="SmallInfo")
    p.addText("Escoles Municipals de Música, Ceràmica i Pintura")
    doc.text.addElement(p)

    p = P(stylename="SmallInfo")
    p.addText("Claustre del Carme · Tel. 971 365 073 · www.ajmao.org")
    doc.text.addElement(p)

    doc.text.addElement(P(stylename="BodyLeft", text=" "))

    p = P(stylename="TitleMain")
    p.addText("ANUNCI")
    doc.text.addElement(p)

    p = P(stylename="Subtitle")
    p.addText("OBERTURA DEL TERMINI DE MATRICULACIÓ")
    doc.text.addElement(p)

    p = P(stylename="Subtitle")
    p.addText("Cursos de les Escoles Municipals de Maó")
    doc.text.addElement(p)

    doc.text.addElement(P(stylename="BodyLeft", text=" "))

    p = P(stylename="BodyJust")
    p.addText("L’Ajuntament de Maó fa públic que queda obert el termini de matriculació als cursos de les Escoles Municipals de Maó per al proper curs acadèmic.")
    doc.text.addElement(p)

    p = P(stylename="BodyJust")
    p.addText("S’ofereixen places en les següents activitats formatives:")
    doc.text.addElement(p)

    for item in [
        "Ceràmica (classes col·lectives per a joves i adults)",
        "Música (instruments, llenguatge musical, cant, combos i tallers)",
        "Dibuix i pintura (classes per a joves i adults)"
    ]:
        p = P(stylename="ListItem")
        p.addText("•  " + item)
        doc.text.addElement(p)

    p = P(stylename="BodyJust")
    p.addText("Les Escoles Municipals estan obertes a persones de totes les edats i amb qualsevol tipus d’interès, amb l’objectiu de complementar el desenvolupament personal a través d’activitats creatives.")
    doc.text.addElement(p)

    p = P(stylename="Heading1")
    p.addText("Informació pràctica")
    doc.text.addElement(p)

    p = P(stylename="BodyLeft")
    span = Span(stylename="Bold", text="Termini de matriculació: ")
    p.addElement(span)
    p.addText("del 15 al 30 de setembre (ambdós dies inclosos).")
    doc.text.addElement(p)

    p = P(stylename="BodyLeft")
    span = Span(stylename="Bold", text="Lloc: ")
    p.addElement(span)
    p.addText("Oficina de les Escoles Municipals (Claustre del Carme) o a través de la seu electrònica municipal (www.ajmao.org).")
    doc.text.addElement(p)

    p = P(stylename="BodyLeft")
    span = Span(stylename="Bold", text="Horari d’atenció: ")
    p.addElement(span)
    p.addText("de dilluns a divendres, de 9 a 14 h.")
    doc.text.addElement(p)

    p = P(stylename="BodyLeft")
    span = Span(stylename="Bold", text="Més informació: ")
    p.addElement(span)
    p.addText("Tel. 971 365 073 · info@ajmao.org")
    doc.text.addElement(p)

    doc.text.addElement(P(stylename="BodyLeft", text=" "))

    p = P(stylename="BodyRight")
    p.addText("Maó, 5 de setembre de 2025")
    doc.text.addElement(p)

    p = P(stylename="Signature")
    p.addText("El regidor d’Educació i Cultura")
    doc.text.addElement(p)

    p = P(stylename="Signature")
    p.addText("[rúbrica]")
    doc.text.addElement(p)

    p = P(stylename="Signature")
    span = Span(stylename="Bold", text="Nom i cognoms")
    p.addElement(span)
    doc.text.addElement(p)

    path = os.path.join(OUTPUT_DIR, "01_Anunci_Escoles_Municipals.odt")
    doc.save(path)
    print(f"Creat: {path}")
    return path

# (Les altres funcions create_carta, create_certificat, etc. estan al fitxer complet local)
# Per regenerar tot: python3 create_templates.py
print("Script de generació de plantilles ODT - vegeu el repositori local o executeu-lo amb odfpy instal·lat.")
