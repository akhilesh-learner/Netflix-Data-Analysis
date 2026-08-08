# Import Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Page Configuration
st.set_page_config(
    page_title="Netflix Analytics Dashboard",
    page_icon="🎬",
    layout="wide"
)

#Loading Dataset
@st.cache_data
def load_data():
    df = pd.read_csv(
        "data/netflix_titles.csv"
    )

    df["date_added"] = (
        df["date_added"]
        .str.strip()
    )

    df["date_added"] = pd.to_datetime(
        df["date_added"],
        errors="coerce"
    )

    df["year_added"] = (
        df["date_added"]
        .dt.year
    )
    return df

df = load_data()

# Dashboard Title
st.title("🎬 Netflix Data Analytics Dashboard")
st.write(
    """
    Interactive Analysis of Netflix movies and TV shows
    using Python, Pandas, Matplotlib, Seaborn and Streamlit.
    """
)

#Sidebar Filters
st.sidebar.header("Filters")


type_filter = st.sidebar.multiselect(
    "Select Content Type",
    df["type"].unique(),
    default=df["type"].unique()
)


year_filter = st.sidebar.slider(
    "Select Release Year",
    int(df["release_year"].min()),
    int(df["release_year"].max()),
    (int(df["release_year"].min()),
     int(df["release_year"].max()))
)


filtered_df = df[
    (df["type"].isin(type_filter))
    &
    (df["release_year"].between(
        year_filter[0],
        year_filter[1]
    ))
]

#KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Titles",
        filtered_df.shape[0]
    )

with col2:
    st.metric(
        "Movies",
        len(
            filtered_df[
                filtered_df["type"]=="Movie"
            ]
        )
    )

with col3:
    st.metric(
        "TV Shows",
        len(
            filtered_df[
                filtered_df["type"]=="TV Show"
            ]
        )
    )
    
# Movie vs TV Show Chart
st.subheader(
    "Movie vs TV Show Distribution"
)

fig, ax = plt.subplots()

sns.countplot(
    data=filtered_df,
    x="type",
    hue="type",
    legend=False,
    ax=ax
)
st.pyplot(fig)

#Content Added Over Time
st.subheader(
    "Netflix Growth Over Years"
)

year_data = (
    filtered_df
    .groupby("year_added")
    .size()
)

fig, ax = plt.subplots(
    figsize=(10,4)
)

sns.lineplot(
    x=year_data.index,
    y=year_data.values,
    marker="o",
    ax=ax
)

ax.set_xlabel("Year")
ax.set_ylabel("Titles Added")

st.pyplot(fig)


# Top COuntries
st.subheader(
    "Top Producing Countries"
)


countries = (
    filtered_df["country"]
    .dropna()
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)


fig, ax = plt.subplots()


sns.barplot(
    x=countries.values,
    y=countries.index,
    hue=countries.index,
    legend=False,
    ax=ax
)


st.pyplot(fig)


# Top Genres
st.subheader(
    "Most Popular Genres"
)


genres = (
    filtered_df["listed_in"]
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)


fig, ax = plt.subplots()

sns.barplot(
    x=genres.values,
    y=genres.index,
    hue=genres.index,
    legend=False,
    ax=ax
)

st.pyplot(fig)