import { APP_NAME } from "../../constants/appConstants";

function Header() {
    return (
        <header className="header">
            <h1>📄 {APP_NAME}</h1>

            <p>
                Upload documents and interact with them using
                Retrieval-Augmented Generation (RAG).
            </p>
        </header>
    );
}

export default Header;