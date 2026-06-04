import streamlit as st
import random

from streamlit import columns
#data
binary_ans = ["yes","No"]
with st.sidebar:
    st.title("**Metacognition**")
    page = st.radio("Menu?",
                    [
                        "Home",
                        "Decision Model",
                        "Travel",
                        "Thinking loop",
                        "Outcomes",
                        "Human Interaction guide"


                    ])

if page == "Home":
    st.title("**Metacognition**")
    st.write("Metacognition is thinking "
             "about our own thinking process")

    with st.container(border= True):
        st.write("Help tips to get the most from this project")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.write("**Human interaction guide: helps you decide "
                     "how to deal with people based on "
                     "how you see them**")

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







if page == "Decision Model":
    tab_longterm, tab_shortterm = st.tabs(["Long term", "Short term"])
    with tab_longterm:
        st.title("Decision Making Checklist (For long-term decision")

        questions = [
            "What outcome am I trying to maximize, and is it clearly defined?",
            "What do I assume other people involved will do in response to my choice?",
            "What happens to my outcome if others act strategically against me?",
            "Do I have a dominant strategy that works best regardless of others’ actions?",
            "Is this situation competitive (zero-sum) or can both sides benefit (non-zero-sum)?",
            "Is there a way to cooperate that improves outcomes for everyone involved?",
            "What information do I have that others don’t, and what might I be missing?",
            "How would my decision change if I knew the other person’s decision in advance?",
            "Am I considering only immediate payoff, or also long-term strategic consequences?",
            "If everyone acted rationally in this situation, what equilibrium outcome would emerge?"
        ]

        responses = {}

        for i, q in enumerate(questions):
            responses[i] = st.text_input(f"Q{i + 1}: {q}", key=f"q{i}")

        if st.button("Submit"):
            st.write("### Your Responses")
            st.json(responses)
    st.divider()




    with tab_shortterm:
        st.header("Decision Utility Tracker")

        decision_name = st.text_input("Decision Name")
        expected_utility = st.text_input("What do you expect from this decision?")

        choice_1 = st.text_input("Choice 1")
        choice_2 = st.text_input("Choice 2")
        choice_3 = st.text_input("Choice 3")

        final_choice = st.text_input("Final Choice")

        utility_function = st.select_slider(
            "How close are outcomes to expected utility?",
            options=["Very far", "Far", "Neutral", "Close", "Very close"]
        )

        st.write(f"""
        Decision Name: {decision_name}

        Expected Utility: {expected_utility}

        Choice 1: {choice_1}

        Choice 2: {choice_2}

        Choice 3: {choice_3}

        Final Choice: {final_choice}

        Utility Function: {utility_function}
        """)


        person = st.number_input("How many total variables?",
                                 min_value=1,
                                 max_value=15,
                                 step=1)

        options = []

        for i in range(person):  # number of options you want
            item = st.text_input(f"Option {i + 1}")
            options.append(item)

        if st.button("Decide"):
            if options:
                st.success(random.choice(options))
            else:
                st.warning("Enter at least one option")

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
            st.write(choice)

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



#----------------------------


if page == "Thinking loop":
    tab_MoodMotivesChoices,  tab_thinkingError, = st.tabs(["Mood Motives choices","Thinking Err"])

    # find out your emotions-----------------
    with tab_MoodMotivesChoices:
        st.header("Emotional Evaluation?")

        Mood_options = [
            "Happy 😊", "Sad 😢",
            "Great", "Awful",
            "Frustrated","aroused",
            "Drained"
        ]
        st.multiselect("What do you feel?", Mood_options)
        Prceding_evnts = ["Something did  not go as expected",
                          "Something unfair",
                          "Something unpleasant",
                          "I dont know",
                          ]
        st.multiselect("what happened?", Prceding_evnts)
        post_event = ["Prayer",
                      "Patience",
                      "Perseverance",
                      "Assesrtive",
                      "Whatever Clamity befalls you",
                      "Honesty",
                      "Gratitude",
                      "Generous",
                      "What is the point?"]


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

    choices = [
        "stay in Comfort zone",
        "Get rid of boredom",
        "Gain some relief",
        "Gain dopamine"
    ]
    st.multiselect("what are your intentions?", choices)


    with tab_thinkingError:
        class Evaluate:
            def __init__(self, options, key):
                self.selected = st.multiselect(
                    "What is  Reasoning process?",
                    options,
                    key=key
                )


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
        if "predicting someone else's nice behaviour" in errors.selected:
            st.write("Read Surah Joseph")
        if "Catastrophizing" in errors.selected:
            st.write("You have been through worse"
                     "Read Surah Joseph")
        if "Entitelment" in errors.selected:
            st.caption("then to Him is your return")
        if "False sense of helplessness" in errors.selected:
            st.write("Seek Guidance through Sbr and Salah!")
        if "Discounting the positive" in errors.selected:
            st.write("Maybe the Context is wrong")
        if"It should go my way" in errors.selected:
            st.caption("Ultimately God will prevails")

        POINTS_PER_TASK = 1

        st.header("Perception Profile")

        # Attention
        st.write("What do they notice repeatedly")
        attention = ["Threats", "Opportunities", "Beauty", "Status", "Meaning", "Relationships"]
        atntn_scr = {
            t: st.checkbox(t, key=f"attention_{t}")
            for t in attention
        }

        st.divider()

        Interpretation = [
            "Optimistic", "Pessimistic",
            "Personal Blame", "External Blame",
            "Logical", "Emotional",
            "Concrete", "Abstract"
        ]

        st.write("How do they explain events?")

        intprtn_scr = {
            t: st.checkbox(t, key=f"interpretation_{t}")
            for t in Interpretation
        }

        st.divider()
        # Emotion
        st.write("Dominant Affect?")
        emotion = ["Calm", "Fearful", "Curious", "Defensive", "Hopeful", "Detached"]
        emtn_scr = {
            t: st.checkbox(t, key=f"emotion_{t}")
            for t in emotion
        }

        st.divider()

        # Behavior
        st.write("Perception eventually appears as Actions")
        behavior = ["Avoidance", "Exploration", "Control", "Connection", "Creativity", "Aggression"]
        bhvr_scr = {
            t: st.checkbox(t, key=f"behavior_{t}")
            for t in behavior
        }

        # Calculate score
        # Calculate score
        score_daily = (
                              sum(atntn_scr.values()) +
                              sum(emtn_scr.values()) +
                              sum(bhvr_scr.values())
                      ) * POINTS_PER_TASK

        st.write(f"Score: {score_daily}")
        if score_daily <5:
            st.write("Very narrow minded")
        elif score_daily <10:
            st.write("Narrow minded")
        elif score_daily <15:
            st.write("Broad Minded")
        elif score_daily <20:
            st.write("Liberal")



#----------------------------


if page == "Outcomes":
    with st.container(border=True):
        # DATA
        intensity = [
            "Non-stimulating",
            "Mild stimulating",
            "Very intense",
            "Overwhelming",
        ]

        emotional_valence_optns = [
            "Sad",
            "Happy",
            "Great",
            "Awful",
            "Peaceful",
            "Neutral"
        ]

        expectation_optns = [
            "Make a meaningful connection",
            "Make good memories",
            "Time pass",
            "Change perception"
        ]

        context_options = [
            "I dont want to interact with anyone",
            "I want to interact with someone"
        ]

        outcomes_optns = ["100 % allighnment with expectation",
                          "50% allignment",
                          "25%",
                          "15%",
                          "<5%",
                          "completely opposite to expectation"

                          ]


        class DeltaExperience:

            def intensity(self, options, key):
                return st.multiselect(
                    "What is the intensity?",
                    options,
                    key=key
                )

            def emotional_valence(self, options, key):
                return st.multiselect(
                    "How is your mood?",
                    options,
                    key=key
                )

            def expectation(self, options, key):
                return st.multiselect(
                    "What are you expecting from this experience?",
                    options,
                    key=key
                )

            def context(self, options, key):
                return st.multiselect(
                    "What is the current interpretation of past self?",
                    options,
                    key=key
                )
            def perception(self,options):
                return st.radio("Did perception change?", binary_ans)




        # creating OBJECT
        experience_1 = DeltaExperience()
# calling methods on the object: objectname.methodname(arg1, arg2, arg3, key="key")
        selected_intensity = experience_1.intensity(intensity, key="intensity")
        selected_emotion = experience_1.emotional_valence(emotional_valence_optns, key="emotion_1")
        selected_expectation = experience_1.expectation(expectation_optns, key="expectation_1")
        selected_context = experience_1.context(context_options, key="context_1")

        exp_name = st.text_input("Name this experience", key="name_1")

        E1 = st.write(f"""
        ### Your {exp_name} Experience Summary 
        Intensity: {selected_intensity} , Mood: {selected_emotion} , Expectation: {selected_expectation},

        Context: {selected_context}
        """)

        # SECOND EXPERIENCE
        experience_2 = DeltaExperience()

        intensity_2nd = experience_2.intensity(intensity, key="intensity_2")
        emotion_2nd = experience_2.emotional_valence(emotional_valence_optns, key="emotion_2")
        perception_delta = experience_2.perception(binary_ans)
        context_2nd = experience_2.context(context_options, key="context_2")

        exp_name_2nd = st.text_input("Name this experience", key="name_2")

        E2 = st.write(f"""
        ### Your {exp_name_2nd} Experience Summary

        Intensity: {intensity_2nd}

        Mood: {emotion_2nd}

        perception: {perception_delta}

        Context: {context_2nd}
        """)




if page == "Human Interaction guide":
    topics_undesirable_hawk= ["Technology/Innovation",
              "Work",
              "Politics",
              "Sports",
              "Current affairs"]
    topics_undesraable_dove =[
              "Experirence",
                         "organizing",
                         "Fashion"]
    with (st.container(border=True)):
        Ess = ["Hawk",
               "Dove", ]
        cutness_ess = [
            "Retaliator",
            "Prober-Retaliator"]

        connection = st.radio("Does it has to be a connection?", binary_ans, index=None)
        st.write("A connection is a relationship that is established between two people.")
        if connection == "yes":
            type = st.radio("What type of connection is this?", ["Desirable", "Undesirable"], index=None)
            if type == "Desirable":
                cutness = st.radio("Are they cute?", binary_ans, index=None)
                if cutness == "yes":
                    smartness = st.radio("Are they smart?", binary_ans, index=None)
                    if smartness == "yes":
                        respect = st.radio("Are they respectful?", binary_ans, index=None)
                        if respect == "yes":
                            care = st.radio("Are they caring?", binary_ans, index=None)
                            if care == "yes":
                                wealth = st.radio("Are they generous?", binary_ans, index=None)
                                if wealth == "yes":
                                    passion_w = st.radio("Are they passionate?", binary_ans, index=None)
                                    if passion_w == "yes":
                                        genuine = st.radio("Are they genuine?", binary_ans, index=None)
                                        if genuine == "yes":
                                            st.write("Rare?")
                                        elif genuine == "No":
                                            st.write("Just talk and get more info")

                                    elif passion_w == "No":
                                        passion_info = st.radio("Not information?", binary_ans)

                                        if passion_info == "yes":
                                            nonpass_genuine = st.radio("Are they genuine?", binary_ans, index=None)
                                        if nonpass_genuine == "yes":
                                            st.write("5%??")
                                        elif nonpass_genuine == "No":
                                            st.write(
                                                "Non-passion, non-genuine, wealthy,smart, respectful, caring and cute! "
                                                "You know what is the first step!"
                                                "Infatuation")

                                elif wealth == "No":
                                    passion_p = st.radio("Are they passionate?", binary_ans, index=None)
                                    if passion_p == "yes":
                                        st.write("You could find out more")
                                    elif passion_p == "No":
                                        cuteEss = st.radio("choose Evolutionary stable strategy", cuteness_Ess,
                                                           index=None)
                                        if cuteEss == "Retaliator":
                                            st.write(
                                            "Behave peacefully at first, but fights back if attacked.")

                                        elif cuteEss == "Prober-Retaliator":
                                            st.write("Occasionally tests opponents with aggression")


                            elif care == "No":
                                st.write("HMMM!Need more information!")
                        elif respect == "No":
                            jerk = st.radio("Are they an asshole?", binary_ans, index=None)
                    elif smartness == "No":
                        st.write("Just ###F")

                # N non-cute connection
                elif cutness == "No":
                    desperation = st.radio("Are you desperate?", binary_ans, index=None)
                    if desperation == "yes":
                        st.write("Why are you desperate?, Consider changing "
                                 "your standards")
                    elif desperation == "No":
                        family=st.radio("Is it family?", binary_ans, index=None)

            # non-cute and undesirable
            elif type == "Undesirable":
                encounter = st.radio("Is more than one encounter probable?", binary_ans, index=None)
                if encounter == "yes":
                    chosenEss = st.radio("choose Evolutionary stable strategy", Ess, index=None)
                    if chosenEss == "Hawk":
                        st.write("A Hawk escalates conflict immediately.")
                        st.caption("Topics to discuss ")
                        st.radio("Choose topics", topics_undesirable_hawk, index=None)
                    elif chosenEss == "Dove":
                        st.write("A Dove avoids serious conflict.")
                        st.caption("Recomended strategy: Silent treatment with frequent smiles")
                        st.caption("Topics to discuss ")
                        st.radio("Choose topics", topics_undesirable_dove, index=None)



                elif encounter == "No":
                    st.write("Then what are you worried about? "
                             "how many filters do you need to wear?")

        elif connection == "No":
            probableConectn= st.radio("Maybe a connection?", binary_ans, index=None)
            if probableConectn == "yes":
                st.write("Go with the flow")
            elif probableConectn=="No":
                st.caption("why are you meeting then?")







