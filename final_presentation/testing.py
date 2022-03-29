#I used this file to figure out the map. Feel free to play with it if you want

# %%
import pydeck
import pandas as pd
df = pd.read_csv("..\data\model_export\export.csv")
#%%
layer = pydeck.Layer(
    'ScatterplotLayer',
    df,
    get_position=['lon', 'lat'],
    auto_highlight=True,
    pickable=True,
    get_radius=1000,
    get_fill_color=['diff < 0 ? diff * -25500 : 0', 'diff > 0 ? diff * 25500 : 0', 0, 255],
    coverage=1,
    radius_min_pixels=3,
    radius_max_pixels=6)

view_state = pydeck.ViewState(
    latitude=42.860851,
    longitude=-110.117649,
    zoom=4.5,
    min_zoom=4,
    max_zoom=15)

r = pydeck.Deck(layers=[layer], initial_view_state=view_state, map_style='light')
r.to_html('hexagon-example.html')
# %%
import pydeck as pdk
pdk.Deck(
        initial_view_state=pdk.ViewState(
            latitude=42.860851,
            longitude=-110.117649,
            zoom=4.5,
            min_zoom=4,
            max_zoom=15
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                df,
                get_position=['lon', 'lat'],
                auto_highlight=True,
                pickable=True,
                get_radius=1000,
                get_fill_color=['diff < 0 ? diff * -25500 : 0', 'diff > 0 ? diff * 25500 : 0', 0, 255],
                coverage=1,
                radius_min_pixels=3,
                radius_max_pixels=6)
        ],
        map_style='light'
    )
# %%
