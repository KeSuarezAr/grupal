from reflex import Style

text_style = Style({
    "font-size": "3em",
    "font-weight": "bold",
    "color": "white",
    "text-align": "center",
    "font-family": "'Helvetica Neue', Arial, sans-serif",
    "flex": "1"
})

image_style = Style({
    "width": "50%",
    "height": "auto",
    "border-radius": "0.5em"
})

box_style = Style({
    "width": "100%",
    "align-items": "center",
    "justify-content": "space-between"
})

header_style = Style({
    "width": "70%",
    "margin": "auto",
    "padding": "3em",
    "background": "linear-gradient(180deg, #003366 0%, #66ccff 100%)",
    "border-radius": "0.5em",
    "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)"
})

curso_card_style = Style({
    "width": "200px",
    "margin": "1em",
    "padding": "1em",
    "background": "rgba(0, 0, 0, 0.7)",
    "border-radius": "0.5em",
    "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.2)"
})

cursos_box_style = Style({
    "display": "flex",
    "justify-content": "center",
    "flex-wrap": "wrap",
    "margin-top": "2em"
})

login_button_style = Style({
    "color": "white",
    "background-color": "#005f99",
    "hover_background_color": "#004080",
    "border-radius": "0.3em",
    "padding": "1em",
    "position": "absolute",
    "top": "1em",
    "left": "1em",
    "cursor": "pointer"
})

index_page_style = Style({
    "width": "100%",
    # "height": "100vh",
    "height": "100%",
    "background": "#003366",
    "display": "flex",
    "flex-direction": "column",
    "align-items": "center"
})
