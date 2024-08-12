import socket
import time

import flet as ft
import json
from templates.ui import MainLayout
from socket_connection import ConnectSocket


with open('settings.json', 'r') as file:
    settings = json.load(file)

host: str = settings['camera_host']
port: int = settings['camera_port']
delay: int = settings['delay']

sc = ConnectSocket(host, port)
codes_count = 0
max_count = 0
codes_list = []
n = 0
start = False
#telnet 192.168.1.126 9999


async def main(page: ft.Page):
    def read_file(path):
        global codes_count
        global max_count
        codes_base = []
        with open(path, 'r') as f:
            codes = f.readlines()
            for code in codes:
                code_n = code.rstrip()
                code_r = "{" + code_n + "}"
                codes_base.append(code_r)
            codes_count = len(codes_base)
            max_count = codes_count
            main_layout.codes_count.value = len(codes_base)
            main_layout.codes_count.update()
            main_layout.log_text.value = f"Загружено {len(codes_base)} строк."
            main_layout.log_text.update()
        return codes_base

    def pick_files_result(e: ft.FilePickerResultEvent):
        global codes_list
        global n
        print(e.files)
        if e.files:
            n = 0
            file_type = e.files[0].name.split('.')[1]
            if file_type == 'txt':
                main_layout.selected_files.value = e.files[0].name
                main_layout.selected_files.color = ft.colors.GREEN
                main_layout.selected_files.update()
                path = e.files[0].path
                codes_list = read_file(path)
            else:
                main_layout.selected_files.value = "Тип файла не txt!"
                main_layout.selected_files.color = ft.colors.RED
                main_layout.selected_files.update()

    def check_input(input_str):
        try:
            int(input_str)
            return True
        except Exception as ex:
            print(ex)
            return False

    def textbox_changed(e):
        global codes_count
        global max_count
        new_count = e.control.value
        if check_input(new_count):
            new_count = int(new_count)
            if codes_count != 0 and codes_count >= new_count:
                max_count = new_count
            elif codes_count == 0:
                max_count = new_count
            else:
                main_layout.codes_count.value = codes_count
                main_layout.codes_count.update()
                max_count = codes_count
            print(max_count)
        else:
            main_layout.codes_count.value = ''
            main_layout.codes_count.update()
            main_layout.log_text.value = "Вы ввели не число!"
            main_layout.log_text.update()

    def send_code(code):
        con.sendall(code)
        time.sleep(delay / 1000)

    def click_start(e):
        global codes_list
        global max_count
        global start
        global n
        start = True
        main_layout.but_stop.disabled = False
        main_layout.but_stop.update()
        main_layout.but_start.disabled = True
        main_layout.but_start.update()
        while start:
            if n < max_count:
                code_b = codes_list[n].encode()
                main_layout.log_text.value = f"-{n + 1} Отправлен код {codes_list[n]}"
                main_layout.log_text.update()
                main_layout.codes_count.value = int(main_layout.codes_count.value) - 1
                main_layout.codes_count.update()
                send_code(code_b)
                n += 1
            else:
                main_layout.log_text.value = main_layout.log_text.value + "\nВыполнено!"
                main_layout.log_text.update()
                main_layout.codes_count.value = max_count
                main_layout.codes_count.update()
                n = 0
                start = False

    def click_stop(e):
        global start
        start = False
        main_layout.but_stop.disabled = True
        main_layout.but_stop.update()
        main_layout.but_start.disabled = False
        main_layout.but_start.update()
        main_layout.log_text.value = main_layout.log_text.value + "\nОстановлено!"
        main_layout.log_text.update()

    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.theme = ft.Theme(color_scheme_seed=ft.colors.LIGHT_BLUE_ACCENT_700, font_family="Ubuntu")
    page.window.resizable = False
    page.window.maximizable = False
    page.window.height = 350
    page.window.width = 700
    page.spacing = 20
    page.title = "Virtual Camera App"

    main_layout = MainLayout(page, click_start, click_stop, textbox_changed)
    page.add(
        main_layout.build_page(pick_files_result)
    )
    main_layout.connection_text.value = "Ожидание подключения..."
    page.update()
    con, addr_string = await sc.connect()
    print(f"Connection = {con}, type = {type(con)}")
    main_layout.connection_text.value = addr_string
    main_layout.connection_text.update()
    main_layout.but_start.disabled = False
    main_layout.but_start.update()


ft.app(target=main, view=ft.AppView.FLET_APP)
