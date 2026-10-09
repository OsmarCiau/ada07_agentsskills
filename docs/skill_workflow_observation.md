# Observación del Workflow (Workflow Observation)

Documento previo al diseño de la Skill `reviewing_pull_requests`. Captura los pasos reales, entradas, decisiones y límites identificados al ejecutar manualmente el flujo de revisión de Pull Requests en el proyecto.

---

## 1. Trigger
¿Cuándo debería utilizarse este workflow?
- Cuando un desarrollador solicita evaluar si un Pull Request o rama de trabajo está listo para revisión humana formal (*PR readiness review*).
- Cuando se pide contrastar un conjunto de cambios (*diff*) contra la especificación (`SPEC.md` / ERS) y la evidencia de pruebas antes de autorizar la fusión.

## 2. Inputs
¿Qué necesita para iniciar?
- Identificador del Pull Request (ej. PR #28) o nombre de la rama local a inspeccionar.
- Acceso de solo lectura al repositorio y su historial de commits.
- Documentos normativos del proyecto (`SPEC.md`, `REQUIREMENTS.md` o contrato de arquitectura) si existen.
- Suite de pruebas unitarias o de integración asociadas al cambio.

## 3. Steps Performed
Pasos ejecutados durante la revisión previa:
1. Identificar el PR o rama y descargar la lista de archivos modificados y el diff.
2. Localizar y leer los requisitos o especificaciones vinculados al cambio (ej. Supuesto III del ERS v2.0 para catálogo).
3. Mapear cada archivo modificado con el comportamiento esperado y descartar cambios fuera de alcance.
4. Identificar las pruebas unitarias y de integración que respaldan el nuevo comportamiento.
5. Ejecutar o revisar el resultado de las suites de prueba (`npm run test:unit`, `npm run test:db`).
6. Contrastar el código contra un checklist de calidad (legibilidad, manejo de errores, tipado y seguridad).
7. Clasificar los hallazgos según severidad objetiva (MUST FIX, SHOULD FIX, OPTIONAL).
8. Generar un informe estructurado de preparación para el revisor humano.

## 4. Decisions
¿Qué decisiones requieren criterio del LLM?
- Interpretar la intención y alcance del cambio frente a la especificación técnica.
- Evaluar si un cambio secundario es un refactor aceptable o un cambio no documentado (*scope creep*).
- Calificar la severidad de un hallazgo (distinguir entre un defecto bloqueante y una sugerencia de estilo).
- Redactar explicaciones claras y sugerencias de remediación para el desarrollador.

## 5. Deterministic Work
¿Qué pasos deberían ser scripts/comandos?
- Ejecución de pruebas automatizadas en consola (`vitest`, `pytest`, `node:test`).
- Verificación de tipos estáticos (`npx tsc --noEmit`) y linter (`npx eslint`).
- Comprobación estructural del reporte generado (asegurar que contenga todas las secciones obligatorias y el indicador de decisión humana).

## 6. Reference Knowledge
¿Qué checklist, criterios o convenciones se consultaron?
- Checklist de revisión de código (trazabilidad a requisitos, ausencia de credenciales, límites arquitectónicos).
- Guía de severidad para estandarizar la prioridad de los hallazgos.
- Contrato de arquitectura del módulo (`contrato-catalogo.md`).

## 7. Output
¿Qué artefacto produce?
- Un reporte local estructurado en Markdown (`results/pr-readiness-review.md`) con el veredicto de preparación, desglose de hallazgos por severidad y resumen de pruebas.

## 8. Stop Conditions
¿Cuándo debe detenerse y pedir intervención humana?
- Siempre al finalizar el reporte: la Skill es de nivel *Draft-Only* y nunca aprueba, comenta ni fusiona el PR.
- Si existe una contradicción insalvable entre los requisitos de negocio y la especificación técnica.
- Si el usuario solicita explícitamente modificar código remoto o hacer merge en GitHub (la Skill debe rechazar la acción y solicitar aprobación humana).
