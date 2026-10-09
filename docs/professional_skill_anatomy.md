# Anatomía de la Skill Profesional (Reverse Engineering)

Análisis de ingeniería inversa de la Skill `code-review-and-quality` (`addyosmani/agent-skills`), identificando sus patrones de diseño, mecanismos de enrutamiento y compuertas de calidad (*quality gates*).

---

## 1. Routing
- **Mecanismo:** El frontmatter en `SKILL.md` utiliza una descripción densa pero estructurada con palabras clave discriminatorias (*keywords*) como `code review`, `diff analysis`, `merge readiness` y `code quality audit`.
- **Delimitación de intenciones:** Incluye frases negativas explícitas (*anti-triggers*) para rechazar tareas de desarrollo ("Do not use to write new features", "Do not refactor code directly"). Esto evita que el agente tome el control del teclado cuando el usuario solo solicita una opinión crítica.

## 2. Workflow y Quality Gates
El flujo sigue una secuencia disciplinada con compuertas de calidad obligatorias:
1. **Compuerta 1 (Reconnaissance):** Identificar el diff exacto y determinar el lenguaje, framework y directrices del repositorio (`AGENTS.md`, linters).
2. **Compuerta 2 (Multi-Axis Audit):** Evaluar el código en paralelo a través de 5 ejes específicos (Corrección, Legibilidad, Arquitectura, Seguridad y Rendimiento).
3. **Compuerta 3 (Verification Check):** Exigir evidencia concreta de pruebas automatizadas o ejecución de linter antes de emitir cualquier dictamen.
4. **Compuerta 4 (Synthesis & Grading):** Consolidar hallazgos categorizados por severidad y asignar un estado final (*Approve*, *Request Changes*, *Needs Human Decision*).

## 3. Ejes de Revisión (Review Axes)
- **Correctness:** Lógica de negocio, manejo de casos borde (*null*, límites numéricos, cadenas vacías), ausencia de regresiones en contratos existentes.
- **Readability / Simplicity:** Carga cognitiva, nombres descriptivos de variables y funciones, ausencia de código muerto (*dead code*) y apego al principio de responsabilidad única.
- **Architecture:** Límites entre módulos, encapsulamiento, dirección de dependencias y respeto a la separación de capas (evitar mezclar lógica de base de datos en vistas).
- **Security:** Sanitización de entradas externas, prevención de inyecciones (SQL/Prompt), manejo seguro de variables de entorno y ausencia de credenciales embebidas.
- **Performance:** Complejidad algorítmica ($O(N^2)$ evitables), contención de memoria, transacciones excesivamente largas y consultas de base de datos en bucles ($N+1$).

## 4. Modelo de Severidad
Diferencia tres niveles jerárquicos claros:
- **BLOCKER / CRITICAL:** Defectos que impiden la fusión inmediata (vulnerabilidades de seguridad, violaciones de contrato, pruebas rotas o fugas de datos).
- **IMPORTANT / SHOULD FIX:** Problemas de mantenibilidad, deuda técnica innecesaria o falta de pruebas para casos borde importantes.
- **NIT / SUGGESTION:** Mejoras menores de estilo, nombres o micro-optimizaciones que no condicionan la aprobación.

## 5. Verificación Exigida
A diferencia de revisiones superficiales de LLMs tradicionales, la Skill prohíbe emitir un veredicto positivo si no existe evidencia verificable:
- Exige citar número de archivo y línea exacta para cada hallazgo.
- Requiere comprobar que la compilación y las suites de prueba hayan concluido con éxito.

## 6. Composición
La Skill está diseñada para orquestar o recomendar capacidades complementarias:
- Sugiere componerse con `security-and-hardening` para análisis estático profundo de vulnerabilidades.
- Sugiere componerse con `performance-optimization` cuando se detectan cuellos de botella en operaciones de E/S o algoritmos pesados.

## 7. Boundaries y Autoridad
- **Draft-Only:** Todo veredicto es presentado como una recomendación estructurada para el desarrollador humano.
- **Acciones prohibidas:** No ejecuta commits automáticos, no modifica archivos fuente sin permiso explícito y no interactúa con APIs de GitHub para aprobar o fusionar ramas. La autoridad final de fusión permanece siempre en el ingeniero revisor.
