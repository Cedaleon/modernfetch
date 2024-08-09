#!/usr/bin/env python3

import platform
import psutil
import json
import datetime
import subprocess
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
import time
import shutil

# Crear un objeto Console de rich
console = Console()

# Colores y estilos
STYLE_ICON = "bold green"
STYLE_VALUE = "bold white"
STYLE_HEADER = "bold bright_cyan"
STYLE_TIME = "bold magenta"
STYLE_ERROR = "bold red"
STYLE_PANEL = "on grey15"  # Fondo gris oscuro
STYLE_PANEL_TITLE = "bold bright_green"  # Título del panel en verde brillante
STYLE_JSON = "bold yellow"

# Definir estilo para el borde con degradado
STYLE_PANEL_BORDER_GRADIENT = "on black #00fff7"  # Degradado azul a verde

def get_cpu_info():
    try:
        output = subprocess.check_output(['lscpu'], text=True)
        cpu_info = {}
        for line in output.splitlines():
            if ':' in line:
                key, value = line.split(':', 1)
                cpu_info[key.strip()] = value.strip()
        return cpu_info.get('Model name', 'Desconocido')
    except Exception as e:
        return f"Error al obtener información del CPU: {e}"

def get_system_info():
    info = {
        "      💻  OS": platform.system(),
        "      🏠  Distribución": platform.node(),
        "      🔧  V. Kernel": platform.release(),
        "      🔩  V. Sistema": platform.version().split(" ")[0],  # Ajusta el formato
        "      🖥  Máquina": platform.machine(),
        "      🧠  Procesador": get_cpu_info(),
        "      🔢  Núcleos PU": str(psutil.cpu_count(logical=False)),
        "      🧵  Hilos CPU": str(psutil.cpu_count(logical=True)),
        "      💾  RAM": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "      💽  Disco": f"{round(psutil.disk_usage('/').total / (1024 ** 3), 2)} GB",
        "      🕒  Hora Actual": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "      🕒  Uptime": str(datetime.timedelta(seconds=int(time.time() - psutil.boot_time()))),
        "      🐍  Python Version": platform.python_version()
    }
    return info

def print_info(info, output_format):
    if output_format == "json":
        json_output = json.dumps(info, indent=4, ensure_ascii=False)
        console.print(json_output, style=STYLE_JSON)
    elif output_format == "table":
        # Crear tabla
        table = Table(border_style="bright_blue", title_style=STYLE_HEADER, box=None)

        # Añadir columnas sin encabezado explícito
        table.add_column("", style=STYLE_ICON, width=24, justify="left")  # Ajustar ancho
        table.add_column("", style=STYLE_VALUE, justify="right")  # Ajustar alineación

        # Agregar filas sin incluir una fila de encabezado adicional
        for key, value in info.items():
            table.add_row(key, str(value))  # Agrega descripción y el valor

        # Obtener el ancho de la consola
        columns, _ = shutil.get_terminal_size()
        panel_width = min(80, columns)  # Ajustar el ancho del panel a un máximo de 80 columnas

        # Mostrar tabla dentro de un panel con borde en degradado y título centrado
        panel = Panel(
            table,
            style=STYLE_PANEL,
            title="[bold bright_green]💀 Información del Sistema 💀[/bold bright_green]",
            title_align="center",  # Centrar el título
            border_style=STYLE_PANEL_BORDER_GRADIENT,  # Estilo del borde con degradado
            width=panel_width,  # Ajustar el ancho del panel
            padding=(1, 2)  # Ajustar el relleno
        )
        
        # Centrar el panel en la consola
        console.print(panel, justify="center")
    else:
        console.print("Formato no soportado. Por favor, elige 'json' o 'table'.", style=STYLE_ERROR)

def display_logo():
    # Mostrar un logo animado más compacto
    logo = """
██╗  ██╗ █████╗ ██╗     ██╗    ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗
██║ ██╔╝██╔══██╗██║     ██║    ██║     ██║████╗  ██║██║   ██║╚██╗██╔╝
█████╔╝ ███████║██║     ██║    ██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝ 
██╔═██╗ ██╔══██║██║     ██║    ██║     ██║██║╚██╗██║██║   ██║ ██╔██╗ 
██║  ██╗██║  ██║███████╗██║    ███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝    ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
                               
    """
    console.print(Text(logo, style="bold bright_green"), justify="center")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Una herramienta moderna para información del sistema con formato enriquecido.")
    parser.add_argument('--format', choices=['json', 'table'], default='table',
                        help='Formato de salida (por defecto: table)')
    args = parser.parse_args()

    # Mostrar logo animado
    display_logo()

    # Pausar para mostrar el logo animado
    time.sleep(1)
    
    system_info = get_system_info()
    print_info(system_info, args.format)
