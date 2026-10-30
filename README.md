# INF-8239 Ciencia de Datos II — Unidad 01

Autora: Kimberly Pereyra

## Sistema operativo y versiones
- Windows 11 (10.0.26300)
- Python 3.11.9
- Git 2.56.0

## Estructura del proyecto
```
data/        datasets (data/raw no se versiona)
notebooks/   notebooks de Jupyter
reports/     figuras y resultados
src/         código reutilizable (paquete inf8239_u01)
tests/       pruebas unitarias
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

## Ejecutar pruebas
```
set PYTHONPATH=src
python -m pytest -q
```
Resultado esperado: `1 passed`.

## Verificar Jupyter
Abrir `notebooks/00_verificacion.ipynb`, seleccionar el kernel `.venv` y ejecutar.
La ruta del intérprete debe contener `.venv`.