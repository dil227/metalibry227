import streamlit as st
import random

from streamlit import columns

with st.sidebar:
    st.title("**Metacognition**")
    page = st.radio("How is your energy?",
                    [
                        "Home",
                        "Productivity",
                        "Trivial Decision",
                        "Travel",
                        "Thinking process",
                        "Outcomes",
                        "Therapy",

                    ])

if page == "Home":
    st.title("**Metacognition**")
    st.write("Metacognition is thinking "
             "about our own thinking process")

    with st.container(border= True):
        st.write("Help tips to get the most from this project")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.write("**Productivity: Boost your productivity**")

        with c2:
            st.write("**Trivial Decisions: Leaving it to the chance to decide**")
        with c3:
            st.write("**Travel: Travel checklist etc**")

        c3, c4, c5 = st.columns(3)
        with c3:
            st.write("**Thinking: Map your thinking process**")
        with c4:
            st.write("**Therapy: Distress tolerance therapy for self help**")
        with c5:
            st.write("**Outcomes: Report outcomes**")







if page == "Productivity":
    st.write("Try it! sometimes it is easy "
             "to follow a task "
             "if it is already decided "
             "thus reducing cognitive load")
        # --- Config ---

    POINTS_PER_TASK = 25
    PRAYER_BONUS = 25
    tasks = [
            "Eat x2 ",
            "Code 💻",
            "Hot tub 🛁",
            "Swimming 🏊",
            "Ice cream 🍦",
            "Game",
            "TV 📺",
            "Read 📖",
            "Write ✍️",
            "Drive 🚗",
            "Park 🏞️",
            "Clean 🧹",
            "Cook 🍳",
            "Protein🥩",
            "Skin care💆",
            "Exercise 🏋️",
            "Family/Friends 👨‍👩‍👧"
    ]

        # --- Inputs for today ---
    st.write("Check everything you did today:")
    checks = {t: st.checkbox(t, key=f"task_{t}") for t in tasks}

        # --- Scores ---
    score_daily = sum(checks.values()) * POINTS_PER_TASK
    st.write("### Daily productivity score:", score_daily)
    if score_daily <= 100:
            c1, c2, c3 = st.columns(3)
            with c1:
                st.write("** What activity involves less time and energy?** 🧘")
            with c2:
                st.write("**you dont have to leave  your comfort zone  "
                         " Zone for this one**")
            with c3:
                st.write("**Pair first task with music**")
    elif score_daily <= 200:
            c1, c2, c3 = st.columns(3)
            with c1:
                st.write("**Maybe go out?**")
            with c2:
                st.write("**Do it for the sake of doing it?**")
            with c3:
                st.write("**Today's efforts will bring tomorrow's results**")
    elif score_daily <= 300:
            c1, c2, c3 = st.columns(3)
            with c1:
                st.write("**What do you think is the main driver for "
                         "high level productivity?**")
            with c2:
                st.write("**Sometimes I wonder, if "
                         "I set expectation too high to fail**")
            with c3:
                st.write("**Its not until you fall that "
                         "you fly!**")

    elif score_daily <= 400:
            mood = "Peace"

    st.divider()
    st.title("**for i in tasks"
            " correlate m in mood**")



if page == "Trivial Decision":
    person = st.number_input("How many total variables?",
                             min_value= 1,
                             max_value=15,
                             step=1)

    options = []

    for i in range(person):  # number of options you want
        item = st.text_input(f"Option {i+1}")
        options.append(item)

    if st.button("Decide"):
        if options:
            st.success(random.choice(options))
        else:
            st.warning("Enter at least one option")

    st.divider()
    st.header("Random Suggestions")
    answers = [
            "You can see what they say",
            "If you are asking you probably have one option",
            "Is money a factor?",
            "Is family involved?",
            "Seek Guidance through prayers and patience",
            "Show them your harsh side",
            "cant hear, cant see, cant say",
            "vibes are positive",
            "Get some water",
            "Go driving to clear your mind",
            "Reply professionally",
            "Ask again with different beliefs",
            "Are lies involve?",
            "Epistemic bias",
            "Try writing",
            "Get Ice_cream",
            "Drink Pepsi",
        "Appearences can be deceptive",
        "Remember to turn on the light!",
        "Denial",
        "Go with option B"
    ]

    if st.button("Get suggestion"):
        choice = random.choice(answers)

if page == "Travel":
    with st.container(border=True):
        st.header("**Travel checklist**")
        options = ["passport",
                   "cards",
                   "phone",
                   "Charger",
                   "books",
                   "Laptop",
                   "headphones"]
        st.markdown("Mark everything you have checked")
        for i in options:
            st.checkbox(i)
if page == "Therapy":
    st.title("Distress tolerance therapy")
    with st.container(border= True):
        st.header("step one: Relax")  # REST(R for relax, E for evaluate, S for select action, T for take actions

        thought_1 = st.text_input("What is first thought??", key="t1")
        st.text_input("what is past experience with this thought?", key="p1")
        thought_2 = st.text_input("What is second thought??")
        thought_3 = st.text_input("What is 3rd thought??")
        thought_4 = st.text_input("What is fourth thought??")

        # Display chain
        st.write(
            f"{thought_1} → {thought_2} → {thought_3} → {thought_4}")


    with st.container(border=True):
        st.header("Step Two:Evaluate")
        class Evaluate:
            def __init__(self, options, key):
                self.selected = st.multiselect(
                    "What is your Reasoning process?",
                    options,
                    key=key
                )


        # evaluate thinking error
        distortions = [
            "Black-and-white thinking",
            "It should go my way",
            "IS this a pattern?",
            "Catastrophizing",
            "Discounting the positive",
            "Emotional reasoning",
            "Fortune telling",
            "predicting someone else's nice behaviour",
            "Entitelment",
            "False sense of helplessness- A paradox",
            "False sense of responsibility"
        ]

        errors = Evaluate(distortions, key="errors")

        if "Emotional reasoning" in errors.selected:
            st.write("Distinguish facts from emotions")
            st.write("Try something productive if intensity is high")
        elif "predicting someone else's nice behaviour" in errors.selected:
            st.write("You have met worse")
        elif "Catastropihizing" in errors.selected:
            st.write("You have been through worse")
        elif "Entitelment" in errors.selected:
            st.write("then to him is your return")
        elif "False sense of helplessness" in errors.selected:
            st.write("Seek Guidance through Sbr and Salah!")
        elif "Discounting the positive" in errors.selected:
            st.write("Maybe the Context is wrong")
        elif "Shoulding" in errors.selected:
            st.write("Surrender versus control")


if page == "Thinking process":
    tab_Emotional_Awarness, tab_Motives, tab_intentions,  tab_actions, = st.tabs(
        ["Emotions", "Motives", "Intentions", "Actions"])

    # find out your emotions-----------------
    with tab_Emotional_Awarness:
        st.header("How you feeling?")


        # creating classes
        class Mood:
            def __init__(self, options):
                self.selected = st.multiselect("What do you feel?", options)



        Mood_options = [
            "Happy 😊", "Sad 😢",
            "Great", "Awful",
            "Frustrated","aroused",
            "Drained"
        ]

        mood_1 = Mood(Mood_options)

    with tab_Motives:
        class Motivector:
            def __init__(self, options):
                self.selected = st.multiselect("What are your motives/Beliefs?", options)
        motives = [
            "Gain something",
            "change outcomes",
            "Change myself",
            "Continue current trajectory",
            "Least_time Principle",
            "Pleasure Principle"
            ]
        motives_2 = Motivector(motives)
    with tab_intentions:
        st.write("Loading")


    with tab_actions:
        st.markdown("Refer to productivity")


if page == "Outcomes":
    with st.container(border= True):
        st.write("may use experience vector")

