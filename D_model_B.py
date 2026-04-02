import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

st.set_page_config(page_title="13 State Lorenz Decision Model", layout="wide")

st.title("13 State Motives Based Decision Model")
st.write("Answers to your questions set the Lorenz dynamics, and the trajectory is classified into one of your 13 states.")

# -----------------------------
# YOUR 13 STATES
# -----------------------------
STATE_NAMES = [
    "1. Depression",
    "2. Illusion",
    "3. Vision Cycle",
    "4. Reason / Hope",
    "5. Fear",
    "6. Pleasure",
    "7. Problems",
    "8. Loneliness",
    "9. Anxiety",
    "10. Family / Connection",
    "11. Grief",
    "12. Instability",
    "13. Chaos"
]

# -----------------------------
# HELPERS
# -----------------------------
def scale_to_range(value, old_min, old_max, new_min, new_max):
    return new_min + (value - old_min) * (new_max - new_min) / (old_max - old_min)

def normalize_last_window(arr, window=300):
    arr = arr[-window:]
    a_min = np.min(arr)
    a_max = np.max(arr)
    if a_max - a_min == 0:
        return np.full_like(arr, 50.0)
    return 100 * (arr - a_min) / (a_max - a_min)

# -----------------------------
# MAP ANSWERS TO NUMBERS
# -----------------------------
motive_map = {
    "Physical": 12,
    "Belonging": 8,
    "Self actualization": 16,
    "Gain something": 10,
    "Change outcomes": 14,
    "Change myself": 15,
    "Continue current trajectory": 6,
}

intention_map = {
    "+": 8,
    "-": -8,
    "Optional": 3,
    "MustChoose": 10,
    "Time may tell": 1,
}

choice_map = {
    "Prayers": 8,
    "Code": 7,
    "Swimming": 8,
    "Read": 6,
    "Write": 6,
    "Drive": 4,
    "Park": 5,
    "Clean": 5,
    "Cook": 5,
    "Quran": 8,
    "Exercise": 9,
    "Family/Friends": 7,
    "Sleep": 4,
    "Work": 6,
    "TV": 2,
    "Game": 2,
    "Ice cream": 1,
    "Sex": 3,
    "THC": -5,
    "ETOH": -6,
}

# -----------------------------
# LORENZ
# -----------------------------
def lorenz_step(x, y, z, sigma, rho, beta, dt):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return x + dx * dt, y + dy * dt, z + dz * dt

def run_lorenz(sigma, rho, beta, steps=2500, dt=0.01, x0=0.1, y0=1.0, z0=1.05):
    xs = np.zeros(steps)
    ys = np.zeros(steps)
    zs = np.zeros(steps)

    xs[0], ys[0], zs[0] = x0, y0, z0

    for i in range(1, steps):
        xs[i], ys[i], zs[i] = lorenz_step(xs[i-1], ys[i-1], zs[i-1], sigma, rho, beta, dt)

    return xs, ys, zs

# -----------------------------
# CLASSIFY ONE MOMENT INTO 13 STATES
# -----------------------------
def identify_state(en, ent, info, striv, motive_score, intention_score, choice_score):
    drive = striv + max(motive_score, 0) * 0.8 + max(intention_score, 0) * 1.2
    burden = ent + abs(min(choice_score, 0)) * 3
    support = info + max(choice_score, 0) * 2

    if burden > 85 and en < 35:
        return "1. Depression"
    elif info < 35 and ent > 60 and intention_score <= 3:
        return "2. Illusion"
    elif info > 70 and drive > 80 and ent < 55:
        return "3. Vision Cycle"
    elif info > 60 and ent < 45 and choice_score >= 0:
        return "4. Reason / Hope"
    elif ent > 70 and en > 40 and drive > 45:
        return "5. Fear"
    elif en > 70 and ent < 40 and support > 55:
        return "6. Pleasure"
    elif ent > 55 and info > 45 and drive > 35:
        return "7. Problems"
    elif en < 35 and drive < 45 and motive_score <= 10:
        return "8. Loneliness"
    elif ent > 75 and drive > 70:
        return "9. Anxiety"
    elif motive_score >= 8 and choice_score >= 5 and info > 45 and striv > 50:
        return "10. Family / Connection"
    elif en < 45 and ent > 70 and info < 50:
        return "11. Grief"
    elif 40 <= en <= 65 and 45 <= ent <= 70 and 35 <= info <= 65:
        return "12. Instability"
    elif ent > 85 or (ent > 70 and info < 30 and drive > 60):
        return "13. Chaos"
    else:
        return "12. Instability"

# -----------------------------
# UI
# -----------------------------
left, right = st.columns([1, 1])

with left:
    st.subheader("Core Questions")
    energy = st.slider("Energy", 0, 100, 60)
    entropy = st.slider("Entropy", 0, 100, 45)
    information = st.slider("Information", 0, 100, 55)
    striving = st.slider("Striving", 0, 100, 65)
    time_pressure = st.slider("Time pressure", 0, 100, 40)

    st.subheader("Motives")
    motives_1 = st.multiselect(
        "What are your motives?",
        ["Physical", "Belonging", "Self actualization"]
    )
    motives_2 = st.multiselect(
        "What is the direction of your motive?",
        ["Gain something", "Change outcomes", "Change myself", "Continue current trajectory"]
    )

with right:
    st.subheader("Intentions and Choices")
    intentions_1 = st.multiselect("Intentions", ["+", "-"])
    intentions_2 = st.multiselect("Intensity", ["Optional", "MustChoose", "Time may tell"])
    choices = st.multiselect(
        "Choices / Actions",
        [
            "Prayers", "Code", "Swimming", "Read", "Write", "Drive", "Park",
            "Clean", "Cook", "Quran", "Exercise", "Family/Friends",
            "Sleep", "Work", "TV", "Game", "Ice cream", "Sex", "THC", "ETOH"
        ]
    )

    steps = st.slider("Simulation steps", 1000, 5000, 2500, 100)
    dt = st.slider("dt", 0.001, 0.03, 0.01, 0.001)

# -----------------------------
# SCORES
# -----------------------------
motive_score = sum(motive_map.get(x, 0) for x in motives_1 + motives_2)
intention_score = sum(intention_map.get(x, 0) for x in intentions_1 + intentions_2)
choice_score = sum(choice_map.get(x, 0) for x in choices)

# Lorenz parameter mapping
sigma = scale_to_range(energy + 0.5 * striving + 0.2 * motive_score, 0, 130, 5, 18)
rho = scale_to_range(entropy + 0.4 * time_pressure + max(-choice_score, 0), 0, 160, 10, 40)
beta = scale_to_range(information + 0.3 * max(choice_score, 0) + 0.2 * max(intention_score, 0), 0, 140, 1.5, 6)

# initial conditions
x0 = scale_to_range(energy, 0, 100, -10, 10)
y0 = scale_to_range(striving + intention_score, -20, 120, -15, 15)
z0 = scale_to_range(information - entropy, -100, 100, 5, 35)

# -----------------------------
# RUN
# -----------------------------
if st.button("Run 13-State Model"):
    xs, ys, zs = run_lorenz(sigma, rho, beta, steps=steps, dt=dt, x0=x0, y0=y0, z0=z0)

    x_norm = normalize_last_window(xs)
    y_norm = normalize_last_window(ys)
    z_norm = normalize_last_window(zs)

    state_trace = []
    for i in range(len(x_norm)):
        en_t = x_norm[i]
        ent_t = z_norm[i]
        info_t = y_norm[i]

        state = identify_state(
            en_t,
            ent_t,
            info_t,
            striving,
            motive_score,
            intention_score,
            choice_score
        )
        state_trace.append(state)

    counts = Counter(state_trace)
    dominant_state = counts.most_common(1)[0][0]
    recent_state = state_trace[-1]

    st.markdown("---")
    st.subheader("Results")

    c1, c2, c3 = st.columns(3)
    c1.metric("Dominant State", dominant_state)
    c2.metric("Final State", recent_state)
    c3.metric("Unique States Visited", len(counts))

    st.write("### Lorenz Parameters")
    st.write(f"Sigma (Energy-like): **{sigma:.2f}**")
    st.write(f"Rho (Entropy-like): **{rho:.2f}**")
    st.write(f"Beta (Information-like): **{beta:.2f}**")

    st.write("### State Counts")
    for state_name in STATE_NAMES:
        st.write(f"{state_name}: {counts.get(state_name, 0)}")

    # 2D Lorenz plot
    fig1, ax1 = plt.subplots()
    ax1.plot(xs, zs, linewidth=0.7)
    ax1.set_title("Lorenz Projection (x vs z)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("z")
    st.pyplot(fig1)

    # Time series
    fig2, ax2 = plt.subplots()
    ax2.plot(x_norm, label="Energy-like")
    ax2.plot(y_norm, label="Information-like")
    ax2.plot(z_norm, label="Entropy-like")
    ax2.set_title("Normalized Trajectory")
    ax2.set_xlabel("Time step")
    ax2.set_ylabel("0-100 scale")
    ax2.legend()
    st.pyplot(fig2)

    # Last 30 states
    st.write("### Recent State Path")
    st.write(" → ".join(state_trace[-30:]))

    # Interpretation
    st.write("### Interpretation")
    if dominant_state == "13. Chaos":
        st.warning("Your current answers generate a highly unstable pattern. Entropy and pressure are overpowering clarity.")
    elif dominant_state == "3. Vision Cycle":
        st.success("Your current answers generate organized movement with forward orientation.")
    elif dominant_state == "4. Reason / Hope":
        st.success("Information is narrowing the chaos and supporting stable direction.")
    elif dominant_state == "9. Anxiety":
        st.warning("High drive under high entropy is producing anxious looping.")
    elif dominant_state == "1. Depression":
        st.warning("Low energy under heavy entropy is collapsing the system into depression-like dynamics.")
    else:
        st.info("Your answers produce a mixed attractor pattern rather than a single fixed state.")

else:
    st.info("Set the inputs, then click Run 13-State Model.")