
import FreeSimpleGUI as sg

layout = [
    [sg.Text("Felicidades por crear una GUI!")],
]


if __name__ == "__main__":
    window = sg.Window("Primer programa", layout)

    while True:
        event, values = window.read()
        # Procesar el evento de cerrar la ventana
        # (si el usuario lo hace)
        if event == sg.WINDOW_CLOSED:
            break


    window.close()