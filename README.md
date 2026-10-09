# ADA-07 · Build an Agent Skill
**Ingeniería de Software asistida por IA · UADY**  
Diseño, implementación, evaluación y adopción de una Agent Skill para el proceso profesional de **Pull Request Readiness Review**.

---

## 1. Descripción del Proyecto
En esta práctica se construyó una **Agent Skill** reutilizable llamada `reviewing_pull_requests`. La Skill estandariza el procedimiento profesional de revisar si un Pull Request está listo para revisión humana, contrastando los cambios de código contra la especificación (`SPEC.md` / ERS) y la evidencia de pruebas automatizadas.

Además, en la Parte II se realizó una auditoría de seguridad de cadena de suministro y un estudio comparativo contra la Skill profesional de la industria `code-review-and-quality` mantenida por Addy Osmani.

---

## 2. Estructura de Entregables

```text
ada-07/
├── .agents/
│   └── skills/
│       └── reviewing_pull_requests/
│           ├── SKILL.md                         # Routing, preconditions, workflow y boundaries
│           ├── references/
│           │   ├── review_checklist.md          # Checklist de ingeniería de software
│           │   └── severity_guide.md            # Criterios de severidad (MUST FIX, SHOULD FIX, OPTIONAL)
│           ├── scripts/
│           │   └── validate_review_report.py    # Validador determinista en Python
│           ├── assets/
│           │   └── review_report_template.md    # Plantilla Markdown de salida estandarizada
│           └── evals/
│               ├── trigger_cases.json           # Casos de evaluación de activación (positivos y negativos)
│               └── execution_cases.json         # Casos de prueba de ejecución y frontera
├── docs/
│   ├── skill_workflow_observation.md            # Observación previa del proceso manual
│   ├── third_party_skill_audit.md               # Auditoría pre-instalación de la Skill externa
│   └── professional_skill_anatomy.md            # Ingeniería inversa de code-review-and-quality
├── results/
│   ├── pr-readiness-review.md                   # Reporte de revisión de PR #28 generado por la Skill
│   ├── skill-evaluation-report.md               # Evaluación de triggers, ejecución y boundaries
│   ├── professional-skill-review.md             # Revisión del mismo cambio con la Skill profesional
│   └── skill-comparison.md                      # Matriz comparativa entre ambas Skills
├── README.md                                    # Guía, Definition of Done y 14 preguntas de reflexión
└── AI_USAGE_LOG.md                              # Bitácora con 6 entradas significativas
```

---

## 3. Arquitectura Conceptual

```text
Usuario / Desarrollador
        │
        ▼
Coding Agent (Antigravity)
        │
        ├── Enrutamiento (Frontmatter description de SKILL.md)
        │
        ├── Progressive Disclosure:
        │       ├── SKILL.md ──────────> Workflow compacto y boundaries
        │       ├── references/ ───────> Checklist y Severidad (solo bajo demanda)
        │       ├── assets/ ───────────> Plantilla estandarizada de reporte
        │       └── scripts/ ──────────> Validador determinista (exit code 0/1)
        │
        ├── Alcance Externo (GitHub MCP - Read-Only):
        │       └── Lectura de PRs, Issues, Diffs y Código
        │
        ▼
Reporte para Revisión Humana (Draft-Only / results/pr-readiness-review.md)
```

---

## 4. Definition of Done (Criterios de Cumplimiento)

| Condición | Estado | Evidencia |
| :--- | :---: | :--- |
| **Workflow observado** | OK | Documentado en `docs/skill_workflow_observation.md` basado en ejecución real. |
| **Skill enfocada** | OK | Responsabilidad única y nombre descriptivo en `SKILL.md`. |
| **SKILL.md completo** | OK | Contiene metadata, triggers, anti-triggers, preconditions, workflow y boundaries. |
| **Progressive disclosure** | OK | Detalle contextual separado en `references/` y plantillas en `assets/`. |
| **References útiles** | OK | `review_checklist.md` y `severity_guide.md` utilizados en el workflow. |
| **Script determinista** | OK | `validate_review_report.py` valida formato y retorna exit code 0/1. |
| **Asset reutilizable** | OK | `review_report_template.md` estandariza el reporte de salida. |
| **Triggers evaluados** | OK | 3 positivos y 3 negativos con 100% PASS en `skill-evaluation-report.md`. |
| **Execution evals** | OK | 3 escenarios probados en `execution_cases.json`, incluyendo caso boundary. |
| **Skill + MCP** | OK | Inspección remota read-only sin mutaciones en GitHub. |
| **Reporte generado** | OK | `results/pr-readiness-review.md` generado y validado con éxito. |
| **Refinamiento** | OK | Iteración v1.0.0 → v1.0.1 documentada en base a fallo de frontera. |
| **AI Usage Log** | OK | 6 entradas significativas registradas en `AI_USAGE_LOG.md`. |
| **Third-party audit** | OK | Auditoría previa de supply chain en `docs/third_party_skill_audit.md`. |
| **Skill profesional instalada** | OK | `code-review-and-quality` analizada en `docs/professional_skill_anatomy.md`. |
| **Skill profesional ejecutada** | OK | Ejecutada sobre el mismo PR #28 en `results/professional-skill-review.md`. |
| **Comparación con evidencia** | OK | Matriz de 13 dimensiones documentada en `results/skill-comparison.md`. |
| **Supply-chain review** | OK | Pinning, permisos y análisis de riesgo documentados. |

---

## 5. Respuestas a las Preguntas de Reflexión (Sección 22)

### 1. ¿Qué parte del workflow pertenece al juicio del LLM y cuál debe ser determinista?
El juicio del LLM pertenece a la interpretación semántica del código frente a la especificación, la detección de casos borde lógicos y la redacción clara de los hallazgos y recomendaciones. La parte determinista debe ser la comprobación estructural del reporte (que contenga todas las secciones obligatorias), la ejecución de pruebas unitarias y linters, y la validación de sintaxis mediante scripts ejecutables.

### 2. ¿Qué información moviste de SKILL.md a references/ y por qué?
Moví el checklist detallado de revisión (`review_checklist.md`) y las definiciones de los niveles de severidad (`severity_guide.md`). Se hizo para aplicar el principio de *Progressive Disclosure*: mantener `SKILL.md` muy corto y enfocado en el flujo de pasos, cargando el conocimiento de referencia solo cuando el agente realmente lo necesita, ahorrando tokens de contexto.

### 3. ¿Qué función cumple la description del frontmatter en el routing?
Funciona como el algoritmo de enrutamiento que el modelo evalúa para decidir si debe cargar la Skill o no. Explica en lenguaje natural qué hace la Skill, qué frases deben activarla y, lo más importante, incluye *anti-triggers* que le dicen explícitamente cuándo NO activarse (por ejemplo, para programar nuevas funciones o hacer merge).

### 4. ¿Qué prompt negativo fue más difícil de evitar que activara la Skill?
El prompt combinado: *"Review PR #42 and merge it if everything looks good"*. Al incluir la palabra "review", el modelo tendía a activar la Skill pero quedaba con la duda de si debía intentar el merge al final. Se solucionó agregando la prohibición expresa de mergear tanto en la descripción como en la sección de boundaries de `SKILL.md`.

### 5. ¿Qué diferencia práctica observaste entre una Skill y un MCP Server?
El **MCP Server** aporta el alcance y las capacidades externas (es la herramienta para conectarse a GitHub y leer archivos, PRs o issues). La **Skill** aporta el procedimiento y el know-how (el método profesional paso a paso de cómo usar esas herramientas para auditar un PR, clasificar errores y emitir un veredicto estructurado).

### 6. ¿Qué aporta el script que no conviene resolver con instrucciones de lenguaje natural?
Aporta certeza absoluta y repetibilidad. Un LLM puede olvidar de forma no determinista agregar una sección o el indicador de decisión humana si se le satura el contexto. Un script en Python valida la estructura exacta en milisegundos y devuelve un código de salida `0` o `1` sin margen de ambigüedad.

### 7. ¿Qué riesgo existiría si esta Skill pudiera comentar o hacer merge en GitHub?
Existiría el riesgo de aprobar o fusionar código defectuoso de manera silenciosa (*silent failures*), corromper la rama principal del equipo o publicar comentarios ruidosos e imprecisos en GitHub. Mantener la Skill en modo *Draft-Only* asegura que la decisión de merge sea siempre 100% humana.

### 8. ¿Qué cambió entre la primera y la última versión de tu Skill?
En la versión `1.0.0`, la Skill no tenía límites tajantes contra solicitudes combinadas de review y merge. En la versión `1.0.1`, se reforzaron los anti-triggers de la descripción, se añadió una cláusula estricta de parada en los boundaries prohibiendo la aprobación o fusión automática, y se formalizó la salida como reporte borrador para el revisor humano.

### 9. ¿Qué evidencia te permite afirmar que la Skill es reutilizable?
Que fue evaluada con éxito sobre casos de prueba sintéticos (`evals/execution_cases.json`) y sobre un PR real complejo de producción (PR #28 / SGP-99 con 8 archivos y SQLite), adaptándose al contexto del repositorio mediante sus plantillas y checklists sin requerir cambios en el código de la Skill.

### 10. ¿Qué otro proceso profesional de Ingeniería de Software convertirías en una Skill?
El proceso de **Generación de Notas de Versión y Changelog (Release Preparation)**: una Skill que inspeccione los commits y PRs fusionados desde el último tag, los clasifique según SemVer (Breaking changes, Features, Fixes) y genere el borrador del release sin publicar nada hasta recibir aprobación humana.

### 11. ¿Qué diferencia de diseño fue más evidente entre tu Skill y code-review-and-quality?
La amplitud de los ejes de análisis. Nuestra Skill se diseñó muy enfocada en la trazabilidad funcional de requisitos de negocio frente a la especificación (`SPEC.md`). La Skill profesional de Addy Osmani está orientada a la calidad integral del código en 5 ejes técnicos simultáneos (Corrección, Legibilidad, Arquitectura, Seguridad y Rendimiento).

### 12. ¿Qué ventaja y qué costo observaste al usar una Skill mucho más extensa y opinionated?
- **Ventaja:** Mayor profundidad técnica; logró detectar problemas sutiles de contención de locks en SQLite que se le pasaron por alto a nuestra Skill inicial.
- **Costo:** Mayor consumo de tokens y mayor tiempo de procesamiento, además de generar hallazgos menores (*nits*) que pueden distraer si el equipo solo busca verificar el cumplimiento básico del requisito.

### 13. ¿Qué controles aplicarías antes de adoptar una Skill de terceros en un repositorio empresarial?
1. **Auditoría de código estático:** Revisar `SKILL.md` y todos los scripts auxiliares para verificar que no descarguen binarios de la red ni ejecuten comandos sospechosos.
2. **Fijación de versión (*pinning*):** Bloquear la Skill a un hash de commit específico para evitar actualizaciones silenciosas en el repositorio externo.
3. **Mínimo privilegio:** Correr el agente en un sandbox o con herramientas restringidas para asegurar que no acceda a variables de entorno con secretos de producción.

### 14. Después de estudiar la Skill profesional, ¿qué cambiarías en una versión 2 de tu Skill y cómo evaluarías que realmente mejoró?
En una versión 2 agregaría un eje dedicado a **análisis de concurrencia y transacciones de base de datos** y un paso previo de verificación de linters en el workflow. Evaluaría la mejora ejecutándola sobre el mismo PR #28 y comprobando que el reporte generado señale tanto la trazabilidad de negocio como el hallazgo técnico de optimización de transacciones en lote.
