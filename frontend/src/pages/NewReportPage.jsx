import { useState, useEffect } from "react";
import transcribeReport from "../services/reportService";
import getPatients from "../services/patientService";

function NewReportPage() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [rawTranscript, setTranscript] = useState("");
  const [report, setReport] = useState(null);
  const [patientList, setPatientList] = useState([]);
  const [selectedPatient, setSelectedPatient] = useState("")

  useEffect(()=>{
    async function loadPatients(){
      try {
        const patients = await getPatients();
        setPatientList(patients);
      }
      catch(error){
        console.log(error);
      }
    }
    loadPatients();
  }, []);

  function handleFileChange(event){
    setSelectedFile(event.target.files[0]);
  }

  async function handleSubmit(event){
    event.preventDefault();
    try{
      const result = await transcribeReport(selectedFile);
      console.log(result);
      setTranscript(result.raw_transcript);
      setReport(result.structured_report);
    }
    catch(error){
      console.error(error);
    }
  }

  async function handleSave(){
    try {
      const res = await saveReport();
      console.log(res.data);
    }
    catch(error){
      console.log(error);
    }
    console.log("saved!");
  }

  return (
    <>
      <label>
        Select a patient :
        <select value={selectedPatient} onChange={(e)=>setSelectedPatient(e.target.value)}>
          <option value="" disabled >--Select a patient--</option>
          {
            patientList.map((pt)=>{
              return (
                <option value={pt.id} key={pt.id}>{pt.patient_name}</option>
              )
            })
          }         
        </select>
      </label>
      <div>
        <h2>New Report</h2>
        <form onSubmit={handleSubmit}>
          Upload audio file : 
          <input type="file" onChange={handleFileChange}></input>
          <input type="submit" value="Generate report"></input>
        </form>
      </div>
      <div>
        <h1>Structured Report</h1>
        
        <h3>Findings</h3>
        <textarea
          value={report?.findings ?? ""}
          onChange={
            (e)=>{
              setReport({
                ...report,
                findings:e.target.value
              });
            }
          }
        ></textarea>

        <h3>Impression</h3>
        <textarea
          value={report?.impression ?? ""}
          onChange={
            (e)=>{
              setReport({
                ...report,
                impression:e.target.value
              });
            }
          }
        ></textarea>
        
        <h3>Advice</h3>
        <textarea
          value={report?.advice ?? ""}
          onChange={
            (e)=>{
              setReport({
                ...report,
                advice:e.target.value
              });
            }
          }
        ></textarea>
        <button onClick={handleSave}>Save Report</button>
      </div>
      <div>
        <h3>Raw transcript</h3>
        <div>
          {rawTranscript}
        </div>
      </div>
    </>
  );
}

export default NewReportPage;