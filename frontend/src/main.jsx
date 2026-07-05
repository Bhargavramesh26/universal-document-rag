import React from "react";
import ReactDOM from "react-dom/client";

import App from "./App";

import { SessionProvider } from "./context/SessionContext";
import { ModelProvider } from "./context/ModelContext";

ReactDOM.createRoot(document.getElementById("root")).render(
    <React.StrictMode>

        <SessionProvider>

            <ModelProvider>

                <App />

            </ModelProvider>

        </SessionProvider>

    </React.StrictMode>
);