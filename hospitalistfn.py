import streamlit as st

st.title("Discharge Algorith")

n = int(st.number_input("Number of patients", min_value=1, step=1))

def hospitalist():
    for i in range(n):

        st.subheader(f"Patient {i + 1}")

        vitals = st.radio(
            "Are vitals stable?",
            ("Yes", "No"),
            key=f"vitals_{i}",
            index=None
        )

        if vitals == "Yes":

            meds = st.radio(
                "Are all meds PO?",
                ("Yes", "No"),
                key=f"meds_{i}",
                index=None
            )

            if meds == "Yes":

                labs = st.radio(
                    "Are major labs stable?",
                    ("Yes", "No"),
                    key=f"labs_{i}",
                    index=None
                )

                if labs == "Yes":

                    consultants = st.radio(
                        "Are all consultants on board with the DC plan?",
                        ("Yes", "No"),
                        key=f"consultants_{i}",
                        index=None
                    )

                    if consultants == "Yes":

                        pt = st.radio(
                            "Are patient/family onboard with the DC plan?",
                            ("Yes", "No"),
                            key=f"pt_{i}",
                            index=None
                        )

                        if pt == "Yes":
                            st.success("PUT THE DC ORDER")
                        elif pt == "No":
                            disposition=st.multiselect("What is the disposition?",
                                           ["home","rehab","Other"])
                            if disposition== "rehab":
                                st.radio("Is rehab approved", ("Yes", "No"), key=f"rehab_{i}", index=None)
                    elif consultants == "No":
                        st.write("What needs done?")
                elif labs == "No":
                    st.multiselect("What is wrong?",
                                   ["Hemoglobin","Hematocrit",
                                    "Platelets","Creatinine","Bilirubin"])
            elif vitals == "No":
                st.multiselect("What is wrong?",
                               ["BP","Temp","RR","saturation","Heart rate"])



hospitalist()

