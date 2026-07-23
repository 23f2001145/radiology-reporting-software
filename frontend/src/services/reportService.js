import api from "../api/axios"

export async function transcribeReport(selectedFile){
    const formData = new FormData() 
    formData.append("audio_file", selectedFile)

    const response = await api.post(
        '/reports/transcribe',
        formData
    )
    return response.data;
}

export async function saveReport(reportData) {
  const response = await api.post("/reports/save", reportData);
  return response.data;
}