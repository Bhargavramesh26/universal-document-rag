import { useContext, useEffect, useState } from "react";

import api from "../../services/api";

import { ModelContext } from "../../context/ModelContext";

function ModelSelector() {

    const [models, setModels] = useState([]);

    const {
        selectedModel,
        setSelectedModel,
    } = useContext(ModelContext);

    useEffect(() => {

        loadModels();

    }, []);

    async function loadModels() {

        try {

            const response = await api.get("/models");

            setModels(response.data.models);

        } catch (error) {

            if (import.meta.env.DEV) {
                console.error(error);
            }

        }

    }

    return (

        <div className="card">

            <h2>Select Model</h2>

            <select
                value={selectedModel}
                onChange={(e) =>
                    setSelectedModel(e.target.value)
                }
            >

                {models.map((model) => (

                    <option
                        key={model.id}
                        value={model.id}
                    >
                        {model.name}
                    </option>

                ))}

            </select>

        </div>

    );
}

export default ModelSelector;