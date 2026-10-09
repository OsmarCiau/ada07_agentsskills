# Comparación de Skills (Skill Comparison)

Análisis comparativo basado en evidencia entre nuestra Skill personalizada (`reviewing-pull-requests`) y la Skill profesional de la industria (`code-review-and-quality` de Addy Osmani), evaluadas sobre el mismo cambio de código (PR #28 en `SGP---Sistema-de-gestion-publicitaria`).

---

## 1. Matriz Comparativa por Dimensiones

| Dimensión | Nuestra Skill (`reviewing-pull-requests`) | Skill Profesional (`code-review-and-quality`) | Conclusión / Aprendizaje |
| :--- | :--- | :--- | :--- |
| **Trigger / Routing** | Enfocada en comprobar si un PR está listo para revisión humana frente a la especificación. | Enfocada en auditoría de calidad de código previa al merge en múltiples escenarios. | Ambas delimitan claramente cuándo activarse y cuándo rechazar la tarea mediante anti-triggers. |
| **Scope / Boundaries** | Estrictamente *Draft-Only*; prohíbe comentar, aprobar o mergear en GitHub. | Estrictamente *Draft-Only*; emite dictamen estructurado y deja la autoridad en el revisor humano. | Ambas coinciden en que una Skill de revisión no debe realizar acciones destructivas ni cambios silenciosos. |
| **Workflow Depth** | 10 pasos lineales con validación determinista del artefacto de salida. | 4 compuertas de calidad (*reconnaissance*, auditoría multi-eje, verificación y dictamen). | La profesional profundiza más en el análisis estático; nuestra Skill enfatiza la trazabilidad con especificaciones. |
| **Correctness** | Comprueba mapeo de requisitos del ERS y pruebas unitarias existentes. | Analiza lógica, manejo de casos nulos, tipos estrictos y regresiones de contrato. | La profesional detecta detalles finos de lógica de lenguaje; la nuestra valida el contrato funcional del negocio. |
| **Architecture** | Revisa respeto al contrato arquitectónico del módulo (`contrato-catalogo.md`). | Evalúa acoplamiento entre capas, patrones de diseño y dirección de dependencias. | Ambas promueven la separación entre lógica de datos y componentes visuales. |
| **Security** | Checklist básico: ausencia de credenciales embebidas y sanitización general. | Eje dedicado: inyección SQL/prompt, manejo de variables de entorno y validación profunda de entradas. | La profesional tiene un lente de seguridad mucho más riguroso y formal. |
| **Performance** | No evalúa rendimiento de forma explícita a menos que lo mencione un test. | Eje dedicado: análisis de complejidad algorítmica, bloqueos de concurrencia y transacciones costosas. | La profesional identificó el riesgo de contención de locks en SQLite que nuestra Skill omitió. |
| **Tests / Verification** | Exige evidencia de pruebas unitarias y de base de datos ejecutadas. | Exige evidencia de suites de prueba, verificación de tipos y linters con cero advertencias. | Ambas impiden declarar éxito sin evidencia verificable en consola. |
| **Severity Model** | 3 niveles: MUST FIX, SHOULD FIX, OPTIONAL. | 3 niveles: BLOCKER / CRITICAL, IMPORTANT, NIT / SUGGESTION. | Modelos conceptualmente equivalentes; el profesional está más estandarizado en la industria. |
| **Human Review** | Obligatorio; el validador exige la línea explícita `Human decision required: YES`. | Obligatorio; el dictamen resume decisiones que requieren firma del arquitecto. | Nuestra Skill cuenta con un script determinista que fuerza la presencia del campo de decisión humana. |
| **References / Composition** | Checklist y guía de severidad cargados bajo demanda (*progressive disclosure*). | Rúbricas especializadas y sugerencia de componerse con `security-and-hardening` o `performance`. | La profesional introduce el concepto de componer varias Skills para auditorías avanzadas. |
| **Reusability** | Altamente reusable para proyectos que sigan especificaciones formales y pruebas. | Altamente reusable y genérica para cualquier base de código moderna (Node, Go, Python). | La profesional tiene mayor versatilidad de dominio al no acoplarse a un formato específico de ERS. |

---

## 2. Análisis Cualitativo

### 1. ¿Qué hace la Skill profesional que tu Skill no contempló?
Incorporó una auditoría explícita de **rendimiento y concurrencia** (*performance axis*). Esto le permitió detectar que ejecutar múltiples sentencias SQL individuales dentro de una transacción en un bucle puede retener el bloqueo exclusivo de escritura de SQLite más tiempo del debido. Nuestra Skill inicial se centró en si la funcionalidad cumplía con los requisitos y pasaba las pruebas, pasando por alto la eficiencia de la transacción.

### 2. ¿Qué elementos de tu Skill son más específicos al curso/proyecto y conviene conservar?
1. **La trazabilidad directa hacia documentos de requisitos del proyecto** (`SPEC.md` y Supuestos del ERS v2.0): nuestra Skill verifica explícitamente si cada cambio corresponde a un criterio de aceptación documentado.
2. **El validador determinista en Python (`scripts/validate_review_report.py`)**: asegura por código que el reporte no omita ninguna sección obligatoria ni el indicador de decisión humana, algo que la Skill profesional confía únicamente al seguimiento de instrucciones del modelo.

### 3. ¿Qué agregarías a una versión 2 de tu Skill?
- Incorporar un eje de evaluación de rendimiento y transacciones en bases de datos.
- Agregar recomendaciones de composición con otras Skills (por ejemplo, auditoría de seguridad).
- Añadir verificación automatizada de linter y compilación dentro de los pasos del workflow antes de generar el reporte.

### 4. ¿Qué NO copiarías y por qué?
No copiaría la sobre-generalización de checklists agnósticos al negocio. En entornos guiados por especificación (*spec-driven development* como el de nuestro curso), es mucho más valioso comprobar que el código resuelva el requisito de negocio pactado en lugar de limitarse a evaluar si el código es sintácticamente elegante o idiomático.

### 5. ¿Cuál produjo hallazgos más accionables? Incluye dos ejemplos.
Ambas aportaron valor complementario, pero la **Skill profesional produjo hallazgos más técnicos y accionables a nivel de código de bajo nivel**:
- **Ejemplo 1 (Hallazgo técnico de la profesional):** En `setDisponibilidadLote`, señaló el problema de enviar queries individuales en bucle dentro de un `BEGIN/COMMIT` en SQLite y propuso la solución exacta (construir una sola sentencia con múltiples `VALUES` o reusar prepared statements para reducir contención de locks).
- **Ejemplo 2 (Hallazgo de trazabilidad de nuestra Skill):** Señaló claramente que la falta de interfaz de usuario en el PR no era un defecto ni un olvido, sino que estaba planificada para los tickets SGP-100 y SGP-101 según el contrato técnico de arquitectura, evitando un falso positivo que habría bloqueado el flujo del equipo.
