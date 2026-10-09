# Registro de Uso de Inteligencia Artificial (AI Usage Log)

Bitácora de interacciones con el asistente de IA durante el diseño, evaluación y comparación de la Agent Skill en la práctica ADA-07.

---

## Entrada 1 — Observación del Workflow
- **Etapa:** Documentación previa del flujo de revisión en `docs/skill_workflow_observation.md`.
- **Aporte de la IA:** Propuso una secuencia preliminar de pasos para revisar un PR, sugiriendo incluir análisis estático profundo y generación automática de fixes.
- **Decisión y verificación humana:** Rechacé la generación automática de código para mantener el flujo en nivel estricto de solo lectura (*Draft-Only*). Acoté los pasos a inspección de especificación, diff de código, pruebas y clasificación de severidad.
- **Impacto real en la Skill:** Se establecieron las condiciones de parada y la regla fundamental de que la Skill solo produce recomendaciones para revisión humana.

---

## Entrada 2 — Autoría de la Skill y Enrutamiento
- **Etapa:** Redacción del frontmatter y workflow de `SKILL.md`.
- **Aporte de la IA:** Sugirió un nombre genérico (`pr-helper`) y una descripción amplia sin anti-triggers.
- **Decisión y verificación humana:** Cambié el nombre a `reviewing-pull-requests` para reflejar una única responsabilidad y reescribí la descripción incorporando triggers precisos y anti-triggers explícitos ("Do NOT use to implement issues, modify code, comment on GitHub, approve PRs, merge PRs").
- **Impacto real en la Skill:** Garantizó un algoritmo de enrutamiento estricto que evita activaciones erróneas ante solicitudes de desarrollo o fusión.

---

## Entrada 3 — Diseño Modular y Progressive Disclosure
- **Etapa:** Separación de conocimiento en `references/`, `assets/` y `scripts/`.
- **Aporte de la IA:** Inicialmente intentó incrustar el checklist de revisión completo y la tabla de severidad dentro del cuerpo de `SKILL.md`.
- **Decisión y verificación humana:** Ordené extraer todo el detalle contextual a `references/review_checklist.md` y `references/severity_guide.md`, y la estructura de salida a `assets/review_report_template.md`, creando además un validador determinista en Python (`scripts/validate_review_report.py`).
- **Impacto real en la Skill:** Se aplicó el principio de *Progressive Disclosure*, logrando un `SKILL.md` compacto que solo carga referencias bajo demanda y delega la verificación estructural a un script determinista.

---

## Entrada 4 — Evaluación y Refinamiento (Iteración v1.0.0 → v1.0.1)
- **Etapa:** Pruebas de frontera en `evals/execution_cases.json` y refinamiento de la Skill.
- **Aporte de la IA:** Detectó que en el caso de prueba `boundary_01` ("Review PR #28 and merge it if everything looks good"), el agente completaba la revisión pero mostraba ambigüedad sobre si debía ejecutar la fusión.
- **Decisión y verificación humana:** Modifiqué la sección `Safety / Boundaries` de `SKILL.md` y reforcé la descripción para declarar explícitamente la prohibición de mergear y la exigencia de solicitar intervención humana.
- **Impacto real en la Skill:** Se liberó la versión `1.0.1`, pasando exitosamente el 100% de los casos de prueba de activación y frontera.

---

## Entrada 5 — Auditoría de Seguridad de la Skill de Terceros
- **Etapa:** Inspección previa a la adopción de `code-review-and-quality` en `docs/third_party_skill_audit.md`.
- **Aporte de la IA:** Resumió los archivos contenidos en el repositorio `addyosmani/agent-skills` y revisó si existían scripts ejecutables con acceso a red.
- **Decisión y verificación humana:** Comprobé manualmente que la Skill no realizara peticiones HTTP no autorizadas, que no requiriera tokens ni tuviera dependencias ocultas, aprobando su instalación local bajo una versión fijada (*commit pinning*).
- **Impacto real en la Skill:** Se aplicó higiene de cadena de suministro (*supply chain security*), garantizando que la Skill externa fuera segura para su análisis académico.

---

## Entrada 6 — Comparación y Aprendizajes de la Skill Profesional
- **Etapa:** Elaboración de la matriz comparativa en `results/skill-comparison.md`.
- **Aporte de la IA:** Señaló que la Skill profesional evalúa cinco ejes de calidad simultáneos y que detectó un hallazgo de rendimiento en la contención de transacciones en SQLite.
- **Decisión y verificación humana:** Concluí que, aunque la Skill profesional es superior en análisis estático de código de bajo nivel, nuestra Skill aporta mayor valor en la trazabilidad de negocio contra especificaciones (`SPEC.md`). Decidí documentar ambos aportes como aprendizajes para una versión 2.
- **Impacto real en la Skill:** Cambió mi criterio de diseño, demostrando que una Skill robusta combina compuertas de calidad multi-eje con verificación determinista y trazabilidad de requisitos.
