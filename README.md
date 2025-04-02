# 🧪 Kata: String Calculator (Python + TDD)

Este proyecto es una implementación de la Kata String Calculator utilizando Python y el enfoque de Desarrollo Guiado por Pruebas (TDD). La idea principal es ir construyendo la lógica a medida que se agregan tests unitarios que guían el desarrollo.

---

## 🚀 Reglas implementadas

- ✅ Sumar dos números separados por coma.
- ✅ Retornar 0 si la cadena está vacía.
- ✅ Soportar múltiples números separados por coma.
- ✅ Soportar saltos de línea como separadores.
- ✅ Lanzar un error si hay números negativos.
- ✅ Ignorar números mayores a 1000.
- ✅ Soportar delimitador personalizado (ej: `//;\n1;2` usa `;` como separador).

---

## 🛠️ Requisitos

- Python 3.10 o superior

---

## 📦 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/crmunozb/kata-string-calculator.git
cd kata-string-calculator

# Ejecutar los tests
python3 -m unittest test_string_calculator.py
