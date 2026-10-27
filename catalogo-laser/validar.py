"""Revisa productos.json antes de publicar: campos, tipos y duplicados.

Uso: python3 catalogo-laser/validar.py
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

RUTA = Path(__file__).with_name("productos.json")
CATEGORIAS = {
    "Cocina comercial",
    "Asadores y fuego",
    "Rancho y campo",
    "Hogar y decoración",
    "Negocio y señalética",
    "Taller y herramientas",
}
PROCESOS = {"Láser", "Doblez", "Soldadura", "Rolado", "Grabado"}
DIFICULTADES = {"Fácil", "Media", "Avanzada"}
TEXTOS = ["id", "nombre", "categoria", "descripcion", "cliente", "material", "dificultad", "tip", "busqueda", "fecha"]


def normaliza(nombre):
    return re.sub(r"[^a-z0-9áéíóúñ]+", " ", nombre.lower()).strip()


def main():
    productos = json.loads(RUTA.read_text(encoding="utf-8"))
    errores = []
    for i, p in enumerate(productos):
        donde = f"#{i} ({p.get('id', '?')})"
        for campo in TEXTOS:
            if not isinstance(p.get(campo), str) or not p[campo].strip():
                errores.append(f"{donde}: falta '{campo}'")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", p.get("id", "")):
            errores.append(f"{donde}: id debe ser minúsculas-con-guiones")
        if p.get("categoria") not in CATEGORIAS:
            errores.append(f"{donde}: categoría desconocida '{p.get('categoria')}'")
        if p.get("dificultad") not in DIFICULTADES:
            errores.append(f"{donde}: dificultad desconocida '{p.get('dificultad')}'")
        procesos = p.get("procesos")
        if not procesos or "Láser" not in procesos or not set(procesos) <= PROCESOS:
            errores.append(f"{donde}: procesos inválidos {procesos}")
        for campo in ("costo_mxn", "precio_mxn"):
            r = p.get(campo)
            if not (isinstance(r, list) and len(r) == 2 and all(isinstance(n, int) and n > 0 for n in r) and r[0] <= r[1]):
                errores.append(f"{donde}: '{campo}' debe ser [min, max] en pesos")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.get("fecha", "")):
            errores.append(f"{donde}: fecha debe ser AAAA-MM-DD")

    for campo, clave in (("id", lambda p: p.get("id")), ("nombre", lambda p: normaliza(p.get("nombre", "")))):
        for valor, n in Counter(map(clave, productos)).items():
            if n > 1:
                errores.append(f"{campo} repetido {n} veces: {valor}")

    if errores:
        print("\n".join(errores))
        sys.exit(1)
    por_fecha = Counter(p["fecha"] for p in productos)
    print(f"OK: {len(productos)} productos. Por fecha: {dict(sorted(por_fecha.items()))}")


if __name__ == "__main__":
    main()
