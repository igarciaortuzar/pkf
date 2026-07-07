# {NOMBRE_DEL_PROYECTO}

<!-- PLANTILLA: este README es para humanos que llegan por primera vez.
     Reemplazar los marcadores {ASÍ} al inicializar el proyecto. -->

{Una descripción de dos o tres frases: qué hace este proyecto y para quién.}

## Cómo está organizado

Este proyecto usa **PKF v0.1** (Project Knowledge Framework), una estructura mínima
para que tanto personas como IAs puedan trabajar en el repositorio sin depender
de contexto externo.

| Si buscas... | Ve a... |
|---|---|
| Entender el proyecto | Este README |
| Colaborar con una IA | `AGENTS.md` (reglas de colaboración) |
| Las reglas de negocio | `docs/business-rules.md` |
| Por qué se decidió algo | `docs/adr/` |
| Convenciones de docs | `docs/CONVENTIONS.md` |

## Cómo empezar

{Instrucciones de instalación/uso del proyecto en sí.}

## Agregar o deprecar una regla de negocio

Para agregar una regla de negocio (RN-xxx) a `docs/business-rules.md`:

```bash
python tools/add_rn.py create \
  --numero 001 \
  --titulo "Título corto de la regla" \
  --regla "Enunciado preciso, verificable, sin ambigüedad." \
  --origen "Contrato / cliente / normativa / decisión interna (referencia)" \
  [--fecha AAAA-MM-DD]  # opcional, default: hoy
```

Para marcar una regla como obsoleta:

```bash
python tools/add_rn.py deprecate \
  --numero 001 \
  --reemplazada-por RN-002 \
  [--fecha AAAA-MM-DD]  # opcional, default: hoy
```

El script valida automáticamente:

- Que el número sea correlativo (evita duplicados)
- Que no haya inyección de Markdown
- Que el archivo se escriba de forma atómica (segura)

## Validar consistencia

```bash
python tools/check_refs.py
```

Verifica que toda referencia a reglas de negocio (RN-xxx) y decisiones (ADR-xxx)
apunte a algo que existe. Correr antes de cada commit relevante.

