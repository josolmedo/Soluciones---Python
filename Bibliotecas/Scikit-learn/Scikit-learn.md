# 📘 Introducción a **scikit-learn**

**scikit-learn** (comúnmente conocido como `sklearn`) es una de las bibliotecas más populares de Python para **Machine Learning**. Está organizada en **módulos** especializados en diferentes tareas, lo que permite estructurar y reutilizar código de forma eficiente.

---

## 🧱 Conceptos clave

- **Módulo**:  
  Archivo `.py` que contiene código Python.

- **Paquete**:  
  Colección de módulos. Debe incluir un archivo especial llamado `__init__.py` para ser reconocido como tal por Python.

- **Biblioteca**:  
  Conjunto de paquetes que proveen funcionalidades específicas, como lo hace `scikit-learn` para el aprendizaje automático.

---

> ✅ **Resumen**:  
> `scikit-learn` es una **biblioteca** → compuesta por **paquetes** → que a su vez contienen **módulos**.


***
# 📦 Principales módulos de scikit-learn

## 1. Preprocesamiento de datos

- `sklearn.preprocessing`: Transformación y normalización de datos.  
  **Ejemplos**: `StandardScaler`, `MinMaxScaler`, `OneHotEncoder`, `LabelEncoder`.

- `sklearn.impute`: Manejo de valores faltantes.  
  **Ejemplo**: `SimpleImputer`.

- `sklearn.feature_selection`: Selección de características
 **Ejemplo**: `SelectKBest, RFECV`

## 2. Selección y extracción de características

- `sklearn.feature_selection`: Métodos para seleccionar características relevantes.  
  **Ejemplos**: `SelectKBest`, `RFECV`.

- `sklearn.feature_extraction`: Extracción de características de texto e imágenes.  
  **Ejemplos**: `CountVectorizer` (para texto), `TfidfVectorizer`.

## 3. Modelos supervisados

- `sklearn.linear_model`: Modelos lineales.  
  **Ejemplos**: `LinearRegression`, `LogisticRegression`, `Ridge`, `Lasso`.

- `sklearn.tree`: Árboles de decisión.  
  **Ejemplos**: `DecisionTreeClassifier`, `DecisionTreeRegressor`.

- `sklearn.ensemble`: Métodos ensemble.  
  **Ejemplos**: `RandomForestClassifier`, `GradientBoostingRegressor`, `AdaBoost`.

- `sklearn.svm`: Máquinas de vectores de soporte (SVM).  
  **Ejemplos**: `SVC`, `SVR`.

- `sklearn.neighbors`: Algoritmos basados en vecinos.  
  **Ejemplos**: `KNeighborsClassifier`, `KNeighborsRegressor`.

- `sklearn.naive_bayes`: Modelos bayesianos
  **Ejemplos:** `GaussianNB, MultinomialNB`

- `sklearn.neural_network`: Redes neuronales básicas 
  **Ejemplos:** `MLPClassifier, MLPRegressor`

## 4. Modelos no supervisados

- `sklearn.cluster`: Algoritmos de clustering.  
  **Ejemplos**: `KMeans`, `DBSCAN`, `AgglomerativeClustering`.

- `sklearn.decomposition`: Reducción de dimensionalidad.  
  **Ejemplos**: `PCA`, `TruncatedSVD`, `NMF`.

- `sklearn.mixture:` Modelos de mezclas Gaussianas 
  **Ejemplo:** `GaussianMixture`.

- `sklearn.covariance:` Detección de anomalías 
  **Ejemplo:** `EllipticEnvelope`.



## 5. Evaluación de modelos

- `sklearn.metrics`: Métricas de evaluación.  
  **Ejemplos**: `accuracy_score`, `precision_score`, `confusion_matrix`, `roc_auc_score`.

- `sklearn.model_selection`: Validación y ajuste de hiperparámetros.  
  **Ejemplos**: `train_test_split`, `cross_val_score`, `GridSearchCV`.

## 6. Utilidades generales

- `sklearn.pipeline`: Creación de flujos de procesamiento.  
  **Ejemplo**: `Pipeline` para encadenar transformadores y estimadores., `ColumnTransformer`

- `sklearn.utils`: Funciones auxiliares.  
  **Ejemplo**: `shuffle` (mezcla de datos), `resample`

- `datasets`: Datasets de prueba
  **Ejemplo:** `load_iris`, `make_classification`

## 7. Módulos Especializados (menos conocidos)

-  `sklearn.cross_decomposition`: Modelos para datos multivariados 
  **Ejemplo:** `PLSCanonical`.

-  `sklearn.isotonic`: Regresión isotónica 
  **Ejemplo:** `IsotonicRegression`.

-  `sklearn.kernel_approximation`: Aproximación de kernels 
  **Ejemplo:** `Nystroem`, `RBFSampler`.

-  `sklearn.manifold`: Reducción de dimensionalidad no lineal 
  **Ejemplos:** `TSNE`, `MDS`.

-  `sklearn.multiclass`: Clasificación multiclase 
  **Ejemplo:** `OneVsRestClassifier`.

-  `sklearn.multioutput`: Modelos para múltiples salidas 
  **Ejemplo:** `MultiOutputRegressor`.

***

## 🔍 ¿Cómo verificar todos los módulos disponibles?

Puedes listar todos los submódulos de `scikit-learn` en Python con:

```python
import sklearn
help(sklearn)  # Muestra la documentación con todos los módulos
```
***
## 🌟 Ejemplo práctico usando varios módulos

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline

# Cargar datos
data = load_iris()
X, y = data.data, data.target

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Crear un pipeline con escalado y modelo
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(n_estimators=100))
])

# Entrenar y predecir
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

# Evaluar
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
```
## Salida:

```Accuracy: 0.96```
