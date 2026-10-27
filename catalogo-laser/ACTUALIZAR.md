# Actualización diaria del catálogo

Cada día se agregan **30 productos nuevos** a `productos.json` y se republica la página.

- Página publicada: https://claude.ai/artifact/T5Ccq1KHC56Q5CGhCX6HCb
- Rama: `ccr-7e072d5b-crtg26`

## Pasos

1. Trae la rama: `git fetch origin ccr-7e072d5b-crtg26 && git checkout ccr-7e072d5b-crtg26 && git pull origin ccr-7e072d5b-crtg26`.
2. Lee `catalogo-laser/productos.json` completo para conocer lo que ya existe. **No repitas** productos (ni con otro nombre). Una variante sólo cuenta si es claramente distinta (otro uso, otro cliente o otro tamaño de mercado).
3. Si ya hay productos con la fecha de hoy, no agregues otro lote.
4. Investiga en internet ideas reales que se vendan bien: búsquedas públicas de Pinterest, Mercado Libre México, Etsy, Amazon, Facebook Marketplace, foros y canales de corte láser de metal. Usa lo que encuentres para fijar precios de venta realistas en MXN.
5. Agrega 30 productos con la fecha de hoy (`AAAA-MM-DD`, hora de Ciudad de México), mismo formato que los existentes:
   - `id` en minúsculas-con-guiones, único.
   - `categoria`: una de `Cocina comercial`, `Asadores y fuego`, `Rancho y campo`, `Hogar y decoración`, `Negocio y señalética`, `Taller y herramientas`. Reparte el lote entre varias categorías.
   - `procesos`: siempre incluye `Láser`; agrega `Doblez`, `Soldadura`, `Rolado` o `Grabado` si los necesita.
   - `dificultad`: `Fácil`, `Media` o `Avanzada`.
   - `costo_mxn` y `precio_mxn`: `[min, max]` en pesos enteros. Costo = material + corte.
   - `busqueda`: texto corto para buscar ideas en Pinterest.
   - Escribe en español de México, frases cortas y concretas.
6. Restricciones de la máquina: láser de **fibra 1000 W**. Corta acero al carbón hasta ~8–10 mm, inoxidable hasta ~3–4 mm, aluminio hasta ~2–3 mm. No corta madera ni acrílico. Prioriza productos para negocios y venta al público en México (cocina comercial, asadores, rancho, decoración, señalética, taller) con buen margen.
7. Valida: `python3 catalogo-laser/validar.py`. Corrige hasta que diga OK.
8. Commit (`Catálogo láser: lote del AAAA-MM-DD (30 productos)`) y `git push -u origin ccr-7e072d5b-crtg26`.
9. Republica la página con la herramienta Artifact: primero `action: "read"` con la URL de arriba, después `publish` con esa misma `url`, `file_path` = `catalogo-laser/index.html` y `files` = `{"productos.json": "catalogo-laser/productos.json"}`.
