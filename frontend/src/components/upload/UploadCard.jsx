import { useState, useContext } from "react";
import api from "../../services/api";
import { SessionContext } from "../../context/SessionContext";
import {
    DEFAULT_WORKSPACE,
    SUPPORTED_FILE_TYPES,
} from "../../constants/appConstants";

function UploadCard() {

    const [file, setFile] = useState(null);
    const [uploading, setUploading] = useState(false);

    const { setSessionId } = useContext(SessionContext);

    const uploadDocument = async () => {

        if (!file) {
            alert("Please select a document first.");
            return;
        }

        const formData = new FormData();

        formData.append("file", file);
        formData.append("workspace", DEFAULT_WORKSPACE);;

        setUploading(true);

        try {

            const response = await api.post(
                "/upload",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            );

            setSessionId(response.data.session_id);

            setStatus("Document uploaded successfully.");

            setFile(null);

        } catch (error) {

            if (import.meta.env.DEV) {
                console.error(error);
            }
            
            setStatus("Upload failed.");

        } finally {

            setUploading(false);

        }
    };

    return (

        <div className="card">

            <h2>Upload Document</h2>

            <input
                type="file"
                accept={SUPPORTED_FILE_TYPES}
                onChange={(e) => 
                    setFile(e.target.files[0])
                }
            />

             {
                file &&
                <p>
                    <strong>Selected:</strong>
                    {" "}
                    {file.name}
                </p>
            }

            <button
                onClick={uploadDocument}
                disabled={uploading}
            >
                {
                uploading ? "Uploading..." : "Upload"}
            </button>

            <small>

                {status}

            </small>

        </div>

    );
}

export default UploadCard;