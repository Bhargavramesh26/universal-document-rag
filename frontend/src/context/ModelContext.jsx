import { createContext, useState } from "react";
import { DEFAULT_MODEL } from "../constants/appConstants";
export const ModelContext = createContext();

export function ModelProvider({ children }) {

    const [selectedModel, setSelectedModel] = useState(DEFAULT_MODEL);

    return (
        <ModelContext.Provider
            value={{
                selectedModel,
                setSelectedModel,
            }}
        >
            {children}
        </ModelContext.Provider>
    );
}