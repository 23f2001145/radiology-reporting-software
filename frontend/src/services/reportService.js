import api from "../api/axios"

async function transcribeReport(selectedFile){
    const formData = new FormData() 
    formData.append("audio_file", selectedFile)

    const response = await api.post(
        '/reports/transcribe',
        formData
    )
    return response.data;
}

export default transcribeReport