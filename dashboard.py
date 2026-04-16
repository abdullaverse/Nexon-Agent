import streamlit as st
import pandas as pd
from dns_logic import get_best_server
import time

st.set_page_config(page_title="NEXON AI", layout="wide")

st.title("🧠 NEXON AI CONTROL CENTER")
st.markdown("### 🌐 Network Status: ACTIVE 🟢")

placeholder = st.empty()

while True:
    best_url, best_name, data, predictions, scores,history = get_best_server()

    with placeholder.container():
        col1, col2, col3 = st.columns(3)

        col1.metric("🚀 Server A", f"{data['Server A']} sec")
        col2.metric("⚡ Server B", f"{data['Server B']} sec")
        col3.metric("🧠 Active Server", best_name)

        st.markdown("---")

        # 📊 Graph
        st.subheader("📊 Real-Time Performance")
        chart_data = pd.DataFrame({
            "Server A": [data["Server A"]],
            "Server B": [data["Server B"]]
        })
        st.line_chart(chart_data)

        st.markdown("---")

        # 🔮 Predictions
        st.subheader("🔮 AI Predictions")
        for server, pred in predictions.items():
            if pred:
                st.error(f"{server} may FAIL soon ⚠️")
            else:
                st.success(f"{server} is stable ✅")

        st.markdown("---")

        # 📊 Confidence Score
        st.subheader("📊 AI Confidence Score")
        for server, score in scores.items():
            st.progress(score / 100)
            st.text(f"{server}: {score}%")

        st.markdown("---")

        # Routing status
        if best_name == "Server A":
            st.success("Routing to Server A 🚀")
        else:
            st.warning("Routing to Server B ⚡")

        st.markdown("---")

        st.subheader("📜 Decision Logs")
        st.subheader("🧠 Agent Memory (Latency History)")
        st.json(history)
        st.text(f"Selected: {best_name} | Data: {data}")

    time.sleep(2)