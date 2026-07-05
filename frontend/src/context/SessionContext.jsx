import { createContext, useState } from "react";

export const SessionContext = createContext();

export function SessionProvider({ children }) {

    const [sessionId, setSessionId] = useState("");

    return (
        <SessionContext.Provider
            value={{
                sessionId,
                setSessionId,
            }}
        >
            {children}
        </SessionContext.Provider>
    );
}