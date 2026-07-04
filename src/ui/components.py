"""
Reusable UI components for the Streamlit application.
"""

import streamlit as st
from typing import Dict, Any, List, Tuple
from ..config import config
from ..test_cases import get_all_test_cases


def render_header():
    """Render the application header section with logos."""
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 4, 1])

    with col1:
        st.image("src/logo/pmgsy-logo.png", width=84)

    with col2:
        st.markdown(f"""
        <div style="padding: 4px 0;">
            <div class="hero-badge">🛣️ &nbsp; AI-Powered · IBM Cloud ML</div>
            <p class="hero-title">{config.APP_TITLE}</p>
            <p class="hero-subtitle">{config.APP_SUBTITLE}</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.image("src/logo/ibm-cloud-logo.png", width=130)

    st.markdown('</div>', unsafe_allow_html=True)


def render_stats(stats: Dict[str, Any], prediction_count: int):
    """
    Render the statistics overview section.

    Args:
        stats: Dictionary with total_records, total_states, total_districts, total_schemes
        prediction_count: Number of predictions made in current session
    """
    st.markdown('<p class="stats-section-label">📊 &nbsp; Dataset Overview</p>', unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <span class="stat-icon">🗂️</span>
            <div class="stat-value">{stats['total_records']:,}</div>
            <div class="stat-label">Records</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <span class="stat-icon">🗺️</span>
            <div class="stat-value">{stats['total_states']}</div>
            <div class="stat-label">States</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <span class="stat-icon">🏙️</span>
            <div class="stat-value">{stats['total_districts']}</div>
            <div class="stat-label">Districts</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="stat-card">
            <span class="stat-icon">📋</span>
            <div class="stat-value">{stats['total_schemes']}</div>
            <div class="stat-label">Schemes</div>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown(f"""
        <div class="stat-card">
            <span class="stat-icon">🔮</span>
            <div class="stat-value accent">{prediction_count}</div>
            <div class="stat-label">Predictions</div>
        </div>
        """, unsafe_allow_html=True)


def render_model_metrics():
    """Render the model performance metrics in an expander."""
    with st.expander("📈  Model Performance Metrics", expanded=False):
        col1, col2, col3 = st.columns(3)
        col1.metric("Accuracy", config.MODEL_ACCURACY)
        col2.metric("Precision", config.MODEL_PRECISION)
        col3.metric("Recall", config.MODEL_RECALL)
        st.caption(f"Trained on {config.TRAINING_RECORDS} records | IBM Cloud ML deployment")


def render_input_form(states: List[str], get_districts_fn) -> Dict[str, Any]:
    """
    Render the project input form with test case auto-fill buttons.
    
    Args:
        states: List of available states
        get_districts_fn: Function to get districts for a state
        
    Returns:
        Dictionary with all form values
    """
    st.markdown('<p class="section-title">📝 &nbsp; Project Details</p>', unsafe_allow_html=True)
    
    # Test case buttons
    st.markdown("""
        <div class="quickfill-banner">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 17px;">⚡</span>
                <span class="quickfill-title">Quick Fill &mdash; All 5 PMGSY Schemes</span>
            </div>
            <p class="quickfill-desc">Click any scheme button below to auto-fill the form with representative sample data (PMGSY I, II, III, RCPLWEA, PM-JANMAN).</p>
        </div>
    """, unsafe_allow_html=True)
    
    test_cases = get_all_test_cases()
    
    # Display test case buttons in two rows for better layout
    st.markdown('<div style="display: flex; flex-direction: column; gap: 8px;">', unsafe_allow_html=True)
    
    # First row: Test cases
    cols1 = st.columns(len(test_cases))
    for idx, test_case in enumerate(test_cases):
        with cols1[idx]:
            # Extract just the scheme name from full name
            display_name = test_case['name'].split(' ', 1)[1] if ' ' in test_case['name'] else test_case['name']
            if st.button(
                f"{test_case['icon']} {display_name}", 
                key=f"test_{idx}",
                help=f"Load sample data for {test_case['scheme']}",
                type="secondary"
            ):
                # Set each value directly in session state
                data = test_case['data']
                for key, value in data.items():
                    st.session_state[f"input_{key}"] = value
                st.rerun()
    
    # Second row: Clear button (centered)
    col_space1, col_clear, col_space2 = st.columns([2, 1, 2])
    with col_clear:
        if st.button("🗑️ Clear All", key="clear_form", help="Clear all form values", type="secondary"):
            # Clear all input fields
            keys_to_clear = ['state', 'district', 'road_sanctioned', 'length_sanctioned', 
                           'bridges_sanctioned', 'cost_sanctioned', 'road_completed', 
                           'length_completed', 'bridges_completed', 'expenditure', 
                           'road_balance', 'length_balance', 'bridges_balance']
            for key in keys_to_clear:
                if f"input_{key}" in st.session_state:
                    del st.session_state[f"input_{key}"]
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Location selection
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown('<p class="form-group-title">📍 Location</p>', unsafe_allow_html=True)
    
    loc_col1, loc_col2 = st.columns(2)
    
    with loc_col1:
        default_state_idx = 0
        if 'input_state' in st.session_state and st.session_state['input_state'] in states:
            default_state_idx = states.index(st.session_state['input_state'])
        
        selected_state = st.selectbox(
            "State",
            options=states,
            index=default_state_idx,
            help="Select the state where the project is located"
        )
    
    districts = get_districts_fn(selected_state)
    
    with loc_col2:
        default_district_idx = 0
        if 'input_district' in st.session_state and st.session_state['input_district'] in districts:
            default_district_idx = districts.index(st.session_state['input_district'])
        
        selected_district = st.selectbox(
            "District",
            options=districts,
            index=default_district_idx,
            help="Select the district within the chosen state"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Sanctioned works
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown('<p class="form-group-title">📋 Sanctioned Works</p>', unsafe_allow_html=True)
    
    sanct_col1, sanct_col2, sanct_col3, sanct_col4 = st.columns(4)
    
    with sanct_col1:
        road_sanctioned = st.number_input(
            "No. of Roads",
            min_value=0,
            value=st.session_state.get('input_road_sanctioned', 0),
            help="Total number of road works sanctioned"
        )
    
    with sanct_col2:
        length_sanctioned = st.number_input(
            "Road Length (km)",
            min_value=0.0,
            value=float(st.session_state.get('input_length_sanctioned', 0.0)),
            format="%.2f",
            help="Total length of road work sanctioned in kilometers"
        )
    
    with sanct_col3:
        bridges_sanctioned = st.number_input(
            "No. of Bridges",
            min_value=0,
            value=st.session_state.get('input_bridges_sanctioned', 0),
            help="Number of bridges sanctioned"
        )
    
    with sanct_col4:
        cost_sanctioned = st.number_input(
            "Cost (₹ Crore)",
            min_value=0.0,
            value=float(st.session_state.get('input_cost_sanctioned', 0.0)),
            format="%.2f",
            help="Total cost of works sanctioned in Crore"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Completed works
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown('<p class="form-group-title">✅ Completed Works</p>', unsafe_allow_html=True)
    
    comp_col1, comp_col2, comp_col3, comp_col4 = st.columns(4)
    
    with comp_col1:
        road_completed = st.number_input(
            "No. of Roads Completed",
            min_value=0,
            value=st.session_state.get('input_road_completed', 0),
            help="Number of road works completed"
        )
    
    with comp_col2:
        length_completed = st.number_input(
            "Road Length Completed (km)",
            min_value=0.0,
            value=float(st.session_state.get('input_length_completed', 0.0)),
            format="%.2f",
            help="Total length of road work completed in kilometers"
        )
    
    with comp_col3:
        bridges_completed = st.number_input(
            "No. of Bridges Completed",
            min_value=0,
            value=st.session_state.get('input_bridges_completed', 0),
            help="Number of bridges completed"
        )
    
    with comp_col4:
        expenditure = st.number_input(
            "Expenditure (₹ Crore)",
            min_value=0.0,
            value=float(st.session_state.get('input_expenditure', 0.0)),
            format="%.2f",
            help="Total expenditure occurred in Crore"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Balance works
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown('<p class="form-group-title">⏳ Balance Works</p>', unsafe_allow_html=True)
    
    bal_col1, bal_col2, bal_col3 = st.columns(3)
    
    with bal_col1:
        road_balance = st.number_input(
            "No. of Roads Balance",
            min_value=0,
            value=st.session_state.get('input_road_balance', 0),
            help="Number of road works pending"
        )
    
    with bal_col2:
        length_balance = st.number_input(
            "Road Length Balance (km)",
            min_value=0.0,
            value=float(st.session_state.get('input_length_balance', 0.0)),
            format="%.2f",
            help="Total length of road work pending in kilometers"
        )
    
    with bal_col3:
        bridges_balance = st.number_input(
            "No. of Bridges Balance",
            min_value=0,
            value=st.session_state.get('input_bridges_balance', 0),
            help="Number of bridges pending"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    return {
        "state": selected_state,
        "district": selected_district,
        "road_sanctioned": road_sanctioned,
        "length_sanctioned": length_sanctioned,
        "bridges_sanctioned": bridges_sanctioned,
        "cost_sanctioned": cost_sanctioned,
        "road_completed": road_completed,
        "length_completed": length_completed,
        "bridges_completed": bridges_completed,
        "expenditure": expenditure,
        "road_balance": road_balance,
        "length_balance": length_balance,
        "bridges_balance": bridges_balance
    }


def render_result(prediction: str, confidence: float, conf_class: str):
    """
    Render the prediction result card.

    Args:
        prediction: The predicted scheme name
        confidence: Confidence percentage (0-100)
        conf_class: CSS class for confidence badge
    """
    st.markdown('<p class="section-title">🎯 &nbsp; Prediction Result</p>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="result-card">
        <p class="result-eyebrow">Predicted PMGSY Scheme</p>
        <h2 class="result-scheme-name">{prediction}</h2>
        <span class="confidence-badge {conf_class}">{confidence:.1f}% Confidence</span>
    </div>
    """, unsafe_allow_html=True)


def render_dataset_insights(data_loader):
    """Render a visual analytics dashboard of the PMGSY dataset."""
    with st.expander("📊 Dataset Insights & Distribution Dashboard", expanded=False):
        df = data_loader.df
        
        # 2 columns for side-by-side analysis
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<p style="font-weight:600; font-size:14px; margin-bottom:8px; color:var(--color-text-primary);">Top 10 States by Project Count</p>', unsafe_allow_html=True)
            # Calculate top states
            top_states = df['STATE_NAME'].value_counts().head(10).reset_index()
            top_states.columns = ['State', 'Count']
            
            import plotly.express as px
            fig_states = px.bar(
                top_states,
                x='Count',
                y='State',
                orientation='h',
                color='Count',
                color_continuous_scale='Purples',
            )
            fig_states.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cbd5e1', family="Plus Jakarta Sans, Inter"),
                margin=dict(l=10, r=10, t=10, b=10),
                height=260,
                xaxis=dict(gridcolor='rgba(99, 102, 241, 0.1)'),
                yaxis=dict(autorange="reversed"),
                coloraxis_showscale=False
            )
            st.plotly_chart(fig_states, width='stretch')
            
        with col2:
            st.markdown('<p style="font-weight:600; font-size:14px; margin-bottom:8px; color:var(--color-text-primary);">PMGSY Scheme Type Distribution</p>', unsafe_allow_html=True)
            # Calculate scheme distribution
            scheme_counts = df['PMGSY_SCHEME'].value_counts().reset_index()
            scheme_counts.columns = ['Scheme', 'Count']
            
            import plotly.express as px
            fig_schemes = px.pie(
                scheme_counts,
                values='Count',
                names='Scheme',
                hole=0.4,
                color_discrete_sequence=px.colors.sequential.Purples_r
            )
            fig_schemes.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cbd5e1', family="Plus Jakarta Sans, Inter"),
                margin=dict(l=10, r=10, t=10, b=10),
                height=260,
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
            )
            st.plotly_chart(fig_schemes, width='stretch')
