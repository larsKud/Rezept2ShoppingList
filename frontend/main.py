import streamlit as st
import pandas as pd
class Item():
    def __init__(self, id:int, name: str, category: str, unit: str):
        self.id = id
        self.name = name
        self.category = category
        self.unit = unit

class Recepie():
    def __init__(self, id:int, title: str, description: str, ingredient_list: list[Item], portions: int):
        self.id = id
        self.title = title
        self.description = description
        self.ingredient_list: list[Item] = ingredient_list
        self.portions = portions

def main():
    tabs = ["Recepies", "Shoppinglist", "Add Recepies", "Add Ingredient"]
    tab1, tab2, tab3, tab4 = st.tabs(tabs=tabs)

    with tab1:
        view_recepie_list()
    with tab2: 
        view_shopping_list()
    with tab3:
        add_recepies()
        
    with tab4:
        add_ingredients()
    

def add_recepies():

    #keys 
    add_ing_key = "add_ingredient_button"
    ing_selector_key = "ingredient_selector"
    add_ing_form_key = "add_ing_form"

    st.title("Add a new Recepie")
    st.text_input("Title")
    with st.container():
        if add_ing_key in st.session_state:
            st.info("Button pressed")

        
        ingredients: list[tuple[Item, int]] = [(Item(0, "Gurke", "Gemüse", "g"), 500)] # get this from backend
        display_dict = {"Ingredient": [], "Quantity": []}
        for ingredient, quantity in ingredients:
            display_dict['Ingredient'].append(ingredient.name)
            display_dict['Quantity'].append(f"{str(quantity)} {ingredient.unit}")
        # render table
        st.table(display_dict)
        
        # Add ingredient form
        with st.form(key=add_ing_form_key):
            with st.container(horizontal=True):
                ingredient_options = ["A", "B"]
                st.selectbox(label="Ingredient", options=ingredient_options, key=ing_selector_key)
                st.number_input(label="Quantity", step=1)
                unit_options = ["ml", "g", "Stk"]
                st.selectbox(label="Unit", options = unit_options)
            st.form_submit_button(label="Add", key=add_ing_key)

    with st.container(width=150):
        st.number_input(label="Portions", step=1, value=4)

    st.text_area("Description")

    save = st.button(label="Save")
    if save:
        pass #TODO: add recepie
    

def add_ingredients():
    st.title("Add Ingredient")
    st.text_input("Name")
    category_options = ["Gemüse", "Obst", "Backwaren"]

    st.selectbox("Category", category_options)
    unit_options = ["ml", "g", "Stk"]

    st.selectbox(label="Base Unit", options = unit_options)
    with st.container(width=300):
        for unit in unit_options:
            st.number_input(label=f"Conversion to {unit}")
    
    save = st.button(label="Save")
    if save:
        pass #TODO: add recepie
        

def view_recepie_list():
    st.title("Recepies")
    recepies_list: list[Recepie] = get_recepie_list_dummy()
    with st.container(border=False):
        for i,recepie in enumerate(recepies_list):
            with st.container(horizontal=True, border=True):
                st.subheader(recepie.title)
                with st.container(width=150):
                    st.number_input("Portions", key=f"num_input_{i}", step=1, label_visibility="collapsed")
                view = st.button("View", key=f"view_{i}")
                if view:
                    view_recepie(recepie.id)

@st.dialog("Recepie")
def view_recepie(id: int):
    recepie = get_recepie_list_dummy()[id]
    st.title(recepie.title)
    ingredient_list = _get_table_from_ingredient_list(recepie.ingredient_list)
    st.table(ingredient_list)
    st.space()
    st.markdown(recepie.description)
    portion_val = st.session_state[f"num_input_{id}"]
    portion = st.number_input("Portions", value=portion_val, step=1)
    if portion != st.session_state[f"num_input_{id}"]:
        st.session_state[f"num_input_{id}"] = portion

        
def _update_portion_if_changed():
    pass

def view_shopping_list():
    pass
    
def _get_table_from_ingredient_list(ingredients: list[tuple[Item, int]]):
    display_dict = {"Ingredient": [], "Quantity": []}
    for ingredient, quantity in ingredients:
        display_dict['Ingredient'].append(ingredient.name)
        display_dict['Quantity'].append(f"{str(quantity)} {ingredient.unit}")
    return display_dict

def get_item_list_dummy():
    I1 = Item(0, "Gurke", "Gemüse", "g")
    I2 = Item(1, "Wasser", "--", "ml")
    I3 = Item(2, "Gummibärchen", "Süssigkeit", "g")
    return [I1, I2, I3]

def get_recepie_list_dummy():
    item_list = get_item_list_dummy()
    R1 = Recepie(0, "Gurken Wasser", "Schnibbel die Gurke in das Wasser und Fertig!", [(item_list[0], 500),(item_list[1], 1000)],4)
    R2 = Recepie(1, "Döner", "Schnibbel die Gurke in das Wasser und Fertig! und nenne es einfach Döner",[(item_list[0], 500),(item_list[1], 1000)],4)
    return [R1, R2]

if __name__ == "__main__":
    main()

