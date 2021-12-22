import streamlit as st
from helper_functions import get_score_avgs
from tweepy_q import query_tweets, results_to_df
from graphing_functions import plot_compound_score, plot_score_average, plot_pie_chart, plot_boxplot

# STREAMLIT COMPONENTS
st.set_page_config(layout="wide")
main_title = st.markdown("<h1 style='text-align: center;'>📈 Twitter Hashtag Sentiment Analysis</h1>", unsafe_allow_html=True)

# SIDEBAR COMPONENTS
sidebar = st.sidebar
form = sidebar.form(key = "hashtag_form")
hashtag = form.text_input(label = "Enter a twitter hashtag", value="#")
tweet_type = form.radio(
    "Type of Tweets",
    ("Popular",
    "Recent",
    "Mixed")
)
submit_btn = form.form_submit_button(label = "Submit")

about_toggle = sidebar.expander("About")
with about_toggle:
    "Detect the underlying sentiment of a trending Twitter hashtag(#)"

# MAIN SCREEN/BODY COMPONENTS
if submit_btn:
    main_title = st.subheader(f"{hashtag.upper()} Sentiment")
    twitter_query = query_tweets(hashtag=hashtag, result_type=tweet_type)
    tweets_df = results_to_df(twitter_query)

    # COMPOUND SCORE GRAPHS/PLOTS
    col1, col2 = st.columns([5,2])
    
    with col1:
        compound_line_chart = plot_compound_score(tweets_df, "compound", title="Sentiment Over Time")
        st.altair_chart(compound_line_chart, use_container_width=True)
    
    with col2:
        avg_all_scores = get_score_avgs(tweets_df, ["pos", "neg", "neu"])
        avg_all_scores_plot = plot_pie_chart(avg_all_scores, "score_name", "score_average", title="Sentiment Score Breakdown")
        st.plotly_chart(avg_all_scores_plot, use_container_width=True)

    
    col3, col4 = st.columns([1,1])
    with col3:
        avg_compound_score = get_score_avgs(tweets_df, ["compound"])
        avg_compound_score_plot = plot_score_average(avg_compound_score, "score_name", "score_average", title="Sentiment Average Score")
        st.plotly_chart(avg_compound_score_plot, use_container_width=True)

    with col4:
        compound_score_boxplot = plot_boxplot(tweets_df, "compound", title="Compound Score Distribution")
        st.plotly_chart(compound_score_boxplot)

    # SCORE COMPONENTS 
    score_types = ["pos", "neu", "neg"]

    for score in score_types:
        expander = st.expander(f"{score.upper()} Breakdown")
        with expander:
            scores = get_score_avgs(tweets_df, [score])
            scores_plot = plot_compound_score(tweets_df, score, title=f"{score.upper()} Score Over Time")
            box_plot = plot_boxplot(tweets_df, score, title=f"{score.upper()} Score Distribution")
            st.altair_chart(scores_plot, use_container_width=True)
            st.plotly_chart(box_plot)
    
    twitter_df = st.expander("Tweets Dataframe")
    with twitter_df:
        st.dataframe(tweets_df)