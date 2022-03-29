# from asyncio.windows_events import NULL
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

header = st.container()
map = st.container()

@st.cache
def get_data():  # load in the data
    data = pd.read_csv("https://raw.githubusercontent.com/BryceBlignaut/team_agile_W22/master/data/model_export/export.csv")
    return data

st.markdown(
    """
<style>
.main {
    background-color: #000000;
}
</style>
    """,
    unsafe_allow_html=True,
)

# --- BODY ---
# header
with header:
    st.title("Where Should I Place My Business?")

# def update_state(df):
    # df = df.query("region == st.session_state.state_select")


with map:

    data = get_data()

    st.write("Considering where to place a new business is a risky business. Choose the wrong spot and you could face financial run.That's why we at WhereShouldIPlaceMyBusiness.Inc are here to help.")

    st.write("Feel free to explore the map below to see where you should start building.")

    df = data[["tract","region","county_name","city","total_visits", "avg_income","total_businesses","lat","lon","diff", "should_build"]]

    value_selected = False

    col1, col2, col3 = st.columns(3)

    with col1:
        state = st.multiselect("Select State",df["region"].unique())
        if(state != []):
            df = df[(df.region == state[0])]
            value_selected = True
    with col2:
        county = st.multiselect("Select County",df["county_name"].unique())
        if(county != []):
            df = df[(df.county_name == county[0])]
            value_selected = True
    with col3:
        city = st.multiselect("Select City",df["city"].unique())
        if(city != []):
            df = df[(df.city == city[0])]
            value_selected = True

    # st.map(df) #This is the basic map. Can't change colors. But it looks nice by itself. And it filters way nice
    st.write("The more green an area is, the more growth potential there")
    #IDK about the colors in this map. But it works.
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v10',
        initial_view_state=pdk.ViewState(
            latitude=42.860851,
            longitude=-110.117649,
            zoom=4.25,
            min_zoom=4,
            max_zoom=15
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df[['lat','lon','diff']].dropna(),
                get_position=['lon', 'lat'],
                auto_highlight=True,
                pickable=True,
                get_radius=1000,
                get_fill_color=['diff < 0 ? diff * -255 : 0', 'diff > 0 ? diff * 255 : 0', 0, 160],
                coverage=1,
                radius_min_pixels=3,
                radius_max_pixels=5)
        ]
    ))

    if value_selected:    
        st.write("What makes these places a great place to build?")

        st.write(df[["tract","region","county_name","city","total_visits", "avg_income","total_businesses", "should_build"]])
