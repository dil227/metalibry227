import random
import streamlit as st

# ============================================================
# GLOBAL DATA
# ============================================================

BINARY_ANS = ["yes", "No"]
POINTS_PER_TASK = 25





def show():
    st.caption("Find your meaning?")

    tab_event, tab_goal, tab_emotions, tab_activities = st.tabs(
        ["Current State", "Current Behaviour", "Emotions", "Activities"]
    )

    # ---------------- EVENTS ----------------
    with tab_event:
        intensity = [
            "if intensity=Non-Stimulating: I don't wanna do anything",
            "elif intensity=Activating: I wanna do something",
            "elif intensity=Very Intense: I wanna do EVERYTHING",
            "else intensity=Overwhelming: system.overload()",
        ]

        emotional_valence = [
            "if Mood=Sad: I can survive",
            "elif Emotion=Happy: I want more of this",
            "elif Feeling=Great: I don't want anything else",
            "elif Feeling=Awful: system.escape()",
            "else Feeling=Peaceful: absence_of_boredom = True",
        ]

        expectations = [
            "if intentions=Connection: Make a meaningful connection",
            "elif finding=meaning: Life's beauty lies in its impermanence",
            "elif blue=Time_Pass: Tomorrow it will be a bad dream?",
            "elif Reframe: Try looking from a different perspective",
            "else Escape: Get out of here",
        ]

        class DeltaExperience:
            def choose(self, label, options, key):
                return st.radio(label, options, key=key)

            def has_choice(self, selected_options, keyword):
                return any(
                    keyword.lower() in option.lower()
                    for option in selected_options
                )

        e = DeltaExperience()

        selected_intensity = e.choose(
            "What is the intensity (ψ)?",
            intensity,
            "forloop_intensity",
        )
        selected_emotion = e.choose(
            "How would you characterize this feeling (θ)?",
            emotional_valence,
            "forloop_emotion",
        )
        selected_expectation = e.choose(
            "What follows this experience (σ)?",
            expectations,
            "forloop_expectation",
        )

        with st.container(border=True):
            if e.has_choice(selected_intensity, "Overwhelming"):
                st.write(
                    "The future unveils the true weight of choices "
                    "that distraction concealed"
                )
            elif e.has_choice(selected_intensity, "Very Intense"):
                st.write(
                    "Repeated preferences shape final orientation; "
                    "the future grows from what the heart consistently chooses"
                )
            elif e.has_choice(selected_intensity, "Activating"):
                st.write(
                    "Self certainty is not a sign of right orientation"
                )
            elif e.has_choice(selected_intensity, "Non-Stimulating"):
                st.write(
                    "Existence is directed: not merely occurring"
                )

            if e.has_choice(selected_emotion, "Sad"):
                st.write("For sadness, choose prayer.")
            elif e.has_choice(selected_emotion, "Awful"):
                st.write("For awful emotions, slow down and breathe.")
            elif e.has_choice(selected_emotion, "Great"):
                st.write("For great emotions, practice gratitude.")
            elif e.has_choice(selected_emotion, "Peaceful"):
                st.write("For peaceful emotions, choose a quiet place.")
            elif e.has_choice(selected_emotion, "Happy"):
                st.write("For happiness, choose a place to relax.")
            elif selected_emotion:
                st.write("For unknown emotions, choose a quiet place.")



    # ---------------- THOUGHTS ----------------
    with tab_goal:
        with st.container(border=True):
            st.header("STEP 2:Gain behavioral control")

            st.write("Basic Principle: "
                "Belief → Meaning → Value  → "
                "Choices → Actions → "
            )

            belief = st.radio(
                "choose one to act on",["Learn mindfulness", "distress tolerance ",
                "emotion regulation","interpersonal effectiveness."]

            )

            meaning = st.radio(
                "2. What makes that belief meaningful?",
                ["I want to be happy", "I want to be successful", "I want to be free"],
                key="goal_meaning",
            )

            value_categories = [
                "Career and contribution",
                "Family and relationships",
                "Safety and security",
                "Personal growth",
                "Leisure and creativity",
                "Faith and relationship with God",
                "Service to others",
                "Health and well-being",
            ]

            selected_values = st.radio(
                "3. What becomes valuable because of this meaning?",
                value_categories,
                key="goal_values",
            )

            custom_value = st.text_input(
                "Add a value not listed above",
                key="custom_goal_value",
            )

            focus_options = [
                "Something I can act on now",
                "Something I can prepare for",
                "Something I need to understand better",
                "Something outside my control",
                "Something I may need to release",
            ]

            attention_goal = st.radio(
                " Where should your attention go right now?",
                focus_options,
                key="goal_attention",
            )

            st.divider()
            st.markdown(
                """
- **11:49** — Be patient; the outcome belongs to the righteous.
- **11:88** — Reform according to your ability while relying on Allah.
- **11:112–115** — Be steadfast, establish prayer, do good, and be patient.
- **11:123** — Worship Allah and trust Him.
- **12:5–6** — Exercise wisdom and trust Allah's plan.
- **12:18** — Practice beautiful patience.
- **12:23** — Seek Allah's protection from temptation.
- **12:33** — Choose righteousness over comfort.
- **13:11** — Change begins within ourselves.
"""
            )


    st.markdown("""
    <style>
    .hero {
        background: linear-gradient(136deg, #1f2837, #111927, #0f766e);
        padding: 1.2rem 1.4rem;
        border-radius: 16px;
        color: #f10fafb;
        box-shadow: 0 8px 24px rgba(0,0,0,.18);
        margin-bottom: 1rem;
    }
    .hero h1 { margin: 0; font-size: 1.6rem; }
    .hero p { margin: .35rem 0 0; opacity: .9; }
    </style>
    <div class="hero">
      <h1>🧠 Roman</h1>
      <p>Iterative cognitive agent — structured reasoning with transparent process</p>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- EMOTIONS ----------------
    with tab_emotions:
        st.header("Deeper Emotional Evaluation")

        mood_options = [
            "Happy",
            "Sad",
            "Great",
            "Awful",
            "Frustrated",
            "Motivated",
            "Drained",
            "Free",
            "Peace",
        ]

        moods = st.pills(
            "What do you feel?",
            mood_options,
            key="moods",
        )

        preceding_events = [
            "Something did not go as expected",
            "Something unfair",
            "Something unpleasant",
            "I don't know",
            "Something as expected",
        ]

        events = st.pills(
            "What happened?",
            preceding_events,
            key="preceding_events",
        )

        motives = [
            "Gain something",
            "Change outcomes",
            "Change myself",
            "Continue current trajectory",
            "Pleasure principle",
            "Serotonin",
        ]

        selected_motives = st.pills(
            "What are your motives?",
            motives,
            key="motives",
        )

        distortions = [
            "Black-and-white thinking",
            "It should go my way",
            "Is this a pattern?",
            "Catastrophizing",
            "Discounting the positive",
            "Emotional reasoning",
            "Fortune telling",
            "Predicting someone else's nice behaviour",
            "Entitlement",
            "False sense of helplessness - A paradox",
            "False sense of responsibility",
        ]

        with st.container(border=True):
            errors = st.radio(
                "What is the reasoning process?",
                distortions,
                key="errors",
            )

            responses = {
                "Emotional reasoning": [
                    "11:49 – Be patient; the outcome belongs to the righteous.",
                    "11:88 – Reform according to your ability while relying on Allah.",
                ],
                "Predicting someone else's nice behaviour": [
                    "11:123 – Worship Allah and trust Him.",
                ],
                "Catastrophizing": [
                    "You have been through worse. Exercise wisdom and trust the plan.",
                ],
                "Entitlement": [
                    "Then to Him is your return.",
                ],
                "False sense of helplessness - A paradox": [
                    "Seek guidance through Sabr and Salah.",
                ],
                "Discounting the positive": [
                    "Maybe the context is wrong.",
                ],
                "It should go my way": [
                    "Ultimately, God's will prevails.",
                ],
            }

            for error in errors:
                for response in responses.get(error, []):
                    st.write(response)
            # Paste this right after st.set_page_config(...)

            st.markdown("""
            <style>
            :root{
              --bg1:#0b1020;
              --bg2:#111827;
              --bg3:#1f2937;
              --card:#111827cc;
              --stroke:#334155;
              --text:#e5e7eb;
              --muted:#94a3b8;
              --accent:#22d3ee;
              --accent2:#8b5cf6;
            }

            /* App background */
            .stApp {
              background: radial-gradient(1200px 500px at 15% -10%, #1d4ed8 0%, transparent 50%),
                          radial-gradient(900px 500px at 100% 0%, #7c3aed 0%, transparent 45%),
                          linear-gradient(135deg, var(--bg1), var(--bg2), var(--bg3));
              color: var(--text);
            }

            /* Main content */
            .block-container {
              max-width: 980px;
              padding-top: 1.2rem;
              padding-bottom: 2.5rem;
            }

            /* Glass containers */
            div[data-testid="stVerticalBlockBorderWrapper"]{
              background: var(--card);
              border: 1px solid var(--stroke);
              border-radius: 16px;
              box-shadow: 0 10px 30px rgba(0,0,0,.25);
            }

            /* Typography */
            h1, h2, h3 { color: #f8fafc !important; letter-spacing: -0.02em; }
            p, .stMarkdown, .stCaption { color: var(--text) !important; }

            /* Tabs */
            .stTabs [data-baseweb="tab-list"] { gap: .5rem; }
            .stTabs [data-baseweb="tab"]{
              border-radius: 999px;
              padding: .5rem .85rem;
              background: #0f172a;
              border: 1px solid #1e293b;
            }
            .stTabs [aria-selected="true"]{
              background: linear-gradient(90deg, var(--accent), var(--accent2));
              color: #0b1020 !important;
              font-weight: 700;
            }

            /* Inputs / buttons */
            .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"]{
              background: #0f172a !important;
              color: #e2e8f0 !important;
              border: 1px solid #334155 !important;
            }
            .stButton > button{
              border-radius: 10px;
              border: 1px solid #334155;
              background: linear-gradient(90deg, #0ea5e9, #8b5cf6);
              color: white;
              font-weight: 600;
            }

            /* Chat bubble polish */
            [data-testid="stChatMessage"]{
              border: 1px solid #334155;
              border-radius: 14px;
              background: #0b1226aa;
            }

            /* Sidebar */
            section[data-testid="stSidebar"] .block-container{
              background: #0b1226aa;
              border-left: 1px solid #334155;
            }
            </style>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="
              padding: 1rem 1.1rem;
              border-radius: 16px;
              border: 1px solid #334155;
              background: linear-gradient(135deg, rgba(34,211,238,.2), rgba(139,92,246,.2));
              margin-bottom: .8rem;">
              <div style="font-size:1.35rem;font-weight:700;color:#f8fafc;">🧠 Roman</div>
              <div style="color:#cbd5e1;">Iterative cognitive agent — transparent reasoning loop</div>
            </div>
            """, unsafe_allow_html=True)

            def ui_badge(text: str, color: str = "#22d3ee") -> None:
                st.markdown(
                    f"""
                    <span style="
                        display:inline-block;
                        margin:.1rem .35rem .2rem 0;
                        padding:.24rem .58rem;
                        border-radius:999px;
                        font-size:.78rem;
                        font-weight:700;
                        color:#0b1020;
                        background:{color};">{text}</span>
                    """,
                    unsafe_allow_html=True,
                )

            def ui_kpi_row(action: str, top_signal: str, confidence: float) -> None:
                st.markdown(f"""
                <div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.55rem;margin:.4rem 0 .8rem 0;">
                  <div style="border:1px solid #334155;border-radius:12px;padding:.6rem .7rem;background:#0f172a;">
                    <div style="font-size:.75rem;color:#94a3b8;">Action</div>
                    <div style="font-size:1rem;font-weight:700;color:#e2e8f0;">{action}</div>
                  </div>
                  <div style="border:1px solid #334155;border-radius:12px;padding:.6rem .7rem;background:#0f172a;">
                    <div style="font-size:.75rem;color:#94a3b8;">Top Signal</div>
                    <div style="font-size:1rem;font-weight:700;color:#e2e8f0;">{top_signal}</div>
                  </div>
                  <div style="border:1px solid #334155;border-radius:12px;padding:.6rem .7rem;background:#0f172a;">
                    <div style="font-size:.75rem;color:#94a3b8;">Confidence</div>
                    <div style="font-size:1rem;font-weight:700;color:#e2e8f0;">{confidence:.2f}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)


    # ---------------- ACTIVITIES ----------------
    with tab_activities:
        st.write(
            "Optional or Rhetorical"
        )

        task_groups = {
            "{Passion} ":["Studying",
                          "Reading medicine",
                          "Listening to a podcast",
                          "A vedio"],


            " {Leisure} ": [
                "Hot tub 🛁", "Swimming 🏊", "Game", "TV 📺", "Read 📖",
                "Coding 💻", "Write ✍️", "Drive 🚗", "Park 🏞️", "Piano", "Weights","N"
            ],
            "{faith}" : [
                "Praying", "Reading Quran", "Supplication", "Dhikr",
                "Listening to a podcast", "Listening to Quran",
                "Generosity", "Tawakkul","Reading Bible","N",

            ],
            " {self-care} ": [
                "Clean 🧹", "Cook 🍳", "Protein 🥩",
                "Skin care 💆", "Exercise 🏋️", "N"
            ],
            "{Connection}": ["Family", "Friends","Colleagues"],
        }

        selected_tasks = {}

        selected_tasks = {}

        for group_name, tasks in task_groups.items():
            selected_tasks[group_name] = st.pills(
                group_name,
                tasks,
                selection_mode="multi",
                key=f"activities_{group_name.lower()}",
            ) or []

        completed_tasks = sum(len(selected) for selected in selected_tasks.values())
        score_daily = completed_tasks * POINTS_PER_TASK
        if score_daily ==100:
            st.write("Consistency or initiative")
        elif score_daily == 150:
            st.write("Self-discipline or self-control:"
                     " Humankind is the most argumentative of beings.")
        elif score_daily == 175:
            st.write("Self-confidence or self-worth:"
                     "In hardship people call on God, then turn away after rescue.")
        elif score_daily == 200:
            st.write("Striving or surviving?")
        elif score_daily == 300:
            st.write("Discipline or motivation?")
        elif score_daily == 400:
            st.write("Instant gratification or long-term pursue?")
        else:
            st.write("score_daily >= 500.")

        st.metric("Daily productivity score", score_daily)
        st.caption(
                f"{completed_tasks} activities completed × "
                f"{POINTS_PER_TASK} points"
            )

    st.markdown("""
    <style>
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0,1fr));
      gap: .6rem;
    }
    .kpi {
      border: 1px solid #e5e7eb;
      border-radius: 12px;
      padding: .65rem .75rem;
      background: #fafafa;
    }
    .kpi .label { font-size: .78rem; color: #6b7280; }
    .kpi .value { font-size: 1rem; font-weight: 700; color: #111827; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="kpi-grid">
      <div class="kpi"><div class="label">Action</div><div class="value">OBSERVE</div></div>
      <div class="kpi"><div class="label">Top Signal</div><div class="value">uncertainty</div></div>
      <div class="kpi"><div class="label">Confidence</div><div class="value">0.80</div></div>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    show()

