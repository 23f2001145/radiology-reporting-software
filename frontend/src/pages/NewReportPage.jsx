import { useState } from "react";
import transcribeReport from "../services/reportService";

function NewReportPage() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [rawTranscript, setTranscript] = useState("");
  const [report, setReport] = useState(null )

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

  return (
    <>
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
        <h3>Clinical history</h3>
        <textarea
          value={report?.clinical_history ?? ""}
          onChange={
            (e)=>{
              setReport({
                ...report,
                clinical_history:e.target.value
              });
            }
          }
        ></textarea>
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
        <h3>Technique</h3>
        <textarea
          value={report?.technique ?? ""}
          onChange={
            (e)=>{
              setReport({
                ...report,
                technique:e.target.value
              });
              console.log(report);
            }
          }
        ></textarea>
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