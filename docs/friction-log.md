# Bitácora de fricciones

> Aquí se anota toda fricción real encontrada al trabajar con el framework:
> algo que la IA no encontró, un rastro que se perdió, una convención que estorbó.
> **Regla de oro de PKF:** ninguna pieza nueva entra al framework si no nace
> de una entrada en esta bitácora. El framework crece por extracción, no por diseño.

## Formato

```markdown
### 2026-07-15 — Título corto de la fricción
**Proyecto:** en cuál ocurrió.
**Qué pasó:** descripción concreta del dolor.
**Frecuencia:** primera vez | recurrente (n veces).
**Solución candidata:** (opcional, solo si es evidente).
```

Una fricción que ocurre una sola vez probablemente no justifica cambios.
Una que se repite en dos proyectos distintos, casi seguro que sí.

---

### 2026-07-03 — Power BI no puede leer docs/business-rules.md
**Proyecto:** PKF v0.1.
**Qué pasó:** se necesita mostrar las reglas de negocio (RN-xxx) en un dashboard de
Power BI, pero `Web.Contents` no parsea Markdown. Se resolvió con un export
generado a JSON (`tools/export_business_rules.py` → `docs/business-rules.json`),
ver ADR-002.
**Frecuencia:** primera vez.
**Solución candidata:** export JSON derivado, generado por script, markdown sigue
siendo la fuente de verdad.
