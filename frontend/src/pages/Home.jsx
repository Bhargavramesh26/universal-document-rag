import Header from "../components/layout/Header";
import UploadCard from "../components/upload/UploadCard";
import ModelSelector from "../components/models/ModelSelector";
import ChatWindow from "../components/chat/ChatWindow";
import Footer from "../components/layout/Footer";

function Home() {
    return (
        <div className="app">

            <Header />

            <div className="sidebar">

                <UploadCard />

                <ModelSelector />

            </div>

            <ChatWindow />

            <Footer />

        </div>
    );
}

export default Home;