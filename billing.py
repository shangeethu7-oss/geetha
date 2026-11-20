import streamlit as st

st.title("KGDS Mall")
st.header("Shopping Bill")

shop_name = "KGDS Mall"

customer = st.text_input("Customer Name")

items = {"Pen": 100, "Book": 600, "Bag": 1500, "Watch": 2000}

st.subheader("Select Products")

def subtotal(prices):
    total = 0
    for p in prices:
        total += p
    return total

def discount(sub):
    if sub > 3000:
        return sub * 0.10
    if sub > 1000:
        return sub * 0.05
    return 0

def gst(amount):
    return amount * 0.18

selected_prices = []

for item, price in items.items():
    st.write(item, "Price: Rs.", price)
    qty = st.number_input("Quantity of " + item, min_value=0, value=0, key=item)
    if qty > 0:
        selected_prices.append(price * qty)

if st.button("Generate Bill"):
    st.subheader("Shopping Bill")
    st.write("Shop Name:", shop_name)
    st.write("Customer:", customer)

    sub = subtotal(selected_prices)
    dis = discount(sub)
    g = gst(sub - dis)
    final = sub - dis + g

    st.write("Subtotal:", sub)
    st.write("Discount:", dis)
    st.write("GST (18%):", g)
    st.success("Final Bill: Rs. " + str(final))