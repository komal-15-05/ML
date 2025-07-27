import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def show_graphs(df):
    import streamlit as st

    # Example: Risk distribution
    fig1, ax1 = plt.subplots()
    ax1.hist(df["Heart Attack Risk"], bins=2, color="orange", edgecolor="black")
    ax1.set_title("Heart Attack Risk Distribution")
    st.pyplot(fig1)

    # Example: Age vs Cholesterol scatter
    fig2, ax2 = plt.subplots()
    colors = df["Heart Attack Risk"].map({0: "blue", 1: "red"})
    ax2.scatter(df["Age"], df["Cholesterol"], c=colors, alpha=0.6)
    ax2.set_title("Age vs Cholesterol")
    st.pyplot(fig2)
