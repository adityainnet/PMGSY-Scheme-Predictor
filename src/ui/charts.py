"""
Chart visualizations for the Streamlit application.
"""

import streamlit as st
import plotly.graph_objects as go
from typing import List


def render_gauge_chart(confidence: float):
    """
    Render a confidence gauge chart.
    
    Args:
        confidence: Confidence percentage (0-100)
    """
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence,
        number={'suffix': '%', 'font': {'size': 36, 'color': '#f8fafc'}},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {
                'range': [0, 100],
                'tickwidth': 1,
                'tickcolor': "#475569",
                'tickfont': {'color': '#cbd5e1'}
            },
            'bar': {'color': "#6366f1", 'thickness': 0.3},
            'bgcolor': "#111827",
            'borderwidth': 1,
            'bordercolor': "rgba(99, 102, 241, 0.2)",
            'steps': [
                {'range': [0, 60], 'color': 'rgba(239, 68, 68, 0.15)'},
                {'range': [60, 80], 'color': 'rgba(245, 158, 11, 0.15)'},
                {'range': [80, 100], 'color': 'rgba(16, 185, 129, 0.15)'}
            ]
        }
    ))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': "#f8fafc", 'family': "Plus Jakarta Sans, Inter"},
        height=250,
        margin=dict(l=20, r=20, t=20, b=20)
    )
    
    st.plotly_chart(fig, width='stretch')


def render_probability_chart(probabilities: List[float], max_confidence: float):
    """
    Render a bar chart showing probability distribution across classes.
    
    Args:
        probabilities: List of probability values for each class
        max_confidence: The highest confidence value (for highlighting)
    """
    with st.expander("📊 View All Class Probabilities", expanded=False):
        fig = go.Figure(
            data=[
                go.Bar(
                    x=[f"Class {i}" for i in range(len(probabilities))],
                    y=[p * 100 for p in probabilities],
                    marker_color=[
                        '#06b6d4' if p == max_confidence else 'rgba(99, 102, 241, 0.25)' 
                        for p in probabilities
                    ],
                    text=[f"{p*100:.1f}%" for p in probabilities],
                    textposition='outside',
                    textfont={'color': '#cbd5e1', 'size': 11}
                )
            ]
        )

        fig.update_layout(
            xaxis_title="",
            yaxis_title="Probability (%)",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#f8fafc', family="Plus Jakarta Sans, Inter"),
            showlegend=False,
            height=300,
            margin=dict(l=20, r=20, t=20, b=40),
            yaxis=dict(gridcolor='rgba(99, 102, 241, 0.15)', zerolinecolor='rgba(99, 102, 241, 0.15)'),
            xaxis=dict(tickfont={'color': '#cbd5e1'})
        )

        st.plotly_chart(fig, width='stretch')
