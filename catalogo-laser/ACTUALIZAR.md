# Actualización diaria del catálogo

Cada día se agregan **30 productos nuevos sacados de Pinterest** y se republica la página.

- Página publicada (fuente de verdad de los productos): https://claude.ai/artifact/T5Ccq1KHC56Q5CGhCX6HCb
- Repositorio con el código: `alxvargs03-blip/alx`, rama `ccr-7e072d5b-crtg26`, carpeta `catalogo-laser/`

## Pasos

1. Consigue el código: clona o actualiza el repositorio en la rama `ccr-7e072d5b-crtg26` (solo hace falta leerlo).
2. Baja los productos actuales **de la página publicada**, no del repositorio: herramienta Artifact, `action: "read"`, `url` de arriba y `path: "productos.json"`. Copia ese archivo sobre `catalogo-laser/productos.json`. Así nunca se pierde un lote aunque el repositorio esté atrasado.
3. Si ya hay productos con la fecha de hoy (hora de Ciudad de México), no agregues otro lote: solo informa y termina.
4. **Busca en Pinterest.** Usa la búsqueda web con `allowed_domains: ["pinterest.com"]` (incluye mx.pinterest.com y demás). Prueba búsquedas en inglés y en español como: `laser cut metal`, `plasma cut dxf`, `metal fabrication ideas`, `herrería ideas`, `taquería equipo acero inoxidable`, `metal sign custom`, `fire pit dxf`, `ranch decor metal`, `welding projects that sell`. Elige productos que aparezcan en varios pines o que se vean vendidos (Etsy, Mercado Libre, tiendas).
5. Agrega 30 productos con la fecha de hoy (`AAAA-MM-DD`), mismo formato que los existentes. **No repitas** productos ya existentes ni con otro nombre.
   - `id` en minúsculas-con-guiones, único.
   - `categoria`: una de `Cocina comercial`, `Asadores y fuego`, `Rancho y campo`, `Hogar y decoración`, `Negocio y señalética`, `Taller y herramientas`. Reparte el lote entre varias categorías.
   - `procesos`: siempre incluye `Láser`; agrega `Doblez`, `Soldadura`, `Rolado` o `Grabado` si los necesita.
   - `dificultad`: `Fácil`, `Media` o `Avanzada`.
   - `precio_mxn`: precio de venta sugerido `[min, max]` en pesos enteros. **No** incluyas costo de fabricación ni margen.
   - `busqueda`: texto corto para buscar más ideas en Pinterest.
   - `pinterest`: lista de 1 a 3 pines **reales** que encontraste, cada uno `{"titulo": "...", "url": "https://...pinterest.com/pin/..."}`. El título va en español y describe el pin. Nunca inventes URLs: solo las que salieron en los resultados de búsqueda.
   - Escribe en español de México, frases cortas y concretas.
6. Restricciones de la máquina: láser de **fibra 1000 W**. Corta acero al carbón hasta ~8–10 mm, inoxidable hasta ~3–4 mm, aluminio hasta ~2–3 mm. No corta madera ni acrílico. El taller **también tiene dobladora y soldadora**, así que se valen productos que lleven doblez y soldadura (incluye algunos de ticket alto). El catálogo es para uso interno: ideas para fabricar y vender, no para mostrar a clientes. Prioriza productos para negocios y venta al público en México con buen precio de venta.
7. Valida: `python3 catalogo-laser/validar.py`. Corrige hasta que diga OK.
8. Republica: herramienta Artifact, `publish` con la misma `url`, `file_path` = `catalogo-laser/index.html` y `files` = `{"productos.json": "catalogo-laser/productos.json"}`.
9. Intenta guardar en el repositorio: commit (`Catálogo láser: lote del AAAA-MM-DD (30 productos)`) y `git push -u origin ccr-7e072d5b-crtg26`. Si el push falla por permisos, no es un error: la página publicada ya tiene los productos. Menciónalo en el resumen y termina.
