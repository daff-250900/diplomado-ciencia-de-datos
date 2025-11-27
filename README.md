# CTG_VIZ - Librería de Visualización de Datos

Librería Python para análisis exploratorio y visualización de datos con Plotly.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso Básico](#uso-básico)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Funciones Principales](#funciones-principales)
  - [Categorización de Variables](#categorización-de-variables)
  - [Preprocesamiento](#preprocesamiento)
  - [Visualizaciones](#visualizaciones)
- [Ejemplos](#ejemplos)
- [Testing](#testing)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Descripción

`ctg_viz` es una librería de Python diseñada para facilitar el análisis exploratorio de datos (EDA) mediante visualizaciones interactivas utilizando Plotly. Proporciona funciones para:

- Clasificación automática de variables en continuas y discretas
- Detección y visualización de datos faltantes
- Generación de múltiples tipos de gráficos interactivos (boxplots, violin plots, density plots, heatmaps, etc.)
- Análisis de distribuciones y relaciones entre variables

## Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación de Dependencias

```bash
pip install -r requirements.txt
```

Las principales dependencias incluyen:
- `pandas`: Manipulación y análisis de datos
- `numpy`: Operaciones numéricas
- `plotly`: Visualizaciones interactivas
- `scipy`: Cálculos estadísticos
- `IPython`: Visualización de datos en notebooks

## Uso Básico

```python
import pandas as pd
from ctg_viz.categorization import categorization
from ctg_viz.preprocessing import check_data_completeness
from ctg_viz.plots.boxplots import plot_boxplot
from ctg_viz.plots.density import plot_density

# Cargar datos
df = pd.DataFrame({
    'edad': [25, 30, 35, 40, 45],
    'salario': [30000, 45000, 55000, 60000, 70000],
    'categoria': ['A', 'B', 'A', 'C', 'B']
})

# Crear objeto para análisis
class CTGViz:
    def __init__(self, df):
        self.df = df

viz = CTGViz(df)

# Categorizar variables
continuas, discretas = categorization(viz)
print(f"Variables continuas: {continuas}")
print(f"Variables discretas: {discretas}")

# Verificar completitud de datos
check_data_completeness(viz)

# Generar visualizaciones
plot_boxplot(df, target=['categoria'])
plot_density(df, x_col='edad', group_by='categoria')
```

## Estructura del Proyecto

```
diplomado-ciencia-de-datos/
├── ctg_viz/                      # Paquete principal
│   ├── __init__.py
│   ├── categorization.py         # Clasificación de variables
│   ├── preprocessing.py          # Preprocesamiento de datos
│   └── plots/                    # Módulos de visualización
│       ├── __init__.py
│       ├── barplots.py          # Gráficos de barras
│       ├── boxplots.py          # Diagramas de caja
│       ├── density.py           # Gráficos de densidad
│       ├── dotplots.py          # Gráficos de puntos
│       ├── heatmap.py           # Mapas de calor
│       ├── histograms.py        # Histogramas
│       ├── lineplots.py         # Gráficos de línea
│       └── violin.py            # Gráficos de violín
├── tests/                        # Pruebas unitarias
│   ├── __init__.py
│   ├── test_boxplots.py
│   ├── test_categorization.py
│   ├── test_density.py
│   └── test_preprocessing.py
├── requirements.txt              # Dependencias del proyecto
├── p3.ipynb                      # Notebook de ejemplo
└── README.md                     # Este archivo
```

## Funciones Principales

### Categorización de Variables

**`categorization(self) -> tuple[list[str], list[str]]`**

Clasifica automáticamente las variables del DataFrame en continuas y discretas.

**Criterios:**
- **Continuas**: Variables numéricas (int64/float64) con más de 10 valores únicos
- **Discretas**: Variables categóricas (object, bool) o numéricas con ≤10 valores únicos

```python
continuas, discretas = categorization(viz)
```

### Preprocesamiento

**`check_data_completeness(self) -> None`**

Analiza y visualiza la completitud de los datos en el DataFrame, mostrando:
- Número total de filas y columnas
- Porcentaje de datos completos
- Desglose de valores faltantes por columna
- Tabla HTML con el resumen

```python
check_data_completeness(viz)
```

### Visualizaciones

#### Boxplots

**`plot_boxplot(df, target, show=True)`**

Genera diagramas de caja para analizar la distribución de variables numéricas agrupadas por variables objetivo.

**Parámetros:**
- `df` (DataFrame): DataFrame con los datos
- `target` (list): Lista de variables categóricas para agrupar
- `show` (bool): Si mostrar el gráfico inmediatamente

```python
plot_boxplot(df, target=['categoria', 'grupo'])
```

#### Density Plots

**`plot_density(df, x_col, group_by=None, show=True)`**

Genera gráficos de densidad KDE (Kernel Density Estimation).

**Parámetros:**
- `df` (DataFrame): DataFrame con los datos
- `x_col` (str): Columna para calcular la densidad
- `group_by` (str, opcional): Variable para agrupar
- `show` (bool): Si mostrar el gráfico

```python
# Densidad simple
plot_density(df, x_col='edad')

# Densidad por grupos
plot_density(df, x_col='salario', group_by='categoria')
```

#### Violin Plots

**`plot_violinplot(df, x_col, y_col, overlay_swarm=False, show=True)`**

Genera gráficos de violín con opción de overlay con swarm plot.

**Parámetros:**
- `df` (DataFrame): DataFrame con los datos
- `x_col` (str): Variable categórica (eje X)
- `y_col` (str): Variable numérica (eje Y)
- `overlay_swarm` (bool): Agregar puntos individuales
- `show` (bool): Si mostrar el gráfico

```python
plot_violinplot(df, x_col='categoria', y_col='salario', overlay_swarm=True)
```

#### Heatmaps

**`plot_heatmap(df, method='pearson', show=True)`**

Genera mapas de calor de correlación entre variables numéricas.

**Parámetros:**
- `df` (DataFrame): DataFrame con los datos
- `method` (str): Método de correlación ('pearson', 'spearman', 'kendall')
- `show` (bool): Si mostrar el gráfico

```python
plot_heatmap(df, method='pearson')
```

#### Dotplots

**`plot_dotplot(df, x_col, y_col, overlay=None, group1=None, group2=None, show=True)`**

Genera gráficos de puntos con opción de comparación entre grupos.

**Parámetros:**
- `df` (DataFrame): DataFrame con los datos
- `x_col` (str): Variable del eje X
- `y_col` (str): Variable del eje Y
- `overlay` (str): Variable para overlay de comparación
- `group1`, `group2` (str): Valores específicos para comparar
- `show` (bool): Si mostrar el gráfico

```python
# Dotplot simple
plot_dotplot(df, x_col='edad', y_col='salario')

# Dotplot con comparación
plot_dotplot(df, x_col='edad', y_col='salario', 
             overlay='categoria', group1='A', group2='B')
```

#### Line Plots

**`plot_lineplot(df, x_col=None, y_cols=None, group_by=None, show=True)`**

Genera gráficos de línea para visualizar tendencias.

**Parámetros:**
- `df` (DataFrame): DataFrame con los datos
- `x_col` (str, opcional): Variable del eje X
- `y_cols` (list, opcional): Lista de columnas para graficar
- `group_by` (str, opcional): Variable para agrupar
- `show` (bool): Si mostrar el gráfico

```python
plot_lineplot(df, x_col='fecha', y_cols=['ventas', 'costos'])
```

## Ejemplos

### Ejemplo Completo de Análisis Exploratorio

```python
import pandas as pd
from ctg_viz.categorization import categorization
from ctg_viz.preprocessing import check_data_completeness
from ctg_viz.plots.boxplots import plot_boxplot
from ctg_viz.plots.density import plot_density
from ctg_viz.plots.heatmap import plot_heatmap
from ctg_viz.plots.violin import plot_violinplot

# Cargar datos
df = pd.read_csv('datos.csv')

# Crear objeto de análisis
class CTGViz:
    def __init__(self, df):
        self.df = df

viz = CTGViz(df)

# 1. Clasificar variables
continuas, discretas = categorization(viz)
print(f"Variables continuas ({len(continuas)}): {continuas}")
print(f"Variables discretas ({len(discretas)}): {discretas}")

# 2. Verificar calidad de datos
check_data_completeness(viz)

# 3. Análisis de correlaciones
plot_heatmap(df[continuas], method='pearson')

# 4. Distribuciones por categoría
if len(discretas) > 0:
    plot_boxplot(df, target=[discretas[0]])
    
    for var_continua in continuas[:3]:  # Primeras 3 variables
        plot_density(df, x_col=var_continua, group_by=discretas[0])
        plot_violinplot(df, x_col=discretas[0], y_col=var_continua, 
                       overlay_swarm=True)
```

### Ejemplo con Datos Faltantes

```python
# Crear datos con valores faltantes
import numpy as np

df = pd.DataFrame({
    'edad': [25, 30, np.nan, 40, 45],
    'salario': [30000, np.nan, 55000, 60000, 70000],
    'categoria': ['A', 'B', None, 'C', 'B']
})

viz = CTGViz(df)

# Verificar completitud (muestra tabla con No., % de datos faltantes, la información principal, así como estadisticas descriptivas del dataframe)
check_data_completeness_dafnelizabethzepedagonzalez(viz)

# Las funciones de visualización manejan automáticamente valores NaN
plot_boxplot(df, target=['categoria'])
```

## Testing

El proyecto incluye pruebas unitarias para garantizar el correcto funcionamiento de algunas funciones clave como .

### Ejecutar Todos los Tests

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

### Ejecutar Tests Específicos

```bash
# Test de categorización
python3 -m unittest tests.test_categorization -v

# Test de boxplots
python3 -m unittest tests.test_boxplots -v

# Test de density plots
python3 -m unittest tests.test_density -v

# Test de preprocesamiento
python3 -m unittest tests.test_preprocessing -v
```

### Cobertura de Tests

Los tests actuales cubren:
- ✅ Clasificación de variables continuas y discretas
- ✅ Detección de datos faltantes
- ✅ Generación de boxplots con múltiples targets
- ✅ Generación de density plots simples y agrupados
- ✅ Manejo de datos faltantes en visualizaciones

## Uso de Git

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia

Este proyecto fue desarrollado como práctica del Diplomado en Ciencia de Datos.

---

**Proyecto creado y mantenido por:** por Dafne (Data Engineer en transición a Ciencia de Datos).
**Año:** 2025