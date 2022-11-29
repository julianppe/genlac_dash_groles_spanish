import dash
from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container

from dash_extensions.enrich import (
    DashProxy,
    MultiplexerTransform,
    html,
    dcc,
)

external_stylesheets = [dbc.themes.JOURNAL]

app = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    use_pages=True,
    prevent_initial_callbacks=True,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
)

server = app.server

GENLAC_LOGO = "/assets/genlac.png"

dropdown = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Brechas entre cónyuges", header=True),
            dbc.DropdownMenuItem("Diferencia de edad entre conyuges", href="/"),
            dbc.DropdownMenuItem("Diferencia educativa entre conyuges", href="/diferencia-educativa"),
            dbc.DropdownMenuItem("Diferencia de horas trabajadas entre cónyuges", href="/diferencia-horas"),
            dbc.DropdownMenuItem("Porcentaje del ingreso de la pareja aportado por cada miembro", href="/porcen-ingreso-pareja"),
            dbc.DropdownMenuItem("Porcentaje de personas más o igualmente educadas que su pareja que se encuentran inactivas", href="/porcentaje-mas-educacion"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Autonomía", header=True),
            dbc.DropdownMenuItem("Porcentaje de adultos sin ingresos propios", href="/autonomia"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Estructura y jefatura de hogar", header=True),
            dbc.DropdownMenuItem("Jefatura de hogar femenina auto-reportada", href="/jefatura-hogar-auto"),
            dbc.DropdownMenuItem("Jefatura de hogar femenina según definición económica", href="/jefatura-hogar-econ"),
            dbc.DropdownMenuItem("Porcentaje de hogares monoparentales", href="/porcen-hog-mono"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Uso del tiempo", header=True),
            dbc.DropdownMenuItem("Participación en tareas domésticas", href="/tareas-domesticas"),
            dbc.DropdownMenuItem("Horas semanales en tareas domésticas", href="/horas-tareas-domesticas"),
            dbc.DropdownMenuItem("Participación en actividades de cuidado", href="/actividades-cuidado"),
            dbc.DropdownMenuItem("Horas semanales dedicadas a actividades de cuidado", href="/horas-actividades-cuidado"),
            dbc.DropdownMenuItem("Participación en actividades de cuidado de niños", href="/actividades-cuidado-ninos"),
            dbc.DropdownMenuItem("Horas semanales dedicadas a actividades de cuidado de niños", href="/horas-actividades-cuidado-ninos"),
            dbc.DropdownMenuItem("Participación en actividades de apoyo a otros hogares", href="/actividades-apoyo"),
            dbc.DropdownMenuItem("Horas semanales dedicadas a actividades de apoyo a otros hogares", href="/horas-actividades-apoyo"),
            dbc.DropdownMenuItem("Participación en actividades de ocio", href="/actividades-ocio"),
            dbc.DropdownMenuItem("Horas semanales dedicadas a actividades de ocio", href="/horas-actividades-ocio"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Fecundidad", header=True),
            dbc.DropdownMenuItem("Tasa de fecundidad", href="/tasa-fecundidad"),
            dbc.DropdownMenuItem("Tasa de fecundidad deseada", href="/tasa-fecundidad-deseada"),
            dbc.DropdownMenuItem("Brecha entre fecundidad y fecundidad deseada", href="/brecha-fecundidad-deseada"),
            dbc.DropdownMenuItem("Brecha de fecundidad deseada entre cónyuges", href="/brecha-fecundidad-deseada-conyuges"),
            dbc.DropdownMenuItem("Porcentaje de mujeres que utilizan métodos anticonceptivos (cualquier método)", href="/metodo-anticonceptivos"),
            dbc.DropdownMenuItem("Porcentaje de mujeres que utilizan métodos anticonceptivos modernos", href="/metodo-anticonceptivos-modernos"),
            dbc.DropdownMenuItem("Porcentaje de mujeres sin acceso a métodos anticonceptivos", href="/metodo-anticonceptivos-sinacceso"),
            dbc.DropdownMenuItem("Fecundidad adolescente", href="/fecundidad-adolescente"),
            dbc.DropdownMenuItem("Matrimonio precoz", href="/matrimonio-precoz"),
        ],
        size="lg",
        nav=True,
        in_navbar=True,
        label="Indicadores",
        className="ms-0",
        toggle_style={"color": "#460074"},
        align_end=False,
        style={'width':'100%'}

        )
    )
],
className="g-0 ms-auto flex-nowrap mt-5 mt-md-0",
align="center",
)


navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(
                            dropdown, 
                            className="ml-auto",
                            id="navbar-collapse",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
        ],
    fluid=True),
    #outline=True, 
    color="light",
    dark=True,
)
# Definimos el layout:
app.layout = html.Div(
    [
        dcc.Store(id="store", data='Argentina'),
        dbc.Container([
    dbc.Row(
        [
            navbar # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True)
    ]
)


if __name__ == "__main__":
    app.run_server()