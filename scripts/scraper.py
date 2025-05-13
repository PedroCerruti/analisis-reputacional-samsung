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
    """Obtiene la URL API usando solo async"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS)
        page = await browser.new_page()
        
        try:
            await page.goto(product_url, timeout=TIMEOUT)
            await page.click('a:has-text("opiniones")', timeout=10000)
            
            # Esperar la redirección a la URL API
            async with page.expect_response(lambda r: "/catalog/reviews/" in r.url) as response_info:
                await page.wait_for_url(lambda url: "/catalog/reviews/" in url, timeout=10000)
            
            return page.url
        except Exception as e:
            print(f"❌ Error obteniendo API URL: {str(e)}")
            return None
        finally:
            await browser.close()

async def scrapear_comentarios(product_name, api_url):
    """Scrapea comentarios usando la URL API"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS)
        context = await browser.new_context(
            viewport={'width': 1366, 'height': 768},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        page = await context.new_page()
        
        try:
            await page.goto(api_url, timeout=TIMEOUT)
            print(f"\n🔍 Iniciando scrapeo de {product_name}...")

            # Esperar comentarios
            try:
                await page.wait_for_selector('article[data-testid="comment-component"]', timeout=10000)
            except:
                print(f"⚠️ No se encontraron comentarios para {product_name}")
                return None

            all_comments = []
            for stars, rating_id in zip([5, 4, 3, 2, 1], range(1, 6)):
                print(f"   ⭐ Procesando {stars} estrellas...")
                try:
                    await page.click('span:has-text("Calificación")')
                    await asyncio.sleep(1)
                    await page.click(f'[data-testid="filterItem-rating-{rating_id}"]')
                    await page.wait_for_selector('article[data-testid="comment-component"]', timeout=10000)
                    
                    await cargar_mas_comentarios(page)
                    comments = await extraer_datos_comentarios(page, rating=stars)
                    all_comments.extend(comments)
                    print(f"      → {len(comments)} comentarios")
                    
                except Exception as e:
                    print(f"      ⚠️ Error con {stars} estrellas: {str(e)}")
                    continue

            # Guardar JSON
            filename = DATA_RAW / f"comentarios_{product_name}.json"  # Path completo
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(all_comments, f, ensure_ascii=False, indent=2)
    
            print(f"💾 Datos guardados en: {filename}")
            return filename
            
        finally:
            await browser.close()

async def cargar_mas_comentarios(page, max_attempts=10):
    """Carga más comentarios con scroll"""
    attempts = 0
    last_count = 0
    
    while attempts < max_attempts:
        await page.mouse.wheel(0, 500)
        await asyncio.sleep(1)
        
        current_count = len(await page.query_selector_all('article[data-testid="comment-component"]'))
        if current_count == last_count:
            attempts += 1
            load_more = await page.query_selector('button:has-text("Ver más comentarios")')
            if load_more:
                await load_more.click()
                await asyncio.sleep(2)
        else:
            attempts = 0
            last_count = current_count

async def extraer_datos_comentarios(page, rating):
    """Extrae datos estructurados de comentarios, asignando calificación desde el filtro"""
    comments = []
    elements = await page.query_selector_all('article[data-testid="comment-component"]')
    
    for element in elements:
        try:
            text = await (await element.query_selector('[data-testid="comment-content-component"]')).inner_text()
            date = await (await element.query_selector('.ui-review-capability-comments__comment__date')).inner_text()
            
            try:
                date = datetime.strptime(date, "%d %b. %Y").strftime("%Y-%m-%d")
            except:
                pass
            
            useful_text = await (await element.query_selector('button[data-testid="like-button"]')).inner_text()
            useful_votes = int(re.search(r"\d+", useful_text).group() or 0)
            
            comments.append({
                "text": text.strip(),
                "rating": rating,
                "date": date,
                "useful_votes": useful_votes
            })
        except:
            continue
            
    return comments


async def main():
    """Función principal"""
    for product_name, product_url in PRODUCTOS.items():
        print(f"\n🔄 Procesando {product_name}...")
        api_url = await obtener_url_api(product_url)
        if api_url:
            await scrapear_comentarios(product_name, api_url)

if __name__ == "__main__":
    asyncio.run(main())