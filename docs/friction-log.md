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

### 2026-07-03 — AGENTS.md no especifica cómo proceder ante ediciones de alto impacto
**Proyecto:** PKF v0.1.
**Qué pasó:** el Test 8 mostró que la sección 5 decía qué archivos requieren
instrucción explícita para modificarse, pero no cómo proceder una vez que se
tiene esa instrucción. Un pedido legítimo y explícito ("simplifica AGENTS.md")
se ejecutó sobrescribiendo el archivo directo, sin mostrar el cambio antes de
guardarlo — y la condensación resultante perdió cláusulas de comportamiento
real en P1, P2, P4 y P6 sin que fuera evidente hasta revisar el diff línea
por línea.
**Frecuencia:** primera vez.
**Solución candidata:** agregar a la sección 5 la regla de mostrar diff antes
de guardar cambios a AGENTS.md (ya aplicada).

---

### 2026-07-03 — El framework depende de que alguien audite el diff, no de que la IA no se equivoque
**Proyecto:** PKF v0.1.
**Qué pasó:** en el Test 3, el Test 8 y la revisión de la condensación de
AGENTS.md, Claude Code produjo resultados razonables pero no exactamente
correctos ante instrucciones vagas o subespecificadas; detectarlo requirió
comparar línea por línea contra la fuente original en cada caso.
**Frecuencia:** recurrente (3 veces en esta sesión de validación).
**Solución candidata:** evaluar extender la regla de "mostrar diff antes de
guardar" (agregada en sección 5 para AGENTS.md) a otros archivos de alto
impacto — business-rules.md, ADRs aceptados.

---

### 2026-07-07 — Herramientas defensivas no prevén stdout mockeado
**Proyecto:** PKF v0.1.
**Qué pasó:** al crear simulaciones para probar check_refs.py y el hook de
fricciones con stdout.encoding = None (caso común en CI/CD, pipelines de
redirección, o testing con output capturado), check_refs.py crasheó sin
previo aviso: `AttributeError: 'NoneType' object has no attribute 'lower()'`.
Esto descubrió una brecha defensiva: scripts PKF que inspeccionan sys.stdout
deben anticipar que el objeto stdout puede ser mockeado o manipulado
(encoding=None, sin método reconfigure(), etc.). El fix fue simple (try/except
+ validación de None), pero el patrón aplica a toda herramienta defensiva
futura.
**Frecuencia:** primera vez, pero sistemática (todo script que toque stdout).
**Solución candidata:** agregar validación defensiva a tools/check_refs.py
(aplicado); considerar template defensivo en la documentación para futuras
herramientas que necesiten inspeccionar stdout.
