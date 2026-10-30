# Ficha del dataset

- **Dominio:** Educación superior — deserción y éxito académico.
- **Unidad de análisis:** un estudiante de pregrado (una fila = un estudiante).
- **Decisión:** identificar al final del 1er semestre a los estudiantes en riesgo de abandono para asignarles tutoría temprana.
- **Target:** `Target` (Dropout, Enrolled, Graduate).
- **Tipo de tarea:** clasificación multiclase (3 clases).
- **Error más costoso:** predecir Graduate o Enrolled para un estudiante que en realidad abandona (Dropout): queda sin apoyo a tiempo.
- **Usuario:** equipo de tutoría y orientación académica.

## Comparación de candidatos

| Criterio | Candidato A: Predict Students' Dropout and Academic Success | Candidato B: Estimation of Obesity Levels Based on Eating Habits and Physical Condition |
|---|---|---|
| Procedencia | UCI ML Repository, id 697. Realinho, V. et al. (2021), Instituto Politécnico de Portalegre. DOI 10.24432/C5MC89 | UCI ML Repository, id 544. Mendoza Palechor, F. y De la Hoz Manotas, A. (2019). DOI 10.24432/C5H31Z |
| URL ficha | https://archive.ics.uci.edu/dataset/697 | https://archive.ics.uci.edu/dataset/544 |
| URL descarga | https://archive.ics.uci.edu/static/public/697/predict+students+dropout+and+academic+success.zip | https://archive.ics.uci.edu/static/public/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition.zip |
| Licencia | CC BY 4.0 | CC BY 4.0 |
| Filas/columnas | 4,424 × 37 (36 predictores + target) | 2,111 × 17 (16 predictores + target) |
| Target y clases | `Target`: Graduate 2,209 / Dropout 1,421 / Enrolled 794 | `NObeyesdad`: 7 niveles de peso/obesidad |
| Ausentes | No tiene | No tiene |
| Riesgo de fuga | Las variables del 2º semestre no están disponibles al final del 1er semestre → se excluyen | Alto: el target se calcula con el IMC (peso/altura²) y `Weight` y `Height` están en X. Además, 77 % de los registros son sintéticos (SMOTE) |

## Decisión propuesta
Se propone el **Candidato A**: datos reales, sin ausentes, licencia abierta, descarga directa reproducible por HTTPS, tamaño compatible con CPU y una decisión clara (alerta temprana de abandono). El Candidato B se descarta por la fuga estructural del target (IMC) y porque la mayoría de los registros son sintéticos.

**Estado:** pendiente de aprobación del docente.