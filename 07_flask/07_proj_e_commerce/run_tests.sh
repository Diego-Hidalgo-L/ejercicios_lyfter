#!/usr/bin/env bash

# Ejecutar todos los tests y guardar los resultados en archivos.
# Se puede ejecutar desde cualquier carpeta: bash ruta/al/proyecto/run_tests.sh

set -o pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR" || exit 1

REPORT_DIR="test_reports"
mkdir -p "$REPORT_DIR"
TEXT_REPORT="$REPORT_DIR/results.txt"
XML_REPORT="$REPORT_DIR/results.xml"

# Priorizar el entorno virtual del proyecto si existe.
if [[ -x ".venv/bin/python" ]]; then
    PYTHON=".venv/bin/python"
else
    PYTHON="python3"
fi

{
    echo "Reporte de tests - E-commerce API"
    echo "Fecha: $(date '+%Y-%m-%d %H:%M:%S')"
    echo "Comando: $PYTHON -m pytest tests/ -v --junitxml=$XML_REPORT"
    echo "----------------------------------------"
} > "$TEXT_REPORT"

"$PYTHON" -m pytest tests/ -v --junitxml="$XML_REPORT" 2>&1 | tee -a "$TEXT_REPORT"
exit_code=${PIPESTATUS[0]}

{
    echo
    echo "----------------------------------------"
    if [[ "$exit_code" -eq 0 ]]; then
        echo "Resultado general: PASSED"
    else
        echo "Resultado general: FAILED (código $exit_code)"
    fi
    echo "Reporte de texto: $TEXT_REPORT"
    if [[ -f "$XML_REPORT" ]]; then
        echo "Reporte JUnit XML: $XML_REPORT"
    else
        echo "No se generó XML (revisar errores en el reporte de texto)."
    fi
} | tee -a "$TEXT_REPORT"

exit "$exit_code"
