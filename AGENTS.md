# AGENTS.md

> Instrucciones para cualquier IA (Claude, ChatGPT, Gemini, Copilot u otra) que colabore
> en este proyecto. Este archivo sigue el estándar AGENTS.md (https://agents.md).
> Léelo completo antes de hacer cualquier cambio.

---

## 1. Qué es este proyecto

<!-- PLANTILLA: reemplazar al inicializar un proyecto nuevo -->

**Nombre:** {NOMBRE_DEL_PROYECTO}
**Propósito:** {Una o dos frases. Qué problema resuelve y para quién.}
**Estado:** {exploración | desarrollo activo | producción | mantenimiento}
**Stack principal:** {ej: Python 3.12, Power Automate, Power BI, React, etc.}

## 2. Mapa del repositorio

| Ruta | Qué contiene | ¿La IA puede modificarla? |
|---|---|---|
| `README.md` | Presentación para humanos nuevos | Sí, si cambia el alcance |
| `AGENTS.md` | Este archivo | Solo con instrucción explícita del dueño |
| `docs/` | Documentación viva del proyecto | Sí, siguiendo `docs/CONVENTIONS.md` |
| `docs/business-rules.md` | Registro de reglas de negocio (RN-xxx) | Solo con instrucción explícita |
| `docs/adr/` | Decisiones de arquitectura (ADR-xxx) | Sí, agregando; nunca editando ADRs aceptados |
| `src/` (o equivalente) | Código fuente | Sí |
| `tools/` | Scripts de validación del propio framework | Sí |

## 3. Principios de colaboración

Estos principios están ordenados por prioridad. Ante conflicto, gana el de número menor.

**P1 — Regla de divergencia.** Si detectas una inconsistencia entre la documentación y
el código (o entre dos documentos), **detente**: no implementes sobre la inconsistencia.
Repórtala, propón cuál de las dos versiones parece correcta y espera confirmación.
Ninguno de los dos "prevalece" por defecto; la divergencia se reconcilia, no se ignora.

**P2 — Reglas de negocio protegidas.** Las reglas registradas en
`docs/business-rules.md` (RN-xxx) solo se crean o modifican con instrucción explícita
del dueño del proyecto. Si una tarea implica cambiar una RN, decláralo antes de tocar código.

**P3 — Decisiones quedan escritas.** Toda decisión técnica con consecuencias no triviales
(elección de librería, cambio de estructura de datos, integración externa, trade-off de
diseño) se registra como ADR en `docs/adr/` usando la plantilla. Si tomaste una decisión
así durante una tarea, el ADR es parte del entregable, no un opcional.

**P4 — Documentación y código viajan juntos.** Todo cambio de código que altere
comportamiento, estructura o interfaz incluye la actualización de los documentos
afectados **en el mismo cambio**. Un cambio que deja la documentación obsoleta
está incompleto.

**P5 — No se borra historia.** La información superada se marca como obsoleta
(con fecha y referencia a lo que la reemplaza), no se elimina. Los ADR nunca se
editan una vez aceptados: se escribe un ADR nuevo que los reemplaza.

**P6 — Referencias estables.** Al citar una regla de negocio o una decisión, usa su ID
(`RN-xxx`, `ADR-xxx` con su número real), no una paráfrasis. Antes de cerrar una tarea que agregó o
referenció IDs, ejecuta `python tools/check_refs.py` y corrige lo que reporte.

## 4. Rutas según tamaño del cambio

No todo cambio requiere el mismo proceso. Clasifica antes de empezar:

| Tipo | Ejemplos | Proceso |
|---|---|---|
| **Trivial** | Typo, formato, comentario, rename local | Hazlo directo. Sin ceremonia. |
| **Normal** | Nueva función, fix de bug, ajuste de lógica | Código + docs afectados juntos (P4). |
| **Estructural** | Nueva entidad, cambio de RN, nueva integración, decisión de arquitectura | Primero ADR o actualización de RN, luego implementación. |

Si dudas entre dos categorías, pregunta o asume la más exigente.

## 5. Qué nunca debe hacer una IA en este proyecto

- Inventar el contenido de un archivo que no pudo leer.
- Modificar `AGENTS.md`, `docs/business-rules.md` o ADRs aceptados sin instrucción explícita.
- Resolver una inconsistencia "eligiendo en silencio" una de las versiones (viola P1).
- Eliminar información histórica en vez de marcarla obsoleta (viola P5).
- Introducir dependencias, servicios externos o credenciales sin declararlo.

## 6. Cómo empezar una sesión de trabajo

1. Lee este archivo.
2. Lee `README.md` para el contexto general.
3. Lee los documentos de `docs/` relevantes a la tarea (el índice está en `docs/CONVENTIONS.md`).
4. Recién entonces, toca código.

---

*Este proyecto usa PKF (Project Knowledge Framework) v0.1.*
*El framework crece por extracción: si una sesión de trabajo revela fricción real,
anótala en `docs/friction-log.md` en vez de improvisar una solución estructural.*
