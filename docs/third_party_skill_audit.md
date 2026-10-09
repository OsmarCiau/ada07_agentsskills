# Third-Party Skill Pre-Install Audit

Auditoría de seguridad y análisis de cadena de suministro previa a la adopción de una Agent Skill de terceros, conforme a las directrices de ADA-07 (Parte II).

---

- **Repository:** `https://github.com/addyosmani/agent-skills`
- **Selected skill:** `code-review-and-quality`
- **Maintainer / Author:** Addy Osmani (Google Chrome team)
- **Version / commit inspected:** `v1.2.0` / commit `3f8a91c` (Rama `main`)
- **Installed path:** `.agents/skills/code-review-and-quality/` (local workspace / global agent skills)

---

## 1. Purpose
Proporcionar un flujo integral de revisión de código previa al merge, evaluando cinco ejes de calidad de software: corrección funcional (*correctness*), legibilidad y simplicidad (*readability*), arquitectura y acoplamiento (*architecture*), seguridad (*security*) y rendimiento (*performance*).

## 2. Trigger / Description
- **Triggers declarados:** Solicitudes explícitas de code review, análisis de calidad de diffs, preparación para merge, auditoría de Pull Requests o escaneo de deuda técnica en ramas activas.
- **Anti-triggers / Fuera de alcance:** Generación de código desde cero, refactorización automática silenciosa, despliegue a producción, aprobación o fusión de PRs en GitHub.

## 3. Supporting References
Utiliza guías modulares de soporte:
- `references/review_rubric.md`: Rúbrica detallada con criterios objetivos para evaluar los 5 ejes de calidad.
- `references/severity_levels.md`: Definición estricta de niveles de severidad (Blocker, Important, Nit).
- `references/code_smells_checklist.md`: Patrones antipatrón comunes y prácticas recomendadas de refactorización limpia.

## 4. Tools / Commands / Permissions
- **Lectura de archivos y diffs:** Requiere permisos de lectura sobre el árbol del repositorio (`git diff`, lectura de archivos fuente).
- **Ejecución determinista:** Invoca herramientas de linters o pruebas del entorno local si están configuradas (`npm test`, `pytest`, `eslint`), sin ejecutar scripts de red ni instaladores externos.
- **Acceso a red / GitHub:** No requiere credenciales externas ni permisos de escritura en la API de GitHub; el análisis se realiza como reporte local.

## 5. Potential Risks
- **Riesgo de supply chain:** Dependencia de repositorios externos en GitHub; mitigado mediante inspección estática del contenido antes de su ejecución y fijado a una versión revisada (*pinning*).
- **Inyección indirecta de prompts:** Si el diff bajo revisión incluye instrucciones maliciosas en comentarios o cadenas de texto. Mitigado al tratar el código como datos inertes de análisis.
- **Consumo excesivo de contexto (Token bloat):** Al ser una Skill extensa con múltiples ejes de revisión, puede consumir una cantidad elevada de tokens si no se limita el alcance del diff.

## 6. Decision
- [x] **Install**
- [ ] Do not install

**Reason:** La Skill proviene de una fuente pública confiable, no contiene scripts maliciosos ni solicita permisos de red o credenciales embebidas. Cumple estrictamente con el principio de mínimo privilegio y opera en modo de solo lectura local, siendo ideal para contrastarla con nuestra Skill construida en la Parte I.
