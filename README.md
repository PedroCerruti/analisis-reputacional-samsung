# 📊 Análisis Reputacional de Smartphones - Caso de Estudio Metodológico

## 🎯 Descripción del Proyecto

**Caso de estudio metodológico** que demuestra técnicas de triangulación entre análisis exploratorio de datos (EDA) y procesamiento de lenguaje natural (NLP) aplicadas al análisis reputacional en datasets pequeños. Diseñado como proof-of-concept para extraer insights válidos de datos limitados (1 crisis documentada, 9 períodos temporales).

### Contexto del Estudio

El proyecto analiza reseñas de usuarios del **Samsung Galaxy A15** y **Motorola Moto G32** en MercadoLibre Argentina, explorando cómo las diferencias en percepción se manifiestan en el discurso de usuarios más allá de métricas cuantitativas simples.

### Limitaciones por Diseño

- **Muestra específica**: 1,085 reseñas de 2 productos (Samsung A15, Motorola G32)
- **Una crisis documentada**: Samsung A15 cargador (jul-nov 2024)
- **Contexto específico**: Argentina, smartphones gama media, MercadoLibre
- **Objetivo**: Demostración técnica, no sistema productivo

## 📁 Estructura del Proyecto

```
proyecto_ml/
├── data/
│   ├── raw/                    # Datos originales del scraping
│   │   ├── Samsung_A15.json
│   │   └── Motorola_G32.json
│   └── processed/              # Datos procesados y limpios
│       ├── reviews_unificado.csv
│       └── reviews_text_clean.csv
├── notebooks/
│   ├── 0_Preprocesamiento.ipynb      # Limpieza y unificación de datos
│   ├── 1_EDA.ipynb                   # Análisis exploratorio de datos
│   ├── 2_NLP.ipynb                   # Procesamiento de lenguaje natural
│   └── 3_Analisis_integrador.ipynb   # Triangulación metodológica
├── src/
│   └── scraper.py              # Script de scraping automatizado

└── README.md
```

## 🛠️ Tecnologías Utilizadas

### Web Scraping
- **Playwright**: Automatización de navegador para extracción de reseñas
- **AsyncIO**: Procesamiento asíncrono para optimizar rendimiento

### Análisis de Datos
- **Pandas**: Manipulación y análisis de datos estructurados
- **NumPy**: Operaciones numéricas y estadísticas
- **Matplotlib/Seaborn**: Visualización de datos y tendencias

### Procesamiento de Lenguaje Natural
- **NLTK**: Tokenización y limpieza de texto
- **TextBlob/VADER**: Análisis de sentimientos
- **Scikit-learn**: Clustering semántico (TF-IDF, K-Means)
- **Unidecode**: Normalización de texto en español argentino

## 📈 Metodología de Triangulación

### 1. Análisis Exploratorio de Datos (EDA)
- **Detección de anomalías temporales** en ratings y volumen
- **Análisis de distribuciones** y patrones estacionales
- **Identificación de períodos críticos** mediante métricas cuantitativas

### 2. Procesamiento de Lenguaje Natural (NLP)
- **Clustering semántico** para agrupamiento automático de contenido
- **Análisis de sentimientos** VADER para polaridad emocional
- **Extracción de atributos** valorados por usuarios
- **Modelado de tópicos** para estructura temática del discurso

### 3. Validación Cruzada
- **Convergencia metodológica** entre técnicas independientes
- **Análisis de coincidencias** temporales entre EDA y NLP
- **Triangulación de hallazgos** para robustez interpretativa

## 🎯 Principales Hallazgos

### Crisis Documentada: Samsung A15 Cargador
- **Detección EDA**: Caída de rating promedio de 4.18 → 2.7 (jul-nov 2024)
- **Diagnóstico NLP**: 99.1% de menciones relacionadas con "cargador" en cluster crítico
- **Timing**: Identificación automática de causa 9 semanas antes del pico de crisis
- **Impacto**: 1,088 votos útiles concentrados en reseñas sobre problemática del cargador

### Diferenciación Competitiva
- **Motorola G32**: Ventaja consistente en relación precio-calidad y estabilidad
- **Samsung A15**: Mayor innovación percibida pero vulnerabilidad en accesorios
- **Vocabulario diferencial**: "precio/calidad/recomiendo" vs "cargador/problema/malo"

### Validación Metodológica
- **Convergencia EDA-NLP**: 70%+ coincidencia en identificación de períodos anómalos
- **Especificidad diagnóstica**: Identificación automática de causa dominante (>80% menciones)
- **Robustez temporal**: Framework detecta evolución de crisis 2-3 períodos antes del pico

## 🚀 Instalación y Uso

### Requisitos
```bash
pip install pandas numpy matplotlib seaborn
pip install nltk textblob vaderSentiment scikit-learn
pip install playwright unidecode dateparser
pip install jupyter notebook
```

### Configuración de Playwright
```bash
playwright install
```

### Ejecución del Scraping
```bash
python src/scraper.py
```

### Análisis Completo
1. **Preprocesamiento**: `notebooks/0_Preprocesamiento.ipynb`
2. **EDA**: `notebooks/1_EDA.ipynb`  
3. **NLP**: `notebooks/2_NLP.ipynb`
4. **Integración**: `notebooks/3_Analisis_integrador.ipynb`

## 📊 Métricas del Proyecto

- **Triangulación**: 3 métodos independientes
- **Dataset**: 1,085 reseñas válidas
- **Período**: dic 2022 - abr 2025
- **Crisis documentada**: 1 caso (Samsung A15 cargador)
- **Convergencia metodológica**: >70% coincidencia
- **Precisión diagnóstica**: 99.1% identificación de causa específica

## 📝 Valor Metodológico

### Lo que este análisis PUEDE demostrar:
✅ **Metodología de triangulación** entre EDA y NLP  
✅ **Identificación post-hoc** de causas específicas en casos documentados  
✅ **Principios replicables** para análisis similares  
✅ **Convergencia metodológica** como técnica de validación en datasets pequeños  

### Lo que este análisis NO pretende:
❌ Capacidades predictivas generalizables  
❌ Robustez estadística para detección automática universal  
❌ Validación en múltiples tipos de crisis o contextos  
❌ Sistema productivo de monitoreo automático  

## 🎓 Aplicabilidad y Extensiones

### Contextos Aplicables
- **E-commerce**: Análisis de reseñas de productos con datos limitados
- **Brand monitoring**: Detección de problemas específicos en feedback de usuarios  
- **Competitive intelligence**: Diferenciación semántica entre marcas competidoras
- **Product management**: Priorización de mejoras basada en análisis automatizado

### Futuras Extensiones
- **Expansión temporal**: Análisis de múltiples crisis para validación robusta
- **Diversificación geográfica**: Aplicación a otros mercados hispanohablantes
- **Escalabilidad técnica**: Implementación de pipelines automatizados
- **Integración multimodal**: Incorporación de imágenes y metadata adicional

## 👥 Contribuciones

Este proyecto establece precedente metodológico para análisis reputacional en contextos de recursos limitados, priorizando transparencia sobre claims exagerados y demonstrando valor práctico mediante rigor técnico apropiado al scope de datos disponibles.

## 📄 Documentación Adicional

- **Informe no-técnico**: [Caso de Estudio: Análisis Reputacional Samsung vs Motorola](enlace-pendiente) *(próximamente)*
- **Notebooks comentados**: Documentación inline detallada en cada notebook
- **Análisis metodológico**: Contenido técnico distribuido en los notebooks del proyecto

## 📧 Contacto

**Pedro Cerruti**  
📧 Email: [tu-email@ejemplo.com](mailto:tu-email@ejemplo.com)  
💼 LinkedIn: [linkedin.com/in/tu-perfil](https://linkedin.com/in/tu-perfil)  

Para consultas sobre metodología, replicación o adaptación a otros contextos, no dudes en contactarme.

---

**Nota metodológica**: Este proyecto reconoce explícitamente sus limitaciones inherentes mientras extrae valor máximo para demostración técnica y desarrollo de principios replicables en análisis reputacional con datos limitados.