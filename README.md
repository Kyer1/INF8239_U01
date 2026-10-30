# INF-8239 Ciencia de Datos II — Unidad 01

**Autora:** Kimberly Pereyra

## Ejercicio 01 · Deserción estudiantil con SVM reproducible

- **Pregunta:** ¿Es posible identificar al final del 1er semestre qué estudiantes abandonarán, seguirán matriculados o se graduarán?
- **Dataset:** *Predict Students' Dropout and Academic Success* — UCI ML Repository, id 697. Realinho, V. et al. (2021). DOI 10.24432/C5MC89. Licencia CC BY 4.0.
- **Unidad de análisis:** un estudiante (4,424 filas).
- **Target:** `Target` (Dropout, Enrolled, Graduate).
- **Métrica principal:** F1 macro; se vigila el recall de Dropout.
- **Prevención de fuga:** se excluyen las 6 variables `Curricular units 2nd sem (...)` porque no están disponibles al final del 1er semestre.

### Resultados (conjunto de prueba, 20 %)

| Modelo | F1 macro | Recall Dropout |
|---|---|---|
| Dummy (most_frequent) | 0.2221 | 0.0000 |
| SVM base (C=1, gamma=scale) | 0.6321 | 0.6831 |
| SVM ajustada (C=10, gamma=0.01, balanced) | **0.6677** | 0.6655 |

## Entorno
- Windows 11 (10.0.26300), Python 3.11.9, Git 2.56.0, scikit-learn 1.9.1

## Estructura
```
data/raw/    dataset descargado (no se versiona)
docs/        ficha y comparación de datasets
notebooks/   00 verificación · 01 SVM guiada · 02 deserción SVM (Ejercicio 01)
reports/     CSV de resultados, matrices de confusión y modelos
src/         paquete inf8239_u01 (data.py, models.py)
tests/       pruebas unitarias y contrato de datos
```

## Instalación (Windows, cmd)
```
git clone <URL-del-repositorio>
cd INF8239_U01
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Descarga reproducible del dataset
```
set PYTHONPATH=src
python -c "from inf8239_u01.data import download_csv; print(download_csv())"
```
Descarga el ZIP oficial de UCI y lo guarda en `data/raw/dataset.csv`. El notebook también lo descarga automáticamente si no existe.

## Ejecución
1. Abrir `notebooks/02_desercion_svm.ipynb`, seleccionar el kernel `.venv` y usar **Run All**.
2. Pruebas:
```
set PYTHONPATH=src
python -m pytest -q
```
Resultado esperado: `8 passed`.

## Nota de entorno
Con scikit-learn 1.9 aparece un `FutureWarning`