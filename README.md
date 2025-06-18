# 📱 Análisis Comparativo de Reseñas: Motorola G32 vs Samsung A15

## 🎯 Descripción del Proyecto

Este proyecto implementa un **framework integral de análisis de reseñas** que combina técnicas de scraping web, análisis exploratorio de datos (EDA) y procesamiento de lenguaje natural (NLP) para evaluar la percepción de usuarios sobre smartphones de gama media.

### **Características principales:**
- 🔍 **Scraping automatizado** de reseñas de MercadoLibre Argentina
- 📊 **Análisis exploratorio avanzado** con visualizaciones interactivas
- 🧠 **Procesamiento de lenguaje natural** con análisis de sentimientos
- 🚨 **Framework de detección de crisis** reputacionales automatizado
- 📈 **Dashboard integrado** para monitoreo continuo

---

## 📋 Tabla de Contenidos

- [🚀 Inicio Rápido](#-inicio-rápido)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [🔧 Instalación](#-instalación)
- [📊 Notebooks y Análisis](#-notebooks-y-análisis)
- [📈 Resultados Principales](#-resultados-principales)
- [🛠️ Tecnologías Utilizadas](#️-tecnologías-utilizadas)
- [📖 Metodología](#-metodología)
- [🤝 Contribución](#-contribución)

---

## 🚀 Inicio Rápido

### **Prerrequisitos**
- Python 3.8+
- Navegador Chromium/Chrome instalado (para Playwright)

### **Instalación rápida**
```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/analisis-resenas-smartphones.git
cd analisis-resenas-smartphones

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar Playwright
playwright install chromium
```

### **Ejecución básica**
```bash
# 1. Ejecutar scraper (opcional - datos ya incluidos)
python src/scraper.py

# 2. Abrir notebooks en orden
jupyter notebook notebooks/0_Preprocesamiento.ipynb
```

---

## 📁 Estructura del Proyecto

```
📦 analisis-resenas-smartphones/
├── 📁 src/
│   └── scraper.py                 # Web scraper para MercadoLibre
├── 📁 notebooks/
│   ├── 0_Preprocesamiento.ipynb   # Limpieza y normalización
│   ├── 1_EDA.ipynb               # Análisis exploratorio
│   ├── 2_NLP.ipynb               # Procesamiento de lenguaje natural
│   └── 3_Analisis_integrador.ipynb # Framework de crisis
├── 📁 data/
│   ├── 📁 raw/                   # Datos crudos (JSON)
│   └── 📁 processed/             # Datos procesados (CSV)
├── 📁 docs/
│   └── informe_final.pdf         # Informe técnico completo
├── requirements.txt              # Dependencias del proyecto
├── .gitignore                   # Archivos excluidos de Git
└── README.md                    # Este archivo
```

---

## 🔧 Instalación

### **1. Dependencias del sistema**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3-pip chromium-browser

# macOS (con Homebrew)
brew install python3
brew install chromium

# Windows
# Descargar Python desde python.org
# Instalar Chrome/Edge desde sus sitios oficiales
```

### **2. Configuración del proyecto**
```bash
# Clonar y navegar
git clone https://github.com/tu-usuario/analisis-resenas-smartphones.git
cd analisis-resenas-smartphones

# Entorno virtual
python -m venv venv
source venv/bin/activate

# Instalación de paquetes
pip install --upgrade pip
pip install -r requirements.txt

# Configuración específica de Playwright
playwright install
```

### **3. Configuración opcional de NLTK**
```python
# Ejecutar en Python/Jupyter
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
```

---

## 📊 Notebooks y Análisis

### **🧼 0. Preprocesamiento** (`0_Preprocesamiento.ipynb`)
- **Objetivo:** Limpieza y normalización de datos crudos
- **Procesos:** Carga de JSON, normalización de texto, conversión de fechas
- **Output:** `reviews_unificado.csv`

### **📈 1. Análisis Exploratorio** (`1_EDA.ipynb`)
- **Objetivo:** Comprensión inicial de patrones en los datos
- **Análisis:** Distribución temporal, ratings, longitud de reseñas, engagement
- **Outputs:** 8+ visualizaciones, estadísticas descriptivas

### **🧠 2. Procesamiento NLP** (`2_NLP.ipynb`)
- **Objetivo:** Extracción de insights semánticos
- **Técnicas:** Análisis léxico, sentimientos, clustering, modelado de tópicos
- **Outputs:** Análisis comparativo TextBlob vs VADER, clustering semántico

### **🚨 3. Framework Integrador** (`3_Analisis_integrador.ipynb`)
- **Objetivo:** Detección automatizada de crisis reputacionales
- **Innovación:** Sistema multi-indicador que combina métricas cuantitativas y semánticas
- **Outputs:** Dashboard de monitoreo, reseñas representativas, validación cruzada

---

## 📈 Resultados Principales

### **🔍 Hallazgos Clave**

#### **Crisis Reputacional Samsung A15 Detectada**
- **Período:** Julio 2024 - Marzo 2025
- **Causa principal:** Ausencia del cargador completo en packaging
- **Impact:** 99.1% de menciones problemáticas, engagement 9.5 vs 2.8 promedio

#### **Posicionamiento Competitivo**
- **Motorola G32:** Rating superior (3.95 vs 3.51), mayor proporción de reseñas positivas (68.7% vs 52.3%)
- **Samsung A15:** Mayor controversia (engagement 5.1 vs 2.8), concentración en problemas de experiencia

#### **Validación Metodológica**
- **Precisión del framework:** >99% en detección automática de crisis
- **Alerta temprana:** Detección 1-2 meses antes que métodos tradicionales
- **Convergencia técnica:** Concordancia >85% entre EDA y análisis semántico

### **📊 Métricas del Dataset**
- **Total reseñas analizadas:** 1,085
- **Período temporal:** 2022-2025
- **Productos:** Motorola G32, Samsung A15
- **Fuente:** MercadoLibre Argentina

---

## 🛠️ Tecnologías Utilizadas

### **Scraping y Automatización**
- ![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=playwright&logoColor=white) **Playwright** - Web scraping dinámico
- ![AsyncIO](https://img.shields.io/badge/AsyncIO-3776AB?style=flat&logo=python&logoColor=white) **AsyncIO** - Programación asíncrona

### **Análisis de Datos**
- ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) **Pandas** - Manipulación de datos
- ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) **NumPy** - Computación numérica
- ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white) **Scikit-learn** - Machine learning

### **Visualización**
- ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat&logo=matplotlib&logoColor=white) **Matplotlib** - Gráficos base
- ![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat&logo=python&logoColor=white) **Seaborn** - Visualizaciones estadísticas

### **Procesamiento de Lenguaje Natural**
- ![NLTK](https://img.shields.io/badge/NLTK-3776AB?style=flat&logo=python&logoColor=white) **NLTK** - Toolkit de NLP
- ![TextBlob](https://img.shields.io/badge/TextBlob-3776AB?style=flat&logo=python&logoColor=white) **TextBlob** - Análisis de sentimientos
- **VADER** - Análisis de sentimientos especializado
- **WordCloud** - Generación de nubes de palabras

---

## 📖 Metodología

### **🔬 Enfoque Científico**
1. **Recolección automatizada** de datos mediante scraping ético
2. **Análisis exploratorio** para identificación de patrones iniciales
3. **Procesamiento semántico** con múltiples técnicas de NLP
4. **Validación cruzada** entre métodos independientes
5. **Framework integrador** que combina hallazgos cuantitativos y cualitativos

### **🎯 Innovaciones Metodológicas**
- **Sistema multi-indicador** para detección de crisis reputacionales
- **Validación temporal** de patrones evolutivos
- **Análisis semántico diferencial** por período y producto
- **Framework replicable** para monitoreo continuo

### **📏 Métricas de Calidad**
- **Precisión de detección:** >99%
- **Concordancia entre métodos:** >85%
- **Cobertura temporal:** 3+ años de datos
- **Robustez metodológica:** Triangulación de 4+ técnicas independientes

---

## 🤝 Contribución

### **📋 Cómo Contribuir**
1. **Fork** el repositorio
2. **Crear una rama** para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abrir un Pull Request**

### **🔍 Áreas de Mejora**
- Expansión a otros productos/categorías
- Implementación de alertas en tiempo real
- Integración con APIs de redes sociales
- Desarrollo de interfaz web interactiva
- Optimización de performance del scraper

### **📝 Reportar Issues**
Si encuentras bugs o tienes sugerencias, por favor:
1. Revisa si el issue ya existe
2. Crea un issue detallado con:
   - Descripción del problema
   - Pasos para reproducir
   - Entorno (SO, versión de Python, etc.)
   - Screenshots si es aplicable

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

---

## 👥 Autores

- **Pedro Cerruti** - *Análisis y desarrollo* - [@tu-usuario](https://github.com/tu-usuario)

---

## 📊 Estadísticas del Proyecto

![GitHub last commit](https://img.shields.io/github/last-commit/tu-usuario/analisis-resenas-smartphones)
![GitHub repo size](https://img.shields.io/github/repo-size/tu-usuario/analisis-resenas-smartphones)
![GitHub language count](https://img.shields.io/github/languages/count/tu-usuario/analisis-resenas-smartphones)
![GitHub top language](https://img.shields.io/github/languages/top/tu-usuario/analisis-resenas-smartphones)

---

⭐ **Si este proyecto te resulta útil, considera darle una estrella en GitHub**