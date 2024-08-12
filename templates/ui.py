import flet as ft


class MainLayout:
    def __init__(self, page: ft.Page):
        self.page = page
        self.selected_files = ft.Text()
        self.file_path = ''

    def build_page(self, on_result):
        pick_files_dialog = ft.FilePicker(on_result=on_result)
        self.page.overlay.append(pick_files_dialog)
        main_column = ft.Column(expand=True, alignment=ft.MainAxisAlignment.CENTER)
        open_file_layout = ft.Row([
            ft.ElevatedButton(
                "Загрузить",
                icon=ft.icons.UPLOAD_FILE,
                on_click=lambda _: pick_files_dialog.pick_files(
                    allow_multiple=False
                ),
            ),
            self.selected_files,
        ])
        counter_codes_layout = ft.Row([
            ft.TextField(keyboard_type=ft.KeyboardType.NUMBER, hint_text="Количество кодов", expand=True)
        ])
        log_layout = ft.Row([
            ft.Text("Something text", expand=True, height=70)
        ])
        buttons_layout = ft.Row(
            [
                ft.TextButton("STOP", expand=True, disabled=True, style=ft.ButtonStyle(color=ft.colors.RED)),
                ft.TextButton("START", expand=True, disabled=True, style=ft.ButtonStyle(color=ft.colors.GREEN))
            ], spacing=20
        )
        main_column.controls.insert(0, open_file_layout)
        main_column.controls.insert(1, counter_codes_layout)
        main_column.controls.insert(2, log_layout)
        main_column.controls.insert(3, buttons_layout)

        return main_column
