# UD2.AO - Documents administratius i comercials

Aquest repositori conté els 6 documents administratius en format ODT creats seguint els models del llibre *Documents administratius i comercials* (Consell Insular de Menorca, 2007) i les instruccions de l'enunciat.

## Fitxers

| Fitxer | Descripció |
|--------|------------|
| 01_Anunci.odt | Anunci de l'Ajuntament de Maó sobre matriculació a l'Escola Municipal (ceràmica, música, dibuix) |
| 02_Carta.odt | Carta de l'IES Joan Ramis i Ramis sol·licitant 2 multifuncions a Xerox de Menorca |
| 03_Certificat.odt | Certificat del secretari del centre que acredita que es cursen els estudis de 1r SMX |
| 04_Circular.odt | Circular del Servei de Recaptació de l'Ajuntament de Maó sobre el termini de pagament de l'IBI |
| 05_Citacio.odt | Citació d'Hisenda per a la signatura del Model 061 |
| 06_Contracte.odt | Contracte de compravenda d'un habitatge |

## Com recuperar els fitxers .odt

Els fitxers `.odt.b64` contenen la codificació base64 dels documents ODT originals (per facilitar la pujada via API de text).

Per reconstruir un fitxer:

```bash
base64 -d 01_Anunci.odt.b64 > 01_Anunci.odt
```

O amb Python:

```python
import base64
with open("01_Anunci.odt.b64") as f:
    data = base64.b64decode(f.read())
with open("01_Anunci.odt", "wb") as f:
    f.write(data)
```

## Estils aplicats

- Tipus de lletra: Liberation Sans (títols) i Liberation Serif (cos)
- Colors: vermell fosc per a títols institucionals
- Alineació: justificada al cos, centrada en títols i signatures
- Marges: 2,2 cm superior, 2 cm inferior, 2,5 cm laterals
- Capçalera i peu de pàgina amb identificació del document i número de pàgina
- Redacció en català administratiu (ús de *vós*, present, frases clares)

Data de creació: 5 de novembre de 2026
