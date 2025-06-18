import asyncio
import json
import re
from datetime import datetime
from playwright.async_api import async_playwright
import os
from pathlib import Path

# Configuración de paths (al inicio del script)
BASE_DIR = Path(__file__).parent.parent  # Raíz del proyecto (/proyecto_ml/)
DATA_RAW = BASE_DIR / "data" / "raw"
DATA_RAW.mkdir(parents=True, exist_ok=True)  # Crea la carpeta si no existe

# Configuración
HEADLESS = False
TIMEOUT = 60000
PRODUCTOS = {
    "Motorola_G32": "https://www.mercadolibre.com.ar/motorola-moto-g32-128-gb-gris-6-gb-ram/p/MLA26924818",
    "Samsung_A15": "https://www.mercadolibre.com.ar/samsung-galaxy-a15-128-gb-negro-azulado-4-gb-ram/p/MLA32427104"
}

async def obtener_url_api(product_url):
    """Obtiene la URL API usando solo async - FUNCIONALIDAD PRESERVADA"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS)
        page = await browser.new_page()
        
        try:
            print(f"📍 Navegando a: {product_url}")
            await page.goto(product_url, timeout=TIMEOUT)
            
            # MEJORA: Verificar que la página cargó correctamente
            await page.wait_for_load_state('networkidle', timeout=30000)
            
            print("🔍 Buscando enlace de opiniones...")
            await page.click('a:has-text("opiniones")', timeout=10000)
            
            # Esperar la redirección a la URL API - LÓGICA ORIGINAL PRESERVADA
            print("⏳ Esperando redirección a API...")
            async with page.expect_response(lambda r: "/catalog/reviews/" in r.url) as response_info:
                await page.wait_for_url(lambda url: "/catalog/reviews/" in url, timeout=10000)
            
            api_url = page.url
            print(f"✅ API URL obtenida: {api_url[:50]}...")
            return api_url
            
        except Exception as e:
            print(f"❌ Error obteniendo API URL: {str(e)}")
            return None
        finally:
            await browser.close()

async def scrapear_comentarios(product_name, api_url):
    """Scrapea comentarios usando la URL API - FUNCIONALIDAD CORE PRESERVADA"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS)
        context = await browser.new_context(
            viewport={'width': 1366, 'height': 768},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        page = await context.new_page()
        
        try:
            print(f"\n🔍 Iniciando scrapeo de {product_name}...")
            await page.goto(api_url, timeout=TIMEOUT)

            # Esperar comentarios - LÓGICA ORIGINAL
            try:
                await page.wait_for_selector('article[data-testid="comment-component"]', timeout=10000)
                print("✅ Comentarios encontrados")
            except:
                print(f"⚠️ No se encontraron comentarios para {product_name}")
                return None

            all_comments = []
            
            # BUCLE PRINCIPAL PRESERVADO - Solo mejorado el logging
            for stars, rating_id in zip([5, 4, 3, 2, 1], range(1, 6)):
                print(f"   ⭐ Procesando {stars} estrellas...")
                try:
                    # Aplicar filtro de estrellas - LÓGICA ORIGINAL
                    await page.click('span:has-text("Calificación")')
                    await asyncio.sleep(1)
                    await page.click(f'[data-testid="filterItem-rating-{rating_id}"]')
                    await page.wait_for_selector('article[data-testid="comment-component"]', timeout=10000)
                    
                    # Cargar más comentarios - FUNCIÓN ORIGINAL
                    await cargar_mas_comentarios(page)
                    
                    # Extraer datos - FUNCIÓN ORIGINAL
                    comments = await extraer_datos_comentarios(page, rating=stars)
                    all_comments.extend(comments)
                    print(f"      → {len(comments)} comentarios extraídos")
                    
                except Exception as e:
                    print(f"      ⚠️ Error con {stars} estrellas: {str(e)}")
                    continue

            # MEJORA: Validar que se extrajeron datos antes de guardar
            if not all_comments:
                print(f"⚠️ No se extrajeron comentarios para {product_name}")
                return None

            # Guardar JSON - FORMATO ORIGINAL PRESERVADO
            filename = DATA_RAW / f"comentarios_{product_name}.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(all_comments, f, ensure_ascii=False, indent=2)
    
            print(f"💾 Datos guardados en: {filename}")
            print(f"📊 Total comentarios: {len(all_comments)}")
            return filename
            
        except Exception as e:
            print(f"❌ Error general en scrapeo: {str(e)}")
            return None
        finally:
            await browser.close()

async def cargar_mas_comentarios(page, max_attempts=10):
    """Carga más comentarios con scroll - FUNCIONALIDAD PRESERVADA"""
    attempts = 0
    last_count = 0
    
    while attempts < max_attempts:
        # Scroll - MÉTODO ORIGINAL
        await page.mouse.wheel(0, 500)
        await asyncio.sleep(1)
        
        current_count = len(await page.query_selector_all('article[data-testid="comment-component"]'))
        
        if current_count == last_count:
            attempts += 1
            # Buscar botón "Ver más" - LÓGICA ORIGINAL
            load_more = await page.query_selector('button:has-text("Ver más comentarios")')
            if load_more:
                try:
                    await load_more.click()
                    await asyncio.sleep(2)
                    print(f"      🔄 Botón 'Ver más' clickeado (intento {attempts})")
                except:
                    print(f"      ⚠️ No se pudo clickear 'Ver más' (intento {attempts})")
        else:
            attempts = 0
            last_count = current_count

async def extraer_datos_comentarios(page, rating):
    """Extrae datos estructurados - ESTRUCTURA ORIGINAL PRESERVADA"""
    comments = []
    elements = await page.query_selector_all('article[data-testid="comment-component"]')
    
    print(f"      🔎 Procesando {len(elements)} elementos...")
    
    for i, element in enumerate(elements):
        try:
            # Extraer texto - SELECTOR ORIGINAL
            text_element = await element.query_selector('[data-testid="comment-content-component"]')
            if not text_element:
                continue
            text = await text_element.inner_text()
            
            # Extraer fecha - LÓGICA ORIGINAL
            date_element = await element.query_selector('.ui-review-capability-comments__comment__date')
            if date_element:
                date = await date_element.inner_text()
                try:
                    date = datetime.strptime(date, "%d %b. %Y").strftime("%Y-%m-%d")
                except:
                    pass  # Mantener formato original si falla
            else:
                date = "N/A"
            
            # Extraer votos útiles - LÓGICA ORIGINAL
            useful_element = await element.query_selector('button[data-testid="like-button"]')
            useful_votes = 0
            if useful_element:
                useful_text = await useful_element.inner_text()
                useful_match = re.search(r"\d+", useful_text)
                useful_votes = int(useful_match.group()) if useful_match else 0
            
            # ESTRUCTURA JSON ORIGINAL PRESERVADA
            comments.append({
                "text": text.strip(),
                "rating": rating,  # Asignado desde filtro
                "date": date,
                "useful_votes": useful_votes
            })
            
        except Exception as e:
            print(f"        ⚠️ Error procesando elemento {i}: {str(e)}")
            continue
            
    return comments

async def main():
    """Función principal - FLUJO ORIGINAL PRESERVADO"""
    print("🚀 Iniciando scraper de MercadoLibre...")
    print(f"📁 Directorio de salida: {DATA_RAW}")
    
    for product_name, product_url in PRODUCTOS.items():
        print(f"\n{'='*50}")
        print(f"🔄 Procesando {product_name}...")
        print(f"{'='*50}")
        
        # Obtener URL API - PASO 1 ORIGINAL
        api_url = await obtener_url_api(product_url)
        
        if api_url:
            # Scrapear comentarios - PASO 2 ORIGINAL
            result = await scrapear_comentarios(product_name, api_url)
            if result:
                print(f"✅ {product_name} completado exitosamente")
            else:
                print(f"❌ {product_name} falló en la extracción")
        else:
            print(f"❌ {product_name} falló en obtener API URL")
    
    print(f"\n🎉 Scraping completado. Archivos en: {DATA_RAW}")

if __name__ == "__main__":
    asyncio.run(main())