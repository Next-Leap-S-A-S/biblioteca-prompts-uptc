# Biblioteca de prompts jurídicos para la UPTC

Biblioteca de prompts con el marco Rol, Contexto e Instrucción, organizada por
áreas y subáreas del derecho colombiano. Material de Next Leap para una clase
en la Universidad Pedagógica y Tecnológica de Colombia (UPTC).

La página es un único `index.html` autocontenido. Filtra por área, luego por
subárea, busca por palabra clave, edita los campos entre corchetes y copia el
prompt. Incluye un laboratorio con medidor y un ejercicio por rondas.

## Cómo se construye

```
src/
  template.html        marcado, estilos y lógica
  prompts-<clave>.js   un archivo por área
  rondas.js            ejercicio por rondas
  assets/              tipografías, logo de Next Leap y logo de la UPTC
  build.py             ensambla index.html (ASCII puro)
```

```
python3 src/build.py            # avisa y omite áreas sin archivo
python3 src/build.py --estricto # exige todos los archivos y subáreas
```

Cada prompt es `{a:"clave", s:"Subárea", t:"título", r:"rol", c:"contexto", i:"instrucción"}`.
Claves de área, en orden: civil, comercial, laboral, penal, administrativo,
constitucional, tributario, ambiental, digital, internacional, practica.

## Branding UPTC

El manual de identidad visual no apareció como documento público. Los datos
salen del portal oficial https://www.uptc.edu.co, consultado el 2026-10-30:

| Uso | Color | Fuente |
|-----|-------|--------|
| Rojo institucional del tema del portal | `#b31b34` (oscuro `#8b1528`) | `theme-red.min.css` |
| Amarillo UPTC | `#ffcc29` (variable `--amarillo-uptc`) | `headerUptc-v3.css` |
| Barra de menú | negro con 90 % de opacidad | `headerUptc-v3.css` |

Tipografías del portal: Montserrat y Open Sans. Esta página conserva Inter e
IBM Plex Mono por el sistema visual de Next Leap.

El logotipo `src/assets/uptc-logo.svg` (y su versión PNG) es la descarga del
archivo que usa el portal: `/sitio/portal/PRUEBAS/pruebasM/Frontal/.content/img/botones/logoUPTC24.svg`.
Es propiedad de la UPTC y se usa aquí con fines académicos. Si la universidad
entrega su manual, conviene cotejar colores y proporciones.
