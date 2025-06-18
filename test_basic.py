#!/usr/bin/env python3
"""
Script básico de verificación para el proyecto de análisis de reseñas.
Verifica estructura de carpetas, imports y funcionalidad básica.
"""

import os
import sys
from pathlib import Path

def test_project_structure():
    """Verifica que la estructura de carpetas sea correcta"""
    print("🔍 Verificando estructura del proyecto...")
    
    required_dirs = [
        'notebooks',
        'data/raw', 
        'data/processed',
        'outputs/visualizations',
        'outputs/analysis_results', 
        'outputs/exports',
        'outputs/dashboards',
        'src'
    ]
    
    missing_dirs = []
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            missing_dirs.append(dir_path)
        else:
            print(f"  ✅ {dir_path}")
    
    if missing_dirs:
        print(f"  ❌ Faltan carpetas: {missing_dirs}")
        return False
    
    print("✅ Estructura de carpetas correcta")
    return True

def test_basic_imports():
    """Verifica que los imports principales funcionen"""
    print("\n🔍 Verificando imports principales...")
    
    try:
        import pandas as pd
        print("  ✅ pandas")
        
        import numpy as np
        print("  ✅ numpy")
        
        import matplotlib.pyplot as plt
        print("  ✅ matplotlib")
        
        import seaborn as sns
        print("  ✅ seaborn")
        
        from textblob import TextBlob
        print("  ✅ textblob")
        
        print("✅ Todos los imports principales funcionan")
        return True
        
    except ImportError as e:
        print(f"  ❌ Error de import: {e}")
        return False

def test_files_exist():
    """Verifica que archivos clave existan"""
    print("\n🔍 Verificando archivos clave...")
    
    required_files = [
        'requirements.txt',
        '.gitignore', 
        'README.md',
        'notebooks/0_Preprocesamiento.ipynb',
        'notebooks/1_EDA.ipynb',
        'notebooks/2_NLP.ipynb',
        'notebooks/3_Analisis_integrador.ipynb'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
        else:
            print(f"  ✅ {file_path}")
    
    if missing_files:
        print(f"  ❌ Faltan archivos: {missing_files}")
        return False
    
    print("✅ Todos los archivos clave existen")
    return True

def main():
    """Ejecuta todas las verificaciones"""
    print("🚀 INICIANDO VERIFICACIÓN BÁSICA DEL PROYECTO")
    print("=" * 50)
    
    tests = [
        test_project_structure,
        test_basic_imports, 
        test_files_exist
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 50)
    if all(results):
        print("🎉 ¡TODAS LAS VERIFICACIONES PASARON!")
        print("✅ El proyecto está listo para ser usado")
        return 0
    else:
        print("❌ Algunas verificaciones fallaron")
        print("🔧 Revisa los errores arriba y corrígelos")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)