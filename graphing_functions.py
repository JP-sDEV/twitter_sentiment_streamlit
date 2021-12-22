import altair as alt
import plotly.express as px
import plotly.graph_objects as go

def plot_compound_score(df, score_name, title=""):
    """
    Plot a line graph for the compound score
    Each point is a single tweet's compound score

    Returns an Altair Chart object
    """
    base = alt.Chart(df).transform_calculate(
        score_line = "'score_line'",
        score_point="'score_point'",
    ).properties(title=title)

    scale = alt.Scale(domain =["score_line", "score_point"], 
                    range=["#1DA1F2", "orange"]) # twitter color

    line_plot = base.mark_line(opacity=1).encode(
        x=alt.X("date", title="timeline"),
        y=alt.Y(score_name),
        color = alt.Color("score_line:N", scale=scale, title=""),
        tooltip=[alt.X("date"), alt.Y(score_name)]
    ).interactive()

    scatter_plot = base.mark_circle(size=50, opacity=0.75).encode(
        x=alt.X("date"),
        y=alt.Y(score_name, title="sentiment score"),
        color = alt.Color("score_point:N", scale=scale, title=""),
        tooltip=[alt.X("date"), alt.Y(score_name)]
    ).interactive()

    combined_layer = alt.layer(line_plot+scatter_plot)

    return combined_layer

def plot_score_average(avg_df, x, y, title=""):
    """
    Plot a bar chart of a score's average

    Return a Plotly Graph Object
    """
    fig = px.bar(
        avg_df,
        # x=x,
        y=y,
        title=title
    )
    fig.update_traces(width=0.5)

    return fig

def plot_pie_chart(avg_df, x, y, title=""):
    """
    Plot a pie chart, showing the distribution of scores in the compound score

    Return a Plotly Graph Object 
    """
    fig = px.pie(
        avg_df,
        values=y,
        names=x,
        title=title
    )
    return fig

def plot_boxplot(df, y, title=""):
    """
    Plot a boxplot, showing the distribution of a single score metric

    Return a Plotly Graph Object
    """
    fig = px.box(df, y=y, title=title)

    return fig