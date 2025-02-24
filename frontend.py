import flet as ft
from backend import evaluate_expression

def main(page: ft.Page):
    page.title = "Calculator"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.padding = 20

    expression_input = ft.TextField(
        label="Enter your expression",
        hint_text="e.g., 3 + 5 * 2",
        width=400,
        autofocus=True,
    )

    result_output = ft.Text(
        size=20,
        weight="bold",
        color=ft.colors.GREEN,
    )

    def calculate(e):
        expression = expression_input.value.strip()
        if not expression:
            result_output.value = "Error: Please enter an expression."
            result_output.color = ft.colors.RED
        else:
            try:
                result = evaluate_expression(expression)
                result_output.value = f"Result: {result}"
                result_output.color = ft.colors.GREEN
            except Exception as ex:
                result_output.value = f"Error: {str(ex)}"
                result_output.color = ft.colors.RED
        page.update()

    calculate_button = ft.ElevatedButton(
        text="Calculate",
        on_click=calculate,
        width=200,
    )

    page.add(
        ft.Column(
            [
                ft.Text("Calculator", size=30, weight="bold"),
                expression_input,
                calculate_button,
                result_output,
            ],
            alignment="center",
            spacing=20,
        )
    )

ft.app(target=main)
