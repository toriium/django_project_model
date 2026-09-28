from django.shortcuts import render

from components.search_bar import build_search_bar_context


def search_bar_example(request):
    fruits = [
        "Apple",
        "Apricot",
        "Avocado",
        "Banana",
        "Blackberry",
        "Blueberry",
        "Cherry",
        "Coconut",
        "Grape",
        "Grapefruit",
        "Kiwi",
        "Lemon",
        "Lime",
        "Mango",
        "Melon",
        "Orange",
        "Papaya",
        "Peach",
        "Pear",
        "Pineapple",
        "Plum",
        "Raspberry",
        "Strawberry",
        "Watermelon",
    ]
    context = {"fruit_search": build_search_bar_context(name="fruit", values=fruits, placeholder="Type a fruit...")}
    return render(request, "library_app/search_bar_example.html", context)
