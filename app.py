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
            dbc.DropdownMenuItem("Ámbito político", header=True),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “Los hombres son mejores líderes políticos que las mujeres”", href="/"),
            dbc.DropdownMenuItem("Población de acuerdo con que la mitad de los miembros del parlamento sean mujeres", href="/equidad-parlamento"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Ámbito laboral", header=True),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “ante la escasez de empleo, los hombres deberían tener más derecho a un empleo que las mujeres”", href="/derecho-empleo"),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “los hombres son mejores empresarios que las mujeres”", href="/empresarios"),
            dbc.DropdownMenuItem("Población adulta que opina que los empresarios no contratan a mujeres con niños", href="/empleador-nocontrata-madres"),
            dbc.DropdownMenuItem("Población adulta que opina que un equipo de trabajo formado por hombres y mujeres logra mejores resultados que un equipo formado solo por hombres", href="/equipo-balance"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Ámbito educativo", header=True),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “la educación universitaria es más importante para un varón que para una mujer”", href="/universidad"),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “las mujeres tienen las mismas capacidades que los hombres para la ciencia y la tecnología”", href="/capacidad-ciencia"),
            dbc.DropdownMenuItem("Docentes de 3er grado que opinan que niños o niñas aprenden más rápido matemática o lengua debido a características innatas", href="/aprenden-rapido-3ro"),
            dbc.DropdownMenuItem("Docentes de 6to grado que opinan que niños o niñas aprenden más rápido matemática, lengua o ciencias debido a características innatas", href="/aprenden-rapido-6to"),
            dbc.DropdownMenuItem("Porcentaje de alumnos de 15 años que espera trabajar en ocupaciones relacionadas a STEM a los 30 años", href="/stem-15"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Ámbito familiar", header=True),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “si una mujer gana más dinero que su marido, es casi seguro que causará problemas”", href="/mujer-gana-mas"),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “cuando una madre trabaja, sus hijos sufren”", href="/madre-trabaja"),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “ser ama de casa es tan gratificante como tener un trabajo remunerado”", href="/ama-de-casa"),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “las mujeres deben trabajar sólo si la pareja no gana suficiente”", href="/mujer-trabaja-pareja"),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “es mejor que la mujer se concentre en el hogar y el hombre en el trabajo”", href="/mujer-casa-hombre-trabajo"),
            dbc.DropdownMenuItem("Porcentaje de mujeres que piensan que está justificado que los maridos golpeen a sus esposas en algunas situaciones", href="/justifica-golpear"),
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