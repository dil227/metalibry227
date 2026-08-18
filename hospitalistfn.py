import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Clinical Workflow", layout="centered")


tab_admit, tab_progress, tab_dc,tab_chiefcomplaint = st.tabs(["Admission", "Daily Progress", "Discharge","Chief Complaint"])

# --------------------
# ADMISSION
# --------------------
with tab_admit:
    st.header("Admission Checklist")

    with st.container(border=True):
        st.subheader("Clinical Pearl")

        st.info(
            "Before admission, confirm that the working diagnosis is reasonably "
            "supported and immediate life-threatening conditions have been addressed. "
            "Review vital-sign trends, oxygen requirements, important labs and imaging, "
            "medications, functional status, code status, and disposition barriers. "
            "Determine whether inpatient or observation status is appropriate and avoid "
            "anchoring prematurely."
        )

    with st.container(border=True):
        st.title("Admission Order Set")

        tasks = [
            "Inpatient versus observation",
            "Diet",
            "DVT prophylaxis",
            "Additional order sets",
            "IV fluids",
            "Medication reconciliation",
            "Code status"
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



def show_pearls(pearls):
    with st.container(border=True):
        st.markdown("### Clinical Pearls")
        for pearl in pearls:
            st.write(f"• {pearl}")


with tab_chiefcomplaint:

    with st.container(border=True):

        chiefComplaint = st.radio(
            "What is the chief complaint?",
            [
                "Chest pain",
                "Abdominal pain",
                "Stroke like symptoms",
                "AMS",
                "SOB",
                "Headache",
                "Syncope",
                "Dehydration"
            ],
            index=None
        )

    # -------------------------------------------------
    # CHEST PAIN
    # -------------------------------------------------
    if chiefComplaint == "Chest pain":

        show_pearls([
            "A reassuring description of the pain should not close the ACS pathway. "
            "Ischemia may coexist with dyspnea, nausea, diaphoresis, weakness, or very little pain.",

            "A troponin is a time-stamped measurement, not a diagnosis. "
            "Symptom timing, serial change, ECG findings, and the overall clinical probability matter:consider"
            " Delta troponin.",

            "Before reflexively treating presumed ACS, reconsider aortic pathology when pain was "
            "abrupt and maximal at onset, particularly with neurologic findings, pulse asymmetry, "
            "or a significant blood-pressure difference."
        ])
        initial_trop = st.number_input("Initial hs-Troponin", min_value=0.0)
        repeat_trop = st.number_input("Repeat hs-Troponin", min_value=0.0)

        if initial_trop > 0:
            absolute_delta = repeat_trop - initial_trop
            relative_delta = (absolute_delta / initial_trop) * 100

            st.write(f"Absolute delta: {absolute_delta:.1f} ng/L")
            st.write(f"Relative delta: {relative_delta:.1f}%")



    # -------------------------------------------------
    # ABDOMINAL PAIN
    # -------------------------------------------------
    elif chiefComplaint == "Abdominal pain":

        show_pearls([
            "Do not confuse an abnormal CT finding with the cause of today's symptoms. "
            "Ask whether the finding anatomically, physiologically, and temporally explains the presentation.",

            "Discordance matters. Severe pain with a surprisingly benign abdominal examination "
            "should broaden rather than narrow the differential, particularly in patients with vascular risk.",

            "The trajectory is often more informative than the first snapshot. "
            "Serial abdominal examinations, vital-sign trends, oral tolerance, and evolution of pain "
            "can change the diagnosis after an initially nondiagnostic workup."
        ])

        with st.container(border=True):
            st.write(
                "Accurate history and physical examination remain central to determining "
                "which abdominal pathology is actually responsible for the current presentation."
            )

            st.write(
                "CT, MRI, ultrasound, X-ray and HIDA are adjuncts to the clinical assessment. "
                "Incidental abnormalities should not automatically become the admitting diagnosis."
            )


    # -------------------------------------------------
    # STROKE
    # -------------------------------------------------
    elif chiefComplaint == "Stroke like symptoms":

        show_pearls([
            "A low NIHSS does not necessarily mean a nondisabling stroke. "
            "Aphasia, visual loss, dominant-hand weakness, or severe gait dysfunction can be "
            "functionally devastating despite a small numerical score.",

            "Document LAST KNOWN WELL, not simply when the patient was found abnormal. "
            "Those are often very different times and may completely change treatment eligibility.",

            "Do not let a low NIHSS make posterior circulation symptoms disappear from the differential. "
            "Diplopia, dysarthria, severe ataxia, vertigo with neurologic findings, or inability to walk "
            "deserve particular attention."
        ])


    # -------------------------------------------------
    # ALTERED MENTAL STATUS
    # -------------------------------------------------
    elif chiefComplaint == "AMS":

        show_pearls([
            "The most useful neurologic test may be a phone call. "
            "Establish the patient's cognitive and functional baseline from family, facility staff, "
            "or caregivers before deciding how abnormal the current examination really is.",

            "Medication reconciliation is part of the diagnostic workup, not administrative cleanup. "
            "Recent additions, dose changes, missed medications, sedatives, anticholinergics, opioids, "
            "and withdrawal states can explain otherwise mysterious AMS.",

            "Delirium fluctuates. A patient becoming lucid during rounds does not prove that the process "
            "has resolved or that the underlying cause has been identified."
        ])


    # -------------------------------------------------
    # SHORTNESS OF BREATH
    # -------------------------------------------------
    elif chiefComplaint == "SOB":

        show_pearls([
            "Shortness of breath is sometimes the presenting manifestation of myocardial ischemia. "
            "The decision to obtain troponin should therefore depend on ischemic suspicion, "
            "not simply whether chest pain is present.",

            "When the chest X-ray, BNP, examination, and clinical story disagree, bedside cardiac "
            "and lung ultrasound can be more informative than simply ordering another laboratory test.",

            "Do not force every hypoxic patient into pneumonia versus CHF. "
            "Mixed physiology is common: infection can precipitate heart failure, PE can coexist "
            "with another pulmonary process, and several mechanisms may contribute simultaneously."
        ])

        with st.container(border=True):

            st.write(
                "Depending on the presentation, consider:"
            )

            soborder = [
                "Chest X-ray",
                "BNP / NT-proBNP when heart failure is clinically plausible",
                "Troponin when there is concern for myocardial ischemia — chest pain is not required",
                "D-dimer / CTA PE based on pre-test probability",
                "Respiratory viral panel when clinically relevant",
                "Bedside lung/cardiac ultrasound when available",
                "Consider CT chest when significant pulmonary pathology remains suspected "
                "despite an unrevealing initial evaluation"
            ]

            for task in soborder:
                st.checkbox(task)


    # -------------------------------------------------
    # HEADACHE
    # -------------------------------------------------
    elif chiefComplaint == "Headache":

        show_pearls([
            "A history of migraine is a risk for anchoring, not a rule-out test. "
            "A meaningful change in onset, intensity, associated symptoms, or neurologic examination "
            "should be treated as a new headache phenotype.",

            "Ask how quickly the headache reached maximal intensity. "
            "'10/10 headache' and 'maximal within seconds' are clinically different pieces of information.",

            "When evaluating possible subarachnoid hemorrhage, the timing of the CT matters. "
            "A negative scan obtained early and a negative scan obtained substantially later "
            "do not carry identical diagnostic meaning."
        ])


    # -------------------------------------------------
    # SYNCOPE
    # -------------------------------------------------
    elif chiefComplaint == "Syncope":

        show_pearls([
            "The diagnosis is often hidden in the 30 seconds before loss of consciousness. "
            "Exertion, position, palpitations, prodrome, pain, urination, defecation, and medication timing "
            "may be more informative than a broad laboratory panel.",

            "A normal ECG now does not prove the rhythm was normal when cerebral perfusion was lost. "
            "Syncope without prodrome, during exertion, or while supine deserves greater concern "
            "for a cardiac mechanism.",

            "Avoid admitting the laboratory abnormality instead of the patient. "
            "Mild dehydration, modest electrolyte abnormalities, or incidental imaging findings "
            "should explain the physiology of the syncopal event before becoming the diagnosis."
        ])


    # -------------------------------------------------
    # DEHYDRATION
    # -------------------------------------------------
    elif chiefComplaint == "Dehydration":

        show_pearls([
            "Dehydration describes physiology; it does not explain why it happened. "
            "Look for the imbalance: poor intake, GI loss, fever, osmotic diuresis, medications, "
            "renal losses, bleeding, or another systemic illness.",

            "An elevated creatinine does not automatically mean the patient needs liters of fluid. "
            "Determine whether the patient is actually volume depleted and simultaneously look "
            "for pulmonary or systemic congestion.",

            "Improvement in blood pressure after fluids does not complete the diagnosis. "
            "Ask what produced the volume deficit and whether that underlying process is still active."
        ])

    st.caption(
        "Clinical pearls are decision-support prompts and should be interpreted "
        "with the individual presentation and local protocols."
    )