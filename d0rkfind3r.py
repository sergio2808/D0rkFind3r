import os
import requests

# Set up your Google Custom Search API credentials
API_KEY = '' # Write your google API key
CX = ''  # Replace with your custom search engine ID

# Colores ANSI
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
BOLD = "\033[1m"

# Function to read the file line by line and replace 'target.com' with the user's URL
def leer_y_reemplazar_contenido_txt(nombre_archivo, url_usuario):
    if not os.path.exists(nombre_archivo):
        print(f"{RED}The file {nombre_archivo} does not exist.{RESET}")
        return None

    # Read all the file lines
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    
    # Replace 'target.com' with the provided URL in each line
    lineas_reemplazadas = [linea.replace("target.com", url_usuario).strip() for linea in lineas]
    return lineas_reemplazadas

# Function to search on Google using the Google Custom Search API
def buscar_en_google(consulta):
    # Construimos la URL para realizar la solicitud
    url = f"https://www.googleapis.com/customsearch/v1?q={consulta}&key={API_KEY}&cx={CX}"
    
    # An HTTP GET request is made to the Google Custom Search API
    response = requests.get(url)
    
    # Check if the request is successful
    if response.status_code == 200:
        resultados = response.json()
        if "items" in resultados:
            # If there are any results, they will be displayed
            return resultados["items"]
        else:
            # If not
            return []
    else:
        print(f"{RED}Error in the request: {response.status_code}{RESET}")
        return []

# Main function
def main():
    nombre_archivo = input(f"{CYAN}Write the file name .txt (add the path if necesarry): {RESET}")
    
    # Ask the user to provide the URL
    url_usuario = input(f"{CYAN}Enter a URL that will replace 'target.com': {RESET}").strip()

    # Read all the lines of the file and replace 'target.com' with the provided URL
    lineas_reemplazadas = leer_y_reemplazar_contenido_txt(nombre_archivo, url_usuario)
    if lineas_reemplazadas is None:
        return

    # Perform the search on Google for each line
    for idx, consulta in enumerate(lineas_reemplazadas, start=1):
        print(f"\n{YELLOW}Searching... {idx}: '{consulta}'{RESET}")
        resultados = buscar_en_google(consulta)

        if resultados:
            print(f"\n{GREEN}There are the results of the last search: {idx}:{RESET}")
            for i, item in enumerate(resultados, start=1):
                print(f"{BOLD}{BLUE}{i}. {item['title']} - {item['link']}{RESET}")
        else:
            print(f"{RED}The search has not any result {idx}.{RESET}")

# Executing the script
if __name__ == "__main__":
    main()

