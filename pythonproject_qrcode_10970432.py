import PySimpleGUI as sg
import qrcode
import io
import threading

def generate_qr_code(input_value):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(input_value)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    bio = io.BytesIO()
    img.save(bio, format='PNG')
    img_bytes = bio.getvalue()
    window['-IMAGE-'].update(data=img_bytes)
def main():
    layout = [[sg.Text('Enter input:'), sg.InputText(key='-INPUT-')],
              [sg.Button('Generate QR Code', key='-GENERATE-')],
              [sg.Image(key='-IMAGE-')]]
    global window
    window = sg.Window('QR Code Generator', layout,background_color='pink')
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == '-GENERATE-':
            input_value = values['-INPUT-']
        if not input_value:   
           sg.popup_error('Input is empty')
        else:
            threading.Thread(target=generate_qr_code, args=(input_value,)).start()
    window.close()
if __name__ == '__main__':
    main()
