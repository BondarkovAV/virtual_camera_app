import flet as ft


class MainLayout:
    def __init__(self, page: ft.Page, click_start, click_stop, text_changed, on_result):
        self.page = page
        self.but_stop = ft.TextButton("STOP", expand=True, disabled=True, style=ft.ButtonStyle(color=ft.colors.RED),
                                      on_click=click_stop)
        self.but_start = ft.TextButton("START", expand=True, disabled=True, style=ft.ButtonStyle(color=ft.colors.GREEN),
                                       on_click=click_start)
        self.codes_count = ft.TextField(hint_text="Количество кодов", expand=True, on_change=text_changed)
        self.selected_files = ft.Text()
        self.connection_text = ft.Text("", expand=True, color=ft.colors.GREEN)
        self.log_text = ft.Text("", expand=True, color=ft.colors.LIGHT_BLUE_ACCENT_700, max_lines=4,
                                height=90)
        self.pick_files_dialog = ft.FilePicker(on_result=on_result)
        self.page.overlay.append(self.pick_files_dialog)
        self.open_file_btn = ft.ElevatedButton(
                "Загрузить .txt",
                icon=ft.icons.UPLOAD_FILE,
                on_click=lambda _: self.pick_files_dialog.pick_files(
                    allow_multiple=False, file_type=ft.FilePickerFileType.CUSTOM,
                    allowed_extensions=["txt"]
                ),
                icon_color=ft.colors.WHITE,
                color=ft.colors.WHITE
            )

    def build_page(self):

        main_column = ft.Column(expand=True, alignment=ft.MainAxisAlignment.CENTER)
        open_file_layout = ft.Row([
            self.open_file_btn,
            self.selected_files,
        ])
        counter_codes_layout = ft.Row([
            self.codes_count
        ])
        connect_layout = ft.Row([self.connection_text,])
        log_layout = ft.Row([self.log_text])
        buttons_layout = ft.Row(
            [
                self.but_stop,
                self.but_start
            ], spacing=20
        )
        main_column.controls.insert(0, open_file_layout)
        main_column.controls.insert(1, counter_codes_layout)
        main_column.controls.insert(2, connect_layout)
        main_column.controls.insert(3, log_layout)
        main_column.controls.insert(4, buttons_layout)

        return main_column
