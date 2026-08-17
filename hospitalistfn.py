import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Clinical Workflow", layout="centered")


tab_admit, tab_progress, tab_dc = st.tabs(["Admission", "Daily Progress", "Discharge"])

# --------------------
# ADMISSION
# --------------------
with (tab_admit):
    st.header("Admission Checklist")
    with st.container(border=True):
        chiefComplaint = st.radio("What is the cheif complaint?",
                                  ["Chest pain",
                                   "Abdominal pain",
                                   "Stroke like symptoms",
                                   "AMS"
                                   "SOB",
                                   "Headache",
                                   "syncope",
                                   "Dehydration"])

        if chiefComplaint == "Chest pain":
            with st.container(border=True):
                st.write("Differentiate between Cardiac , pulmonary ,MSK and GI")
                cp_orderset=[
                    "EKG", "Xray","Trop" , "D-dimer", "CT-chest","BNP","Echo","",
                ]

        if chiefComplaint == "Abdominal pain":
            with st.container(border=True):
                st.write("Accurate history and physical examination"
                     " is more important than imagings and labs")
                st.write("Alot of organs in the abdomen and a number of "
                     "differential diagnoses")

    with st.container(border=True):
        st.title("Admission order set")
        tasks=["inpatient versus observation"
               "Diet",
               "DVT",
               "Additional order sets",
               "Culture?",
               "IV fluids",
               "Antibiotics",
           "Med rec",
           "code status"
               ]
        for task in tasks:
            st.checkbox(task)



    st.radio(
        "Are notes done?",["yes", "no",],index=None,
    )


    st.radio(
        "Consult needed?",
        ["Yes", "No"],
        index=None
    )





# --------------------
# DAILY PROGRESS
# --------------------
with tab_progress:
    st.header("Daily Progress")

    with st.container(border=True):
        improving = st.radio("Is the patient improving?", ["Yes", "No"], index=None, key="improving_input")

        entry = {"date": datetime.now().strftime("%Y-%m-%d %H:%M"), "improving": improving}

        if improving == "Yes":
            entry["barriers_to_discharge"] = st.multiselect(
                "What is still keeping the patient in hospital?",
                ["IV medications", "Oxygen", "Abnormal labs", "Consultant clearance", "PT/OT", "Placement", "Other"],
                key="barriers_input",
            )
            st.info("Continue current plan and reassess discharge readiness.")

        elif improving == "No":
            entry["issues"] = st.multiselect(
                "What needs attention?",
                ["Vitals", "Labs", "Imaging", "Medications", "New symptoms", "Consultants", "Other"],
                key="issues_input",
            )
            st.warning("Reassess diagnosis and treatment plan.")




# --------------------
# DISCHARGE
# --------------------
with tab_dc:
    st.header("Discharge")

    with st.container(border=True):
        vitals = st.radio(
            "Are vitals stable?",
            ("Yes", "No"),
            index=None
        )

        if vitals == "Yes":

            meds = st.radio(
                "Are all meds PO or can be changed to PO?",
                ("Yes", "No"),
                index=None
            )

            if meds == "Yes":

                labs = st.radio(
                    "Are major labs stable?",
                    ("Yes", "No"),
                    index=None
                )

                if labs == "Yes":

                    consultants = st.radio(
                        "Are all consultants on board with the DC plan?",
                        ("Yes", "No"),
                        index=None
                    )

                    if consultants == "Yes":

                        pt = st.radio(
                            "Are patient/family onboard with the DC plan?",
                            ("Yes", "No"),
                            index=None
                        )

                        if pt == "Yes":
                            st.success("PUT THE DC ORDER")
                        elif pt == "No":
                            disposition = st.multiselect("What is the disposition?",
                                                         ["home", "rehab", "Other"])
                            if disposition == "rehab":
                                st.radio("Is rehab approved", ("Yes", "No"), key=f"rehab_{i}", index=None)
                    elif consultants == "No":
                        st.write("What needs done?")
                elif labs == "No":
                    st.multiselect("What is wrong?",
                                   ["Hemoglobin", "Hematocrit",
                                    "Platelets", "Creatinine", "Bilirubin"])
            elif vitals == "No":
                st.multiselect("What is wrong?",
                               ["BP", "Temp", "RR", "saturation", "Heart rate"])


