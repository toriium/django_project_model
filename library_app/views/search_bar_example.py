from django.shortcuts import render

from components.search_bar import build_search_bar_context


def search_bar_example(request):
    fruits = [
        {"label": "Apple", "color": "red"},
        {"label": "Apricot", "color": "orange"},
        {"label": "Avocado", "color": "green"},
        {"label": "Banana", "color": "yellow"},
        {"label": "Blackberry", "color": "black"},
        {"label": "Blueberry", "color": "blue"},
        {"label": "Cherry", "color": "red"},
        {"label": "Coconut", "color": "brown"},
        {"label": "Grape", "color": "purple"},
        {"label": "Grapefruit", "color": "pink"},
        {"label": "Kiwi", "color": "brown"},
        {"label": "Lemon", "color": "yellow"},
    ]
    colors = [
        {"label": "Black", "hex": "#000000"},
        {"label": "Blue", "hex": "#0000ff"},
        {"label": "Brown", "hex": "#a52a2a"},
        {"label": "Cyan", "hex": "#00ffff"},
        {"label": "Gray", "hex": "#808080"},
        {"label": "Green", "hex": "#008000"},
        {"label": "Orange", "hex": "#ffa500"},
        {"label": "Pink", "hex": "#ffc0cb"},
        {"label": "Purple", "hex": "#800080"},
        {"label": "Red", "hex": "#ff0000"},
        {"label": "White", "hex": "#ffffff"},
        {"label": "Yellow", "hex": "#ffff00"},
    ]

    fruit_search = build_search_bar_context(name="fruit", values=fruits, placeholder="Type a fruit...")
    color_search = build_search_bar_context(name="color", values=colors, placeholder="Type a color...") 
    color_search_preselected = build_search_bar_context(
        name="color preselected", values=colors, placeholder="Type a color...", selected_value=colors[9]
    )
    
    context = {
        "fruit_search": fruit_search,
        "color_search": color_search,
        "color_search_preselected": color_search_preselected,
    }
    return render(request, "library_app/search_bar_example.html", context)
